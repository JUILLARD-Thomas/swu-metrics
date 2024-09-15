#!/usr/bin/env python3

import csv
import argparse
from datetime import datetime
from collections import defaultdict

# Nom du fichier CSV
filename = 'star_wars_metrics.csv'
date_format = '%Y-%m-%d'  # Format de la date utilisé dans le fichier CSV

def add_entry():
    """Ajoute une nouvelle entrée au fichier CSV."""
    date = datetime.now().strftime(date_format)  # Date du jour au format YYYY-MM-DD
    my_leader = input("Entrez le nom de votre leader : ").lower()
    my_base = input("Entrez le nom de votre base : ").lower()
    enemy_leader = input("Entrez le nom du leader ennemi : ").lower()
    enemy_base = input("Entrez le nom de la base ennemie : ").lower()
    is_win = input("Avez-vous gagné ? (0 pour non, 1 pour oui) : ")
    is_give_up = input("Avez-vous abandonné ? (0 pour non, 1 pour oui) : ")
    turn = input("Entrez le nombre de tours : ")
    platform = input("Entrez la plateforme : ").lower()
    side = input("Entrez le side: ").lower()
    comment = input("Entrez un commentaire : ").lower()

    file_exists = False
    try:
        with open(filename, 'r') as file:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Date', 'My Leader', 'My Base', 'Enemy Leader', 'Enemy Base', 'Is WIN', 'Is Give Up?', 'Turn', 'Platform', 'Side', 'Comment'])
        writer.writerow([date, my_leader, my_base, enemy_leader, enemy_base, is_win, is_give_up, turn, platform, side, comment])

    print(f"Les données ont été ajoutées au fichier {filename}.")

def filter_games(my_leader_filter=None, enemy_leader_filter=None, my_base_filter=None, enemy_base_filter=None, date_after=None, date_before=None, platform_filter=None):
    """Filtre les parties depuis le fichier CSV selon les critères donnés."""
    filtered_rows = []

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convertir les valeurs du fichier en minuscules pour comparaison
                row['My Leader'] = row['My Leader'].lower()
                row['My Base'] = row['My Base'].lower()
                row['Enemy Leader'] = row['Enemy Leader'].lower()
                row['Enemy Base'] = row['Enemy Base'].lower()
                row['Platform'] = row['Platform'].lower()
                row['Side'] = row['Side'].lower()
                
                # Appliquer les filtres
                if my_leader_filter and row['My Leader'] != my_leader_filter.lower():
                    continue
                if enemy_leader_filter and row['Enemy Leader'] != enemy_leader_filter.lower():
                    continue
                if my_base_filter and row['My Base'] != my_base_filter.lower():
                    continue
                if enemy_base_filter and row['Enemy Base'] != enemy_base_filter.lower():
                    continue
                if platform_filter and row['Platform'] != platform_filter.lower():
                    continue

                row_date = datetime.strptime(row['Date'], date_format)
                if date_after and row_date < date_after:
                    continue
                if date_before and row_date > date_before:
                    continue

                filtered_rows.append(row)

        return filtered_rows

    except FileNotFoundError:
        print("Le fichier CSV n'existe pas. Assurez-vous que les données ont été ajoutées.")
        return []

