
import pygame
import sys
import mysql.connector
import time

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
    
    def getProduct(self,id):
        self.cursor.execute(f"select id from product")
        var_id= self.cursor.fetchall()
        self.listOfId=[var_id]
        self.listOfId.append(var_id)
        print(self.listOfId[0][id][0])
        return self.listOfId[0][id][0]
        
    def addProduct(self,name,description,price,quantity,id_category):
        product_list=[]         
        if id_category.lower() == 'légumes' or 'légume' or 'legumes' or 'legume' or "1":
            id_category=1
        elif id_category.lower() == 'fruits' or 'fruit' or "2":
            id_category=2
        elif id_category.lower() == 'boissons' or 'boisson' or "3":
            id_category=3
        elif id_category.lower() == 'dessert' or 'desserts' or 'déssert' or 'désserts' or "4":
            id_category=4
        product_list=[(name , description,price,quantity,id_category)] 
        print(product_list)
        for product in product_list:
            print(product)
            self.cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",product)
        self.mydb.commit()
        self.mydb.close()

    def removeProduct(self,idToRemove):
        self.readProduct()
        self.cursor.execute(f'delete from product where id={idToRemove}')
        self.mydb.commit()
        self.mydb.close()

    def updateProduct(self,name,description,price,quantity,id_category,productToUpdate):
        self.readProduct() 
        if id_category.lower() == 'légumes' or 'légume' or 'legumes' or 'legume' or "1":
            id_category=1
        elif id_category.lower() == 'fruits' or 'fruit' or "2":
            id_category=2
        elif id_category.lower() == 'boissons' or 'boisson' or "3":
            id_category=3
        elif id_category.lower() == 'dessert' or 'desserts' or 'déssert' or 'désserts' or "4":
            id_category=4
        update_data = (name , description,price,quantity,id_category)
        self.cursor.execute(f"UPDATE product SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s WHERE id = {productToUpdate}", update_data)
        self.mydb.commit()
        self.mydb.close()
    
    


class Graph(Store):
    def __init__(self) -> None:     
        super().__init__()
        pygame.init()
        self.screen=pygame.display.set_mode((1250,600))
        self.button_prev_rect=pygame.Rect(0,300,100,50)
        self.button_next_rect=pygame.Rect(1120,300,100,50)
        self.button_add_rect=pygame.Rect(100,400,300,50)
        self.button_remove_rect=pygame.Rect(450,400,300,50)
        self.button_edit_rect=pygame.Rect(800,400,300,50)
        self.text_rect=pygame.Rect(200,200,700,100)
        self.running = True
        self.user_text=""
        self.var_product=0
        print(self.var_product)
        print(self.countProduct())
        self.product_nega=False
        self.product_posi=False
        self.input_active=False

        self.name_text=""
        self.description_text=""
        self.price_text=0
        self.quantity_text=0
        self.id_category_text=""

        self.name=False
        self.description=False
        self.price=False
        self.quantity=False
        self.id_category=False

        self.add=False
        self.edit=False
        self.input_okay=False

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
            
    def display(self):
        self.screen.fill((255,255,255)) 
        pygame.draw.rect(self.screen , (0, 0, 0),(100,100,1000,300),3)
        pygame.draw.rect(self.screen , (0, 0, 0),(100,100,1000,100),3)
        pygame.draw.line(self.screen , (0, 0, 0),(100,270),(1100,270),3)
        pygame.draw.line(self.screen , (0, 0, 0),(290,200),(290,400),3)
        pygame.draw.line(self.screen , (0, 0, 0),(790,200),(790,400),3)
        pygame.draw.line(self.screen , (0, 0, 0),(940,200),(940,400),3)
        self.message(45,'Category :',(300,120,0,0,),(0,0,0))
        self.message(45,'name                    description                        price        stock     ',(120,220,0,0,),(0,0,0))
        self.draw_button(self.button_prev_rect,(0,0,0),f"prev.",(255,255,255))
        self.draw_button(self.button_next_rect,(0,0,0),f"next",(255,255,255))
        self.draw_button(self.button_add_rect,(0,0,0),f"Add",(255,255,255))
        self.draw_button(self.button_remove_rect,(0,0,0),f"remove",(255,255,255))
        self.draw_button(self.button_edit_rect,(0,0,0),f"edit",(255,255,255))

    
    def loop(self):

        while self.running :
            self.display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_next_rect.collidepoint(event.pos):
                        self.var_product += 1
                        if self.var_product == self.countProduct():
                            self.var_product = 0
                    elif self.button_prev_rect.collidepoint(event.pos):
                        if self.var_product == 0:
                            self.var_product = self.countProduct() - 1
                        else:
                            self.var_product -= 1
                    elif self.button_add_rect.collidepoint(event.pos):
                        self.input_active=True
                        self.name=True
                        self.add=True

                    elif self.button_remove_rect.collidepoint(event.pos):
                        product.removeProduct(product.getProduct(self.var_product))
                        while True:
                            self.message(60,'Produit supprimé avec succés.',(300,400,0,0,),(0,0,0))
                            time.sleep(2)
                    elif self.button_edit_rect.collidepoint(event.pos):
                        self.input_active=True
                        self.name=True
                        self.edit=True
                #ça sert a mettre en place une barre d'input dans l'interface
                if self.input_active:
                    if event.type == pygame.KEYDOWN:   
                        if event.key == pygame.K_RETURN: # lorsqu'il appuiras sur entrée la l'input sera donné a la variable
                            # print(self.user_text)  
                            if self.name:
                                self.name_text= self.user_text
                                self.description = True
                                self.name=False
                                print(self.name_text)
                                print(self.description_text)
                            elif self.description:
                                self.description_text=self.user_text
                                self.price=True
                                self.description=False
                            elif self.price:
                                self.price_text=self.user_text
                                self.quantity=True
                                self.price=False
                            elif self.quantity:
                                self.quantity_text =self.user_text
                                self.id_category=True
                                self.quantity=False
                            elif self.id_category:
                                self.id_category_text=self.user_text
                                self.input_okay=True

                            
                            self.user_text = ''  # Efface le texte après avoir appuyé sur Entrée
                        elif event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]  # Supprime le dernier caractère
                        else:
                            self.user_text += event.unicode  # Ajoute la lettre saisi par l'utilisateur
            
            if self.input_active:
                self.draw_button(self.text_rect,(0,0,0),self.user_text,(255,255,255))
            if self.input_okay:
                if self.add:
                    product.addProduct(self.name_text,self.description_text,self.price_text,self.quantity_text,self.id_category_text)
                    self.add=False
                    self.input_okay=False
                    self.input_active=False
                if self.edit:
                    product.updateProduct(self.name_text,self.description_text,self.price_text,self.quantity_text,self.id_category_text,self.var_product+1)
                    self.edit=False
                    self.input_okay=False
                    self.input_active=False

            self.writeProducts(self.var_product)
            # product.getProduct(self.var_product)
                
            pygame.display.flip()  

shop = Store()
product = Product()
graphique = Graph()
graphique.loop()



   
        
        