from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=True)
    price = db.Column(db.Float(precision=2), unique=False, nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=True)
    store = db.relationship("StoreModel", back_populates="items")