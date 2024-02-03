import mysql.connector
from store import Store

class Product(Store):
    def __init__(self) -> None:
        super().__init__()

    def addProduct(self):
        product_list=[]
        if True:
            self.name=input("nom : ")
            self.description=input("description : ")
            self.price=int(input("prix : "))
            self.quantity=input("quantité : ")
            self.id_category=input("nom de la catégorie(légume , fruit , boisson ou dessert) : ")           
            if self.id_category == 'légumes' or 'légume' or 'legumes' or 'legume' or 1:
                self.id_category=1
            elif self.id_category == 'fruits' or 'fruit' or 2:
                self.id_category=2
            elif self.id_category == 'boissons' or 'boisson' or 3:
                self.id_category=3
            elif self.id_category == 'dessert' or 'desserts' or 4:
                self.id_category=4
            product_list=[(self.name , self.description,self.price,self.quantity,self.id_category)] 
            print(product_list)
        for product in product_list:
            print(product)
            self.cursor.execute("INSERT INTO test (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",product)
        self.mydb.commit()
        self.mydb.close()

    def removeProduct(self):
        self.readProduct()
        self.productToRemove= int(input("Vous voulez supprimer le produit numéro : "))
        self.cursor.execute(f'delete from test where id={self.productToRemove}')
        self.readProduct()
        self.mydb.commit()
        self.mydb.close()

    def updateProduct(self):
        self.readProduct()    
        self.productToUpdate= int(input("Vous voulez modifier le produit numéro : "))
        self.new_name = input("Nouveau nom : ")
        self.new_description = input("Nouvelle description : ")
        self.new_price = int(input("Nouveau prix : "))
        self.new_quantity = int(input("Nouvelle quantité : "))
        self.new_category = input("Nouvelle catégorie : ")
        update_data = (self.new_name,self.new_description, self.new_price, self.new_quantity, self.new_category)
        self.cursor.execute(f"UPDATE test SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s WHERE id = {self.productToUpdate}", update_data)
        self.mydb.commit()
        self.mydb.close()



