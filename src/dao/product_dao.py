import sys
sys.path.append(".")
from src.models.product import Product
from src.dao.base_dao import BaseDao

class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)

