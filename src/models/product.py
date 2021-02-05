from sqlalchemy import String, DECIMAL, Column
from sqlalchemy.orm import validates

from src.models.base_model import BaseModel


class Product(BaseModel):
    __tablename__="PRODUCT_GRUPO_5"
    name = Column(String(length=50), nullable=False)
    description = Column(String(length=500), nullable=False)
    price = Column(DECIMAL, nullable=False)

    def __init__(self, name: str, description: str, price: float) -> None:
        self.name = name
        self.description = description
        self.price = price

    @validates("price")
    def validates_price(self, key: str, price: float) -> str:

        if not isinstance(price, float):
            raise TypeError("Price must be float.")
        if price <= 0:
            raise ValueError("Price must be greater than 0."   ) 
        
        return price

    @validates("name")
    def validates_name(self, key, name: str) -> str:
        
        if not isinstance(name, str):
            raise TypeError("Name must be str.")
        if len(name) > 50:
            raise ValueError("Name length must not be greater than 50")
        if not name.strip():
            raise ValueError("Name must not be empty.")

        return name

    @validates("description")
    def validates_description(self, key, description: str) -> str:
        if not isinstance(description, str):
            raise TypeError("Description must be str.")
        if len(description) > 200:
            raise ValueError("Description length must not be greater than 200")
        if not description.strip():
            raise ValueError("Description must not be empty.")

        return description
