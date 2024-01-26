# Scraping with Scrapy
Projet pour la collecte d’informations sur les sites publics 

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


## Flask Server

### Utilisation
Pour lancer le server flask, il faut entrer la ligne de commande ci-dessous dans le terminal:
```sh
flask --app server.py --debug run
```
Le server flask permet de:

* scraper les données dans sa base:
http://localhost:5000/api/run_spider

* récupérer une citation:
http://127.0.0.1:5000/api/random_quote

* vérifier les logs:
http://127.0.0.1:5000/api/get_log

## Streamlit
Vous pouvez visualizer les données à partir d'une page Streamlit:
```sh
streamlit run main.py
```
## Logs

### Flask
Le fichier __flask.log__ contiendra les tout les logs FLASK à niveau DEBUG.

### Scrapy
Le fichier __spider_quotes.log__ aura toutes les informations relatives aux logs de l’instance Scrapy Quotes.

Pour modifier les paramètres du log vérifier les paramètres dans __settings.log__.

## Contribution
Les fiers participants sont:
* [Jhonatan Caldeira](https://github.com/JhonatanCaldeira)

Avec l'aimable participation des formateurs:
* [Adrien Dulac](https://github.com/dtrckd)
* [Antonys Schultz](https://github.com/DeVerMyst)

## Licence
[MIT](https://choosealicense.com/licenses/mit/)
