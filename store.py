import mysql.connector

class Store:
    def __init__(self) -> None:
        
        self.mydb= mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='store',
        )

        self.cursor =self.mydb.cursor()

    def readProduct(self):
        self.cursor.execute("SELECT * FROM test")

        self.product_repertory= self.cursor.fetchall()
        self.listOfProduct=[]
        for i in self.product_repertory:
            self.listOfProduct.append(i)
            print(i[0],i[1],i[2],i[3],i[4])
        print(self.listOfProduct[1][1])
shop=Store()
shop.readProduct()