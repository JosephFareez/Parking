from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)

from .database import db


class Client(db.Model):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    credit_card = Column(String(50), nullable=True)
    car_number = Column(String(10), nullable=True)

    def __repr__(self) -> str:
        return f"Клиент {self.name} {self.surname}"

    def to_json(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Parking(db.Model):
    __tablename__ = "parking"

    id = Column(Integer, primary_key=True)
    address = Column(String(100), nullable=False)
    opened = Column(Boolean, nullable=True)
    count_places = Column(Integer, nullable=False)
    count_available_places = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Парковка {self.address}"

    def to_json(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class ClientParking(db.Model):
    __tablename__ = "client_parking"
    __table_args__ = (UniqueConstraint("client_id", "parking_id"),)

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    parking_id = Column(Integer, ForeignKey("parking.id"), nullable=False)
    time_in = Column(DateTime, nullable=True)
    time_out = Column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"Клиент {self.client_id} место {self.parking_id}"

    def to_json(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
