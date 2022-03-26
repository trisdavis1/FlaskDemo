import pytest
from app import app
from app.models import User

@pytest.fixture()
def app():
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

@pytest.fixture(scope='module')
def new_user():
    user = User('byan', 'byan@mwsu.edu', '123456')
    return user
