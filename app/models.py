from .database import db


class Client(db.Model):
    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    credit_card = db.Column(db.String(50), nullable=True)
    car_number = db.Column(db.String(10), nullable=True)

    def __repr__(self) -> str:
        return f"Клиент {self.name} {self.surname}"

    def to_json(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class Parking(db.Model):
    __tablename__ = "parking"

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), nullable=False)
    opened = db.Column(db.Boolean, nullable=True)
    count_places = db.Column(db.Integer, nullable=False)
    count_available_places = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Парковка {self.address}"

    def to_json(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


class ClientParking(db.Model):
    __tablename__ = "client_parking"
    __table_args__ = (db.UniqueConstraint("client_id", "parking_id"),)

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    parking_id = db.Column(db.Integer, db.ForeignKey("parking.id"), nullable=False)
    time_in = db.Column(db.DateTime, nullable=True)
    time_out = db.Column(db.DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"Клиент {self.client_id} место {self.parking_id}"

    def to_json(self) -> dict:
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
