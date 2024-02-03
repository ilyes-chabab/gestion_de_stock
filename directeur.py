from store import Store
from product import Product
import mysql.connector

class Directeur:
    def __init__(self) -> None:
        self.store = Store()
        self.product = Product()