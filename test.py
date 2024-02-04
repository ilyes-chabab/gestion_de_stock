
import pygame
import sys
import mysql.connector

mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='store',
)

cursor =mydb.cursor()

def readProduct():
    cursor.execute("SELECT product.name , product.description, product.price , product.quantity , category.name FROM product inner join category on product.id_category=category.name")

    product_repertory= cursor.fetchall()

    for i in product_repertory:
        print(i[0],i[1],i[2],i[3],i[4])
def writeProducts(id_product):
    cursor.execute(f"SELECT product.name , product.description, product.price , product.quantity , category.name FROM product inner join category on product.id_category=category.id")
    product_repertory= cursor.fetchall()
    listOfProduct=[]
    y=300
    listOfProduct.append(product_repertory)
    message(30,f"{listOfProduct[0][id_product][0]} ",(120,y,0,0,),(0,0,0))  
    message(30,f"{listOfProduct[0][id_product][1]} ",(290,y,0,0,),(0,0,0))
    message(30,f"{listOfProduct[0][id_product][2]} ",(850,y,0,0,),(0,0,0))
    message(30,f"{listOfProduct[0][id_product][3]} ",(950,y,0,0,),(0,0,0))
    message(40,f"{listOfProduct[0][id_product][4]} ",(550,120,0,0,),(0,0,0))

def countProduct():
    cursor.execute(f"SELECT COUNT(*) FROM product")
    countOfProduct= cursor.fetchall()
    return countOfProduct 

def addProduct(self):
    product_list=[]
    name=input("nom : ")
    description=input("description : ")
    price=int(input("prix : "))
    quantity=input("quantité : ")
    id_category=input("nom de la catégorie(légume , fruit , boisson ou dessert) : ")           
    if id_category == 'légumes' or 'légume' or 'legumes' or 'legume' or 1:
        id_category=1
    elif id_category == 'fruits' or 'fruit' or 2:
        id_category=2
    elif id_category == 'boissons' or 'boisson' or 3:
        id_category=3
    elif id_category == 'dessert' or 'desserts' or 4:
        id_category=4
    product_list=[(name , description,price,quantity,id_category)] 
    print(product_list)
    for product in product_list:
        print(product)
        cursor.execute("INSERT INTO test (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",product)
    mydb.commit()
    mydb.close()

def removeProduct():
    readProduct()
    productToRemove= int(input("Vous voulez supprimer le produit numéro : "))
    cursor.execute(f'delete from test where id={productToRemove}')
    readProduct()
    mydb.commit()
    mydb.close()

def updateProduct(self):
    readProduct()    
    productToUpdate= int(input("Vous voulez modifier le produit numéro : "))
    new_name = input("Nouveau nom : ")
    new_description = input("Nouvelle description : ")
    new_price = int(input("Nouveau prix : "))
    new_quantity = int(input("Nouvelle quantité : "))
    new_category = input("Nouvelle catégorie : ")
    update_data = (new_name,new_description, new_price, new_quantity, new_category)
    cursor.execute(f"UPDATE test SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s WHERE id = {productToUpdate}", update_data)
    mydb.commit()
    mydb.close()

id= 0
cursor.execute(f"select id from product")
var_id= cursor.fetchall()
listOfId=[var_id]
listOfId.append(var_id)
print(id,listOfId[0][id][0])



readProduct()
print(countProduct())
# shop=Store()  
# product=Product()
# shop.writeProducts(2)
# # # product.addProduct()  
# # product.updateProduct() 


pygame.init()
screen=pygame.display.set_mode((1250,600))
def message(size,message,message_rectangle,color):
    font=pygame.font.SysFont("arial",size)
    message = font.render(message,False,color)
    screen.blit(message,message_rectangle)
var_product=11

running = True

while running:
    screen.fill((255,255,255))
    
    pygame.draw.rect(screen , (0, 0, 0),(100,100,1000,300),3)
    pygame.draw.rect(screen , (0, 0, 0),(100,100,1000,100),3)
    pygame.draw.line(screen , (0, 0, 0),(100,270),(1100,270),3)
    pygame.draw.line(screen , (0, 0, 0),(290,200),(290,400),3)
    pygame.draw.line(screen , (0, 0, 0),(790,200),(790,400),3)
    pygame.draw.line(screen , (0, 0, 0),(940,200),(940,400),3)
    message(45,'Category :',(300,120,0,0,),(0,0,0))
    message(45,'name                    description                        price        stock     ',(120,220,0,0,),(0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            var_product+=1
    if var_product== -1:
        var_product=countProduct()[0][0]
    elif var_product==countProduct()[0][0]:
        var_product=0
    else :
        writeProducts(var_product)
    pygame.display.flip()  

   
        
        