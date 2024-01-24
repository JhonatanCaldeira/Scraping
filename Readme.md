# Scraping with Scrapy
## Projet pour la collecte d’informations sur les sites publics 

![Moteur de recherche](Images/engine.png)


## Introduction
Ce projet propose une base pour la collecte de données sur les sites publics. Dans ce projet, nous utiliserons le site http://quotes.toscrape.com comme modèle mais la solution peut être adaptée à d’autres besoins futurs.

## Caractéristiques


## Python Libraries

```pip install -r requirements.txt```

## Fichiers de configuration
Vous devez modifier le fichier de configuration situé dans __.env__ avec les informations de votre base de données et de votre serveur typesense.

## Script d'Initialisation
Le script __search_engine_init.py__ joue un rôle crucial en initialisant le moteur de recherche avec des données pertinentes. Il exporte les données de MySQL, les convertit au format JSONL, et les importe dans Typesense.

## Flask Server

### Utilisation
Pour lancer le server flask, il faut entrer la ligne de commande ci-dessous dans le terminal:
```sh
flask --app server.py --debug run
```
Le server flask permet de configurer des routes (url) qui vont être utilisée:

* soit pour charger une table,
exemple: 
Pour charger la table food on va taper:
http://localhost:5000/9moisacroquer/UpdateCollection?table_name=food

* soit pour effectuer une recherche:
exemple:
on entre dans la barre de recherche les termes à rechercher et le serveur va faire plusieurs requêtes dans les tables, préalablement chargées, à l'adresse suivante:
http://localhost:5000/9moisacroquer/SearchCollection
si les termes sont: carences en fer, il va rechercher tous les textes contenant "fer", "carences" et "carences fer".


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