def calculate_win_ratio(my_leader_filter=None, enemy_leader_filter=None, my_base_filter=None, enemy_base_filter=None, date_after=None, date_before=None, platform_filter=None):
    """Calcule des statistiques globales par combinaison My Leader / Enemy Leader."""
    stats_by_leader_pair = defaultdict(lambda: {'games': 0, 'wins': 0, 'giveups': 0, 'turns': 0})

    filtered_rows = filter_games(
        my_leader_filter=my_leader_filter, 
        enemy_leader_filter=enemy_leader_filter, 
        my_base_filter=my_base_filter, 
        enemy_base_filter=enemy_base_filter, 
        date_after=date_after, 
        date_before=date_before, 
        platform_filter=platform_filter
    )

    total_games = 0
    total_wins = 0

    for row in filtered_rows:
        my_leader = row['My Leader'].lower()
        enemy_leader = row['Enemy Leader'].lower()
        pair_key = (my_leader, enemy_leader)

        stats_by_leader_pair[pair_key]['games'] += 1
        stats_by_leader_pair[pair_key]['turns'] += int(row['Turn'])
        if row['Is WIN'] == '1':
            stats_by_leader_pair[pair_key]['wins'] += 1
            total_wins += 1
        if row['Is Give Up?'] == '1':
            stats_by_leader_pair[pair_key]['giveups'] += 1

        total_games += 1

    if total_games == 0:
        print("Aucune donnée trouvée avec les filtres appliqués.")
        return

    # Afficher les statistiques par paire de leaders
    print("Statistiques par combinaison My Leader / Enemy Leader :")
    print(f"{'My Leader':<20} {'Enemy Leader':<20} {'Victoires (%)':<15} {'Abandons (%)':<15} {'Tours Moyens':<15} {'Parties Jouées':<15}")

    for (my_leader, enemy_leader), stats in stats_by_leader_pair.items():
        win_ratio = (stats['wins'] / stats['games']) * 100 if stats['games'] > 0 else 0
        give_up_ratio = (stats['giveups'] / stats['games']) * 100 if stats['games'] > 0 else 0
        avg_turns = stats['turns'] / stats['games'] if stats['games'] > 0 else 0
        print(f"{my_leader:<20} {enemy_leader:<20} {win_ratio:<15.2f} {give_up_ratio:<15.2f} {avg_turns:<15.2f} {stats['games']:<15}")

    # Afficher le ratio global si souhaité
    win_ratio_global = (total_wins / total_games) * 100 if total_games > 0 else 0
    print(f"\nRatio de victoires global : {win_ratio_global:.2f}%")

def rank_leaders(my_leader_filter=None, enemy_leader_filter=None, my_base_filter=None, enemy_base_filter=None, date_after=None, date_before=None, platform_filter=None):
    """Classe les leaders par taux de victoire, nombre de tours et taux d'abandon."""
    leader_stats = defaultdict(lambda: {'games': 0, 'wins': 0, 'giveups': 0, 'turns': 0})

    filtered_rows = filter_games(
        my_leader_filter=my_leader_filter, 
        enemy_leader_filter=enemy_leader_filter, 
        my_base_filter=my_base_filter, 
        enemy_base_filter=enemy_base_filter, 
        date_after=date_after, 
        date_before=date_before, 
        platform_filter=platform_filter
    )

    for row in filtered_rows:
        leader = row['My Leader']
        leader_stats[leader]['games'] += 1
        leader_stats[leader]['turns'] += int(row['Turn'])  # Accumuler le nombre de tours
        if row['Is WIN'] == '1':
            leader_stats[leader]['wins'] += 1
        if row['Is Give Up?'] == '1':
            leader_stats[leader]['giveups'] += 1

    if not leader_stats:
        print("Aucune donnée trouvée.")
        return

    # Calcul des taux et des stats pour chaque leader
    leader_ranking = []
    for leader, stats in leader_stats.items():
        win_ratio = (stats['wins'] / stats['games']) * 100 if stats['games'] > 0 else 0
        give_up_ratio = (stats['giveups'] / stats['games']) * 100 if stats['games'] > 0 else 0
        avg_turns = stats['turns'] / stats['games'] if stats['games'] > 0 else 0
        leader_ranking.append((leader, win_ratio, give_up_ratio, avg_turns, stats['games']))

    # Trier les leaders par taux de victoire décroissant
    leader_ranking.sort(key=lambda x: x[1], reverse=True)

    # Afficher le classement avec les nouvelles stats
    print("Classement des leaders par taux de victoire :")
    print(f"{'Leader':<15} {'Victoires (%)':<15} {'Abandons (%)':<15} {'Tours Moyens':<15} {'Parties Jouées':<15}")
    for rank, (leader, win_ratio, give_up_ratio, avg_turns, games) in enumerate(leader_ranking, start=1):
        print(f"{leader:<15} {win_ratio:<15.2f} {give_up_ratio:<15.2f} {avg_turns:<15.2f} {games:<15}")

def display_filtered_data(my_leader_filter=None, enemy_leader_filter=None, my_base_filter=None, enemy_base_filter=None, date_after=None, date_before=None, platform_filter=None):
    """Affiche les lignes de données en fonction des filtres spécifiés."""
    
    # Filtrer les données en utilisant les filtres spécifiés
    filtered_rows = filter_games(
        my_leader_filter=my_leader_filter, 
        enemy_leader_filter=enemy_leader_filter, 
        my_base_filter=my_base_filter, 
        enemy_base_filter=enemy_base_filter, 
        date_after=date_after, 
        date_before=date_before, 
        platform_filter=platform_filter
    )
    
    if not filtered_rows:
        print("Aucune donnée trouvée avec les filtres appliqués.")
        return

    # Afficher les en-têtes de colonne
    print(f"{'Date':<12} {'My Leader':<20} {'My Base':<15} {'Enemy Leader':<20} {'Enemy Base':<15} {'Is WIN':<6} {'Is Give Up?':<12} {'Turn':<5} {'Platform':<10} {'Side':<25} {'Comment':<50}")

    # Afficher les données filtrées
    for row in filtered_rows:
        print(f"{row['Date']:<12} {row['My Leader']:<20} {row['My Base']:<15} {row['Enemy Leader']:<20} {row['Enemy Base']:<15} {row['Is WIN']:<6} {row['Is Give Up?']:<12} {row['Turn']:<5} {row['Platform']:<10} {row['Side']:<25} {row['Comment']:<50}")

def main():
    parser = argparse.ArgumentParser(description="Gestion des parties de Star Wars.")
    parser.add_argument(
        'command',
        choices=['add', 'stat', 'rank', 'display'],
        help="La commande à exécuter : 'add' pour ajouter des données, 'stat' pour afficher les statistiques, 'rank' pour classer les leaders, 'display' pour afficher les données filtrées."
    )

    parser.add_argument('--my_leader', help="Filtrer par leader allié.")
    parser.add_argument('--enemy_leader', help="Filtrer par leader ennemi.")
    parser.add_argument('--my_base', help="Filtrer par base alliée.")
    parser.add_argument('--enemy_base', help="Filtrer par base ennemie.")
    parser.add_argument('--date_after', help="Filtrer les données après cette date (format YYYY-MM-DD).")
    parser.add_argument('--date_before', help="Filtrer les données avant cette date (format YYYY-MM-DD).")
    parser.add_argument('--platform', help="Filtrer par plateforme.")

    args = parser.parse_args()

    if args.command == 'add':
        add_entry()
    elif args.command == 'stat':
        calculate_win_ratio(
            my_leader_filter=args.my_leader,
            enemy_leader_filter=args.enemy_leader,
            my_base_filter=args.my_base,
            enemy_base_filter=args.enemy_base,
            date_after=args.date_after,
            date_before=args.date_before,
            platform_filter=args.platform
        )
    elif args.command == 'rank':
        rank_leaders(
            my_leader_filter=args.my_leader,
            enemy_leader_filter=args.enemy_leader,
            my_base_filter=args.my_base,
            enemy_base_filter=args.enemy_base,
            date_after=args.date_after,
            date_before=args.date_before,
            platform_filter=args.platform
        )
    elif args.command == 'display':
        display_filtered_data(
            my_leader_filter=args.my_leader,
            enemy_leader_filter=args.enemy_leader,
            my_base_filter=args.my_base,
            enemy_base_filter=args.enemy_base,
            date_after=args.date_after,
            date_before=args.date_before,
            platform_filter=args.platform
        )

if __name__ == "__main__":
    main()
