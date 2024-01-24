# Scraping with Scrapy
## Projet pour la collecte d’informations sur les sites publics 

![Moteur de recherche](Images/engine.png)


## Introduction
Ce projet propose une base pour la collecte de données sur les sites publics. Dans ce projet, nous utiliserons le site http://quotes.toscrape.com comme modèle mais la solution peut être adaptée à d’autres besoins futurs.

## Caractéristiques


## Python Libraries

```pip install -r requirements.txt```

## Base des données
Vous devez modifier le fichier de configuration situé dans __simplon_scarpy/simplon_scrapy/settings.py__ avec les informations de votre base de données Mongo.

### MONGODB Settings
MONGO_URI = "localhost:27017"
MONGO_DATABASE = "scrapping-database"

## Script d'Initialisation
Le script __search_engine_init.py__ joue un rôle crucial en initialisant le moteur de recherche avec des données pertinentes. Il exporte les données de MySQL, les convertit au format JSONL, et les importe dans Typesense.

## Flask Server

### Utilisation
Pour lancer le server flask, il faut entrer la ligne de commande ci-dessous dans le terminal:
```sh
flask --app server.py --debug run
```
Le server flask permet de:

* scraper les données dans sa base:
http://localhost:5000/api/run-spider

* récupérer une citation:
http://127.0.0.1:5000/api/random_quote


## Tests
Pour exécuter les tests :

```py
python tests/test.py
```

## Contribution
Les fiers participants sont:
* [Jhonatan Caldeira](https://github.com/JhonatanCaldeira)

Avec l'aimable participation des formateurs:
* [Adrien Dulac](https://github.com/dtrckd)
* [Antonys Schultz](https://github.com/DeVerMyst)

## Licence
[MIT](https://choosealicense.com/licenses/mit/)
