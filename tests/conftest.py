import sys
from datetime import datetime, timedelta
from typing import Generator

import pytest
from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.database import db as _db
from app.models import Client, ClientParking, Parking

sys.path.append("../../parking")


@pytest.fixture
def app() -> Generator[Flask, None, None]:
    _app = create_app()
    _app.config["SQLALCHEMY_ECHO"] = True
    _app.config["TESTING"] = True
    _app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    with _app.app_context():
        _db.create_all()

        client = Client(
            name="test_name_client",
            surname="test_surname_client",
            credit_card="test_credit_card_client",
            car_number="test_car_number",
        )

        parking = Parking(
            address="test_address_parking",
            opened=True,
            count_places=100,
            count_available_places=100,
        )

        client_parking = ClientParking(
            client_id=1,
            parking_id=1,
            time_in=datetime.now(),
            time_out=datetime.now() + timedelta(minutes=10),
        )

        _db.session.add(client)
        _db.session.add(parking)
        _db.session.add(client_parking)
        _db.session.commit()

        yield _app

        _db.session.close()
        _db.drop_all()


@pytest.fixture
def web_client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def db(app: Flask) -> Generator[SQLAlchemy, None, None]:
    with app.app_context():
        yield _db
