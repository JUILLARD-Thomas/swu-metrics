# Star Wars Metrics Manager

## Description

Star Wars Metrics Manager est un outil en ligne de commande pour gérer et analyser des données de jeux basés sur l'univers de Star Wars. Il permet d'ajouter des entrées à un fichier CSV, de calculer des statistiques, de classer les leaders, et d'afficher les données filtrées. Le programme offre une flexibilité considérable grâce à des filtres détaillés pour les leaders, les bases, les dates, et les plateformes.

## Fonctionnalités

- **Ajouter des entrées** : Ajouter de nouvelles entrées de jeu au fichier CSV avec des informations détaillées.
- **Calculer des statistiques** : Calculer le ratio de victoires, le ratio d'abandons, et d'autres statistiques globales ou spécifiques à des leaders, avec des filtres personnalisés.
- **Classer les leaders** : Obtenir un classement des leaders en fonction du taux de victoire, du nombre de tours moyen, et du taux d'abandon, avec des options de filtrage.
- **Afficher des données filtrées** : Afficher les lignes de données correspondant aux critères de filtrage spécifiés pour une analyse plus approfondie.

## Installation

1. **Clonez ou téléchargez le projet** :

    ```bash
    git clone https://github.com/votre-utilisateur/star-wars-metrics-manager.git
    ```

2. **Naviguez dans le répertoire du projet** :

    ```bash
    cd star-wars-metrics-manager
    ```

3. **Assurez-vous d'avoir Python 3 installé sur votre système**. Vous pouvez vérifier en exécutant :

    ```bash
    python --version
    ```

4. **Installez les dépendances requises** (s'il y en a) avec :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

### Ajouter des données

Pour ajouter une nouvelle entrée au fichier CSV, utilisez la commande suivante :

```bash
python star_wars_metrics.py add
```

Vous serez invité à entrer les détails du jeu, y compris le nom de votre leader, le nom de votre base, le leader ennemi, la base ennemie, et d'autres informations pertinentes.




## Calculer des statistiques

Pour calculer des statistiques globales ou par combinaison de leaders, utilisez la commande suivante :

```bash
python star_wars_metrics.py stat [options]


Options :

    --my_leader : Filtrer par leader allié.
    --enemy_leader : Filtrer par leader ennemi.
    --my_base : Filtrer par base alliée.
    --enemy_base : Filtrer par base ennemie.
    --date_after : Filtrer les données après cette date (format YYYY-MM-DD).
    --date_before : Filtrer les données avant cette date (format YYYY-MM-DD).
    --platform : Filtrer par plateforme.
```

## Exemple :

Pour calculer les statistiques pour un leader spécifique et un leader ennemi, avec un filtre sur la plateforme :

```bash
python star_wars_metrics.py stat --my_leader "Sabine" --enemy_leader "Kylo Ren" --platform "TTI"
```

# Classer les leaders

Pour obtenir un classement des leaders, utilisez la commande suivante :

```bash
python star_wars_metrics.py rank [options]

Options :

    --my_leader : Filtrer par leader allié.
    --enemy_leader : Filtrer par leader ennemi.
    --my_base : Filtrer par base alliée.
    --enemy_base : Filtrer par base ennemie.
    --date_after : Filtrer les données après cette date (format YYYY-MM-DD).
    --date_before : Filtrer les données avant cette date (format YYYY-MM-DD).
    --platform : Filtrer par plateforme.
```

## Exemple :

Pour classer les leaders par taux de victoire avec filtrage par plateforme :


```bash
python star_wars_metrics.py rank --platform "TTI"
```

# Afficher des données filtrées

Pour afficher les lignes de données correspondant aux critères spécifiés, utilisez la commande suivante :

```bash
python star_wars_metrics.py display [options]

Options :

    --my_leader : Filtrer par leader allié.
    --enemy_leader : Filtrer par leader ennemi.
    --my_base : Filtrer par base alliée.
    --enemy_base : Filtrer par base ennemie.
    --date_after : Filtrer les données après cette date (format YYYY-MM-DD).
    --date_before : Filtrer les données avant cette date (format YYYY-MM-DD).
    --platform : Filtrer par plateforme.
```

# Exemple :

Pour afficher les données pour une période spécifique :

```bash
python star_wars_metrics.py display --date_after "2024-01-01" --date_before "2024-12-31"
```

# Fichier CSV

Les données sont stockées dans un fichier CSV nommé star_wars_metrics.csv. Le fichier utilise les colonnes suivantes :

    - Date
    - My Leader
    - My Base
    - Enemy Leader
    - Enemy Base
    - Is WIN
    - Is Give Up?
    - Turn
    - Platform
    - Side

Les données sont toutes converties en minuscules pour assurer la cohérence des entrées.
Contribution

Les contributions sont les bienvenues ! Si vous souhaitez contribuer, veuillez soumettre une demande de tirage avec des explications détaillées. Assurez-vous de suivre les bonnes pratiques de développement et de tester les modifications avant de les soumettre.
Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

perl


Ce fichier `README.md` devrait maintenant être correctement formaté pour une utilisation facile et claire. Assure-toi de le copier et de le coller dans un éditeur de texte qui prend en charge le format Markdown pour garantir que la mise en forme est correctement rendue.

