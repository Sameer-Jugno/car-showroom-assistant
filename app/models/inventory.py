from sqlalchemy import Column, Integer, String

from app.db.postgres import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    selling_price = Column(Integer, nullable=False)
    km_driven = Column(Integer, nullable=False)
    fuel = Column(String, nullable=False)
    seller_type = Column(String, nullable=False)
    transmission = Column(String, nullable=False)
    owner = Column(String, nullable=False)