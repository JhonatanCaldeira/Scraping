import pytest
import pymongo
from server import app


@pytest.fixture()
def app_flask():
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app


@pytest.fixture()
def client(app_flask):
    return app_flask.test_client()


@pytest.fixture()
def runner(app_flask):
    return app_flask.test_cli_runner()


def test_api(client):
    response = client.get("/api/random_quote")
    assert response.status_code == 200


def test_scrap(client):
    response = client.get("/api/run_spider")
    assert response.status_code == 200


# testing the mongodb connection


@pytest.fixture()
def mongo_connection():
    try:
        client = pymongo.MongoClient()
        return client
    except Exception:
        pytest.fail("Could not yield DB client")


def test_mongo_db(mongo_connection):
    try:
        mongo_connection.quote_db
    except Exception:
        pytest.fail("Could not connect to MongoDB")
