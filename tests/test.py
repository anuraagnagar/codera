import pytest

from flask_blog import blog_app

@pytest.fixture()
def app():
    app = blog_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()