import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image
from customer import custome_menu
from tkinter import filedialog



class admin_page:
    def __init__(self, frame):
        self.myroot = frame
        self.c = custome_menu(frame)
        self.check_return = ""
        self.new_category = False
        


    def admin_login(self):
        self.login_frame = ctk.CTkFrame(self.myroot,height=500,width=400, fg_color="snow",border_width=2)
        self.login_frame.place(x=380,y=10)
        # login_frame.grid_propagate(False)
        image_path = "C:\\Users\\jatin\\Desktop\\cafe managment\\images\\admin icon.png"
        image = Image.open(image_path)
        ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(140, 140))

        head_img = ctk.CTkLabel(self.login_frame, image=ctk_image, text="")
        head_img.place(x=130,y=10)

        username_label = ctk.CTkLabel(self.login_frame,height=10,width=20,text="Username :", font=("arial",25,"bold"))
        username_label.place(x=20,y=170)

        user_input = ctk.CTkEntry(self.login_frame,height=40,width=350, border_width=1,font=("Arial Greek",20))
        user_input.place(x=20,y=200)

        password_label = ctk.CTkLabel(self.login_frame,height=10,width=20,text="Password :", font=("arial",25,"bold"))
        password_label.place(x=20,y=270)

        password_input = ctk.CTkEntry(self.login_frame,height=40,width=350, border_width=1,font=("Arial Greek",20))
        password_input.place(x=20,y=300)

        self.login_btn = ctk.CTkButton(self.login_frame,height=10,width=30,text="Login", font=("arial",25,"bold"),fg_color="green",corner_radius=5,hover_color="slate gray",command=lambda:self.check(user_input.get(),password_input.get()))
        self.login_btn.place(x=150,y=420)
    def check(self,username,password):
        with open("user_info.json","r") as file:
            user_info = json.load(file)
            self.user_data = user_info["admin"]
        if self.user_data[0] == username and self.user_data[1]==password:
            tk.messagebox.showinfo("Login","Logged in Successfully.")
            self.check_return =True
            

        else:
            tk.messagebox.showerror("Login","Your username or password is incorrect! ")
            self.check_return=False
    def add_remove_items(self,event):
        for widget in self.myroot.winfo_children():
             widget.destroy()
        self.add_remove_frame = ctk.CTkFrame(self.myroot,height=460,width=400, fg_color="snow",border_width=2)
        self.add_remove_frame.place(x=380,y=10)
        self.category_check = True
        # self.newroot = newroot
        topframe = ctk.CTkFrame(self.add_remove_frame,width=400,height=60, fg_color="slate gray")
        topframe.place(x=0,y=0)
        self.bottomframe= ctk.CTkFrame(self.add_remove_frame, height=400,width=400,fg_color="snow", border_width=2)
        self.bottomframe.place(x=0,y=60)
        
        add_label = ctk.CTkButton(topframe,width=200,height=60,text="Add", fg_color="slate gray",text_color="snow",hover_color="gray",border_width=1,command=self.add_items)
        add_label.grid(row=0,column=0)

        remove_label = ctk.CTkButton(topframe,width=200,height=60,text="Remove",fg_color="slate gray", text_color="snow",hover_color="gray",border_width=1,command=self.remove_items)
        remove_label.grid(row=0,column=1)


    # This methods for removing items
    def remove_items(self):
        
        for widget in self.bottomframe.winfo_children():
             widget.destroy()
        with open("cafe_items.json","r")as file:
            self.cafeitems = json.load(file)
        self.cafe_items = self.cafeitems["cafe menu"]
        values = list(self.cafe_items.keys())
        category_label = ctk.CTkLabel(self.bottomframe, font=("arial",15,"bold"),text="Select Category :" ,text_color="black")
        category_label.place(x=30,y=30)
        self.remove_category_combobox = ctk.CTkComboBox(self.bottomframe, width=200 ,values=values,fg_color="snow",text_color="black", command=self.selected_item)
        self.remove_category_combobox.place(x=170,y=30)
        self.remove_items_label = ctk.CTkLabel(self.bottomframe, font=("arial",15,"bold"),text="Select Item:" ,text_color="black")
        self.remove_items_label.place(x=30,y=100)
        self.remove_items_combobox = ctk.CTkComboBox(self.bottomframe, width=200 , values=["select item"],fg_color="snow",text_color="black")
        self.remove_items_combobox.place(x=170,y=100)
        Proceed_btn = ctk.CTkButton(self.bottomframe,font=("arial",15,"bold"), text="Proceed", text_color="black",fg_color="green",hover_color="gray",border_width=1, corner_radius=5, command=self.selected_product)
        Proceed_btn.place(x=110,y = 280)


    def selected_item(self,item):
        self.item =item
        self.category_item = []
        for  key  in self.cafe_items.keys():
                if key ==item:
                      mylist = self.cafe_items[key]
                    #   print(mylist)
                      for product in mylist:
                           self.category_item.append(product['name'])
        self.remove_items_combobox.configure(values=self.category_item)

    def selected_product(self):
        selected_category = self.remove_category_combobox.get()
        selected_item = self.remove_items_combobox.get()
        # print(selected_item)

        for key, value in self.cafe_items.items():
              if key ==selected_category and selected_item =="":
                        del self.cafeitems["cafe menu"][key]
                        tk.messagebox.showinfo("file updated",f"{key} are removed successfully.")
                        break
              elif key==selected_category:    
                   for values in value:
                        if values['name']==selected_item:
                            self.cafeitems['cafe menu'][key].remove(values)
                            tk.messagebox.showinfo("file updated",f"{values['name']} is removed successfully.")
                            break

        
        with open("cafe_items.json", "w") as json_file:
            json.dump(self.cafeitems, json_file)
            print("file updated")
        self.category_item =[]

    #these methods are for adding items 
    def add_items(self):
        for widget in self.bottomframe.winfo_children():
             widget.destroy()
        with open("cafe_items.json","r")as file:
            self.addcafeitems = json.load(file)
        self.addcafe_items = self.addcafeitems["cafe menu"]
        self.add_category_label = ctk.CTkLabel(self.bottomframe, font=("arial",15,"bold"),text="Select Category :" ,text_color="black")
        self.add_category_label.place(x=30,y=20)
        new_category_btn = ctk.CTkButton(self.bottomframe, width=15, height=15, font=("arial",17,"bold"),text="+" ,text_color="black" ,fg_color="snow", border_width=1,command=self.choice_new_or_old)
        new_category_btn.place(x=330,y=22)
        values = list(self.addcafe_items.keys())
        self.add_category_combobox = ctk.CTkComboBox(self.bottomframe, width=150 ,values=values,fg_color="snow",text_color="black")
        self.add_category_combobox.place(x=170,y=20)
        self.add_category_entrybox = ctk.CTkEntry(self.bottomframe, width=150,fg_color="snow",text_color="black")
        self.add_category_entrybox.place_forget()

        item_label = ctk.CTkLabel(self.bottomframe, font=("arial",15,"bold"),text="Item Name :" ,text_color="black")
        item_label.place(x=30,y=80)
        self.add_item_entrybox = ctk.CTkEntry(self.bottomframe, width=150 ,fg_color="snow",text_color="black")
        self.add_item_entrybox.place(x=170,y=80)

        item_price = ctk.CTkLabel(self.bottomframe, font=("arial",15,"bold"),text="Item Price :" ,text_color="black")
        item_price.place(x=30,y=140)
        self.add_price_entrybox = ctk.CTkEntry(self.bottomframe, width=150 ,fg_color="snow",text_color="black")
        self.add_price_entrybox.place(x=170,y=140)

        image_label = ctk.CTkLabel(self.bottomframe, font=("arial",15,"bold"),text="Select Image :" ,text_color="black")
        image_label.place(x=30,y=200)
        image_btn = ctk.CTkButton(self.bottomframe, width=150, font=("arial",15,"bold"),text="Choose file" ,text_color="black" ,fg_color="snow", border_width=2, command=self.get_image)
        image_btn.place(x=170,y=200)

        Proceed_btn = ctk.CTkButton(self.bottomframe,font=("arial",15,"bold"), text="Proceed", text_color="black",fg_color="green",hover_color="gray",border_width=1, corner_radius=5, command=self.add_selected_items)
        Proceed_btn.place(x=110,y = 280)
    def choice_new_or_old(self):
        self.new_category = True
        self.add_category_combobox.place_forget()
        self.add_category_entrybox.place(x=170,y=20)
        self.add_category_label.configure(text="Category Name :")
    def get_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path: 
            self.file_location = file_path  
            print(file_path) # Keep a reference to avoid garbage collection
    def add_selected_items(self):
        item = self.add_item_entrybox.get()
        price = float(self.add_price_entrybox.get())
        if self.new_category:  
             category = self.add_category_entrybox.get()
             for cafe_items in self.addcafeitems.values():
                  cafe_items[category] = {'name':item,'price':price,'image_location':self.file_location}
                  break
        else:
            category = self.add_category_combobox.get()
            for cafe_items in self.addcafeitems.values():
                for key in cafe_items:
                    if key == category:
                        data = {'name':item,"price":price,"image_location":self.file_location}
                        self.addcafeitems["cafe menu"][key].append(data)
                        break
    
        with open("cafe_items.json", "w") as json_file:
            json.dump(self.addcafeitems, json_file)
            print("file updated")       

