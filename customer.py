
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image


class custome_menu(ctk.CTk):
    def __init__(self,frame):
        self.cart_items = []
        self.myroot = frame
      


    def catergary(self):
        frame = ctk.CTkScrollableFrame(self.myroot,height= 545,width=220, fg_color="snow",scrollbar_button_color="dark slate gray")
        frame.place(x=0,y=1)

        self.catergary_buttons = {}
        with open("C:\\Users\\jatin\\Desktop\\cafe managment\\cafe_items.json","r") as file:
            data  = json.load(file)
        self.cafe_items = data["cafe menu"]
        

        for row in range(0, len(self.cafe_items.keys())):
            category_name = list(self.cafe_items.keys())[row]
            btn = ctk.CTkButton(master=frame,height=49,width=217,  hover_color="slate gray",fg_color="dark slate gray",font=("Book Antiqua", 17, "bold"), text=category_name,command=lambda row=row :  self.selected_category(row))
            btn.grid(row=row, column=0, padx=1, pady=5)
            self.catergary_buttons[row] = btn



        self.main_frame = ctk.CTkScrollableFrame(self.myroot,height=520,width=1000,fg_color="snow")
        self.main_frame.place(x=250,y=0)

       

    def selected_category(self, row):
        for btn in self.catergary_buttons.values():
            btn.configure(fg_color="dark slate gray",text_color="snow", hover_color="slate gray",border_width=0)
        clicked_btn = self.catergary_buttons[row]
        clicked_btn.configure(fg_color="snow", text_color="black", hover_color="snow",border_width=2)
        self.list_of_items(clicked_btn)


        

    def list_of_items(self,clicked_btn):
        text = clicked_btn.cget("text")
        for check in self.cafe_items.keys():
            if check == text:
                selected_item = self.cafe_items[check]
        
        row = 0
        col = 0
        for item in selected_item:
            # print(key[0])
                box = ctk.CTkFrame(self.main_frame,height=225,width=203,border_width=2,fg_color="snow",corner_radius=10)
                box.grid(row=row, column=col, padx=10, pady=10,sticky=ctk.W)
                box.grid_propagate(False)
                image_path = item['image_location']
                image = Image.open(image_path)
                ctk_image = ctk.CTkImage(dark_image=image, size=(190, 120))
                image_label = ctk.CTkLabel(box,image=ctk_image,text="")
                image_label.grid(row=1,column=0,pady=6)
                name_label = ctk.CTkLabel(box,text=item['name'], font=("Georgia", 13,"bold"),text_color="black")
                name_label.grid(row=2,column=0,padx=10)
                price_label = ctk.CTkLabel(box,text=f"${item['price']}", font=("Georgia", 13,"bold"),text_color="black")
                price_label.grid(row=3,column=0,padx=10)
                cart_button = ctk.CTkButton(box,text="Add To Cart", font=("Georgia", 10,"bold"),text_color="black",width=195, command= lambda name = item['name'], price = item['price']:self.update(name,price))
                cart_button.grid(row=4,column=0,padx=3)
                
                if col<3:
                    col+=1
                else:
                    row+=1
                    col=0
    def update(self, name ,price):
            bool = True
            price = float(price)
            # print(self.index)
            for item in self.cart_items:
                if item['name'] == name:
                    item['quantity'] += 1 
                    price = item['quantity']*price
                    item['price'] = price
                    bool=False
                    break
                else:
                    pass
            
            if bool:
                data ={'name':name,'quantity':1, 'price':price}
                self.cart_items.append(data)
            print(self.cart_items)

    def total(self):
        total_amount =0
        for  product in self.cart_items:
                total_amount+=product['price']
            
        return total_amount
    def cart(self):
        total_amount =self.total()
        shopping_label = ctk.CTkLabel(self.myroot, width=30, text="Shopping Cart: " ,font=("Adobe Heiti Std R", 20,"bold"))
        shopping_label.place(x=200,y=15)

        product_label =  ctk.CTkLabel(self.myroot, width=20, text="Product" ,font=("Adobe Heiti Std R", 15,"italic"))
        product_label.place(x=480,y=45)
        quantity_label =  ctk.CTkLabel(self.myroot, width=20, text="Quantity" ,font=("Adobe Heiti Std R", 15,"italic"))
        quantity_label.place(x=570,y=45)
        price_label =  ctk.CTkLabel(self.myroot, width=20, text="Price" ,font=("Adobe Heiti Std R", 15,"italic"))
        price_label.place(x=650,y=45)
        
        cart_frame = ctk.CTkScrollableFrame(self.myroot,height=350,width=300,fg_color="snow",border_width=1)
        cart_frame.place(x=450,y=70)
        row =0
        for key in self.cart_items:

            product_name =  tk.Label(cart_frame, width=14, text=f"{key['name']}" ,font=("Adobe Heiti Std R", 13,"italic"))
            product_name.grid(row=row,column=0,padx=5,pady=6)
            quantity =  tk.Label(cart_frame, width=5, text=key['quantity'] ,font=("Adobe Heiti Std R", 13,"italic"))
            quantity.grid(row=row,column=1,padx=5,pady=6)
            price =  tk.Label(cart_frame, width=5, text=f"${key['price']}" ,font=("Adobe Heiti Std R", 13,"italic"))
            price.grid(row=row,column=2,padx=10,pady=6)
            remove_btn =ctk.CTkButton(cart_frame,width=10,height=10,text="Remove", fg_color="slate gray", command=lambda name = product_name["text"]:self.del_cart_item(name))
            remove_btn.grid(row=row,column=3,pady=6)
            row+=1
        total_label= ctk.CTkLabel(self.myroot, text="Total Amount : " ,font=("Adobe Heiti Std R", 20,"italic"))
        total_label.place(x=470,y=400)

        total_price= ctk.CTkLabel(self.myroot, text=f"${total_amount}" ,font=("Adobe Heiti Std R", 15,"italic"))
        total_price.place(x=670,y=400)

        place_order_btn  = ctk.CTkButton(self.myroot,height=10,width=30, text= "Place Order", fg_color="green", font=("Tekton Pro",20,"bold"),corner_radius=5,hover_color="slate gray",command=self.order_finished)
        place_order_btn.place(x=540,y=440)

    
    def del_cart_item(self,name):
        for product in self.cart_items:
            if product['name']==name:
                if product['quantity']==1:
                    self.cart_items.remove(product)
                    self.cart()        
                    break
                else:
                    product['quantity'] = product['quantity']-1
                    for key,item in self.cafe_items.items():
                       for value in item:
                           if value['name'] ==  name:
                                product['price'] = product['price']-value['price']
                                break
                    self.cart()
                    break     


    def order_finished(self):

        if len(self.cart_items)==0:
            tk.messagebox.showinfo("Empty","Your cart is empty! \n Please add items.")
        else:
            tk.messagebox.showinfo("order placed", "Thank you for placing order")
            self.cart_items = {}
            self.cart()

    
        