
import pygame
import sys
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
        self.cursor.execute("SELECT * FROM product")
        self.product_repertory= self.cursor.fetchall()

    def readProduct(self):
        self.cursor.execute("SELECT * FROM product")
        self.product_repertory= self.cursor.fetchall()
        self.listOfProduct=[]
        for i in self.product_repertory:
            print(i)

    def writeProducts(self,id_product):
        self.cursor.execute(f"SELECT product.name , product.description, product.price , product.quantity , category.name FROM product inner join category on product.id_category=category.id")
        product_repertory= self.cursor.fetchall()
        listOfProduct=[]
        y=300
        listOfProduct.append(product_repertory)
        self.message(30,f"{listOfProduct[0][id_product][0]} ",(120,y,0,0,),(0,0,0))  
        self.message(30,f"{listOfProduct[0][id_product][1]} ",(290,y,0,0,),(0,0,0))
        self.message(30,f"{listOfProduct[0][id_product][2]}€ ",(850,y,0,0,),(0,0,0))
        self.message(30,f"{listOfProduct[0][id_product][3]} ",(950,y,0,0,),(0,0,0))
        self.message(40,f"{listOfProduct[0][id_product][4]} ",(550,120,0,0,),(0,0,0))

    def countProduct(self):
        self.cursor.execute(f"SELECT COUNT(*) FROM product")
        countOfProduct= self.cursor.fetchall()
        return countOfProduct[0][0]
    
class Product(Store):
    def __init__(self) -> None:
        super().__init__()

    def addProduct(self):
        product_list=[]
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

class Graph(Store):
    def __init__(self) -> None:     
        super().__init__()
        pygame.init()
        self.screen=pygame.display.set_mode((1250,600))
        self.running = True
        self.var_product=0
        print(self.var_product)
        print(self.countProduct())
        self.product_nega=False
        self.product_posi=False

    def message(self,size,message,message_rectangle,color):
        font=pygame.font.SysFont("arial",size)
        message = font.render(message,False,color)
        self.screen.blit(message,message_rectangle)
    
    def draw_button(self,rect, color, text, text_color):
        pygame.draw.rect(self.screen, color, rect)
        
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        
        self.screen.blit(text_surface, text_rect)

    
    def loop(self):

        while self.running :
            self.screen.fill((255,255,255))
            
            pygame.draw.rect(self.screen , (0, 0, 0),(100,100,1000,300),3)
            pygame.draw.rect(self.screen , (0, 0, 0),(100,100,1000,100),3)
            pygame.draw.line(self.screen , (0, 0, 0),(100,270),(1100,270),3)
            pygame.draw.line(self.screen , (0, 0, 0),(290,200),(290,400),3)
            pygame.draw.line(self.screen , (0, 0, 0),(790,200),(790,400),3)
            pygame.draw.line(self.screen , (0, 0, 0),(940,200),(940,400),3)
            self.message(45,'Category :',(300,120,0,0,),(0,0,0))
            self.message(45,'name                    description                        price        stock     ',(120,220,0,0,),(0,0,0))
            button_prev_rect=pygame.Rect(0,300,100,50)
            self.draw_button(button_prev_rect,(0,0,0),f"prev.",(255,255,255))
            button_next_rect=pygame.Rect(1120,300,100,50)
            self.draw_button(button_next_rect,(0,0,0),f"next",(255,255,255))
            button_add_rect=pygame.Rect(100,400,300,50)
            self.draw_button(button_add_rect,(0,0,0),f"Add",(255,255,255))
            button_remove_rect=pygame.Rect(450,400,300,50)
            self.draw_button(button_remove_rect,(0,0,0),f"remove",(255,255,255))
            button_edit_rect=pygame.Rect(800,400,300,50)
            self.draw_button(button_edit_rect,(0,0,0),f"edit",(255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_next_rect.collidepoint(event.pos):
                        self.var_product += 1
                        if self.var_product == self.countProduct():
                            self.var_product = 0
                    elif button_prev_rect.collidepoint(event.pos):
                        if self.var_product == 0:
                            self.var_product = self.countProduct() - 1
                        else:
                            self.var_product -= 1
                    elif button_add_rect.collidepoint(event.pos):
                        product.addProduct()
                    elif button_remove_rect.collidepoint(event.pos):
                        product.removeProduct()
                    elif button_edit_rect.collidepoint(event.pos):
                        product.updateProduct()
            self.writeProducts(self.var_product)
            
            pygame.display.flip()  

shop = Store()
product = Product()
graphique = Graph()
graphique.loop()


   
        
        