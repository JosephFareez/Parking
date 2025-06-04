from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .database import Model


class Client(Model):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    credit_card: Mapped[str | None] = mapped_column(String(50), nullable=True)
    car_number: Mapped[str | None] = mapped_column(String(10), nullable=True)

    def __repr__(self) -> str:
        return f"Клиент {self.name} {self.surname}"

    def to_json(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Parking(Model):
    __tablename__ = "parking"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    opened: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    count_places: Mapped[int] = mapped_column(Integer, nullable=False)
    count_available_places: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Парковка {self.address}"

    def to_json(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class ClientParking(Model):
    __tablename__ = "client_parking"
    __table_args__ = (UniqueConstraint("client_id", "parking_id"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), nullable=False)
    parking_id: Mapped[int] = mapped_column(ForeignKey("parking.id"), nullable=False)
    time_in: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    time_out: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"Клиент {self.client_id} место {self.parking_id}"

    def to_json(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
