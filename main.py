import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from customer import custome_menu
from admin import admin_page
from contact import ContactUsApp
from home import Home
class cafeapp:
    def __init__(self, root): 
        root =root
        self.frame = ctk.CTkFrame(root, height=550, width=1200, fg_color="snow")
        self.frame.place(x=0,y=60)
        self.page = Home(self.frame)
        self.c = custome_menu(self.frame)
        self.admin = admin_page(self.frame)
        self.phone = ContactUsApp(self.frame)
        self.topbar()
        self.page.homepage()
    



    def topbar(self):
        self.topbar = ctk.CTkFrame(root, width=1200, height=65, fg_color="dark slate gray")
        self.topbar.pack()


        # self.switch = ctk.CTkSwitch(self.topbar, text="Dark", font=("Helvetica", 12,"bold"), command=self.toggle_theme, text_color="snow")
        # self.switch.place(x=1120,y=15)
        # created top menu bar and labels 

        self.edit_label = ctk.CTkLabel(self.topbar,text="Add/Remove",font=("Helvetica",14,"bold"),text_color="snow",cursor="hand2")
        self.edit_label.place_forget()

        self.home_label = ctk.CTkLabel(self.topbar,text="Home",font=("Helvetica",14,"bold"),text_color="snow",cursor="hand2")
        self.home_label.place(x=600,y=15)
        self.home_label.bind("<Button-1>", self.back_to_home)

        self.menu_label = ctk.CTkLabel(self.topbar,text="Menu",font=("Helvetica",14,"bold"),text_color="snow",cursor="hand2")
        self.menu_label.place(x=700,y=15)
        self.menu_label.bind("<Button-1>", self.Menu)

        self.contact_label = ctk.CTkLabel(self.topbar,text="contact",font=("Helvetica",14,"bold"),text_color="snow",cursor="hand2")
        self.contact_label.place(x=800,y=15)
        self.contact_label.bind("<Button-1>", self.contact)


        # make a admin profile icon 
        self.image_path = "C:\\Users\\jatin\\Desktop\\cafe managment\\images\\admin icon.png"
        self.image = Image.open(self.image_path)
        self.ctk_image = ctk.CTkImage(light_image=self.image, dark_image=self.image, size=(40, 40)) # Adjust size as needed

        self.admin_button = ctk.CTkButton(master=self.topbar,image=self.ctk_image,text="",hover_color="slate gray", height=30,width=30, fg_color="dark slate gray",command=self.login)
        self.admin_button.place(x= 900,y=6)
    

        # creating the cart button 
        self.cart_image_path = "C:\\Users\\jatin\\Desktop\\cafe managment\\images\\cart2.png"
        self.cart_image = Image.open(self.cart_image_path)
        self.cart_ctk_image = ctk.CTkImage(light_image=self.cart_image, dark_image=self.cart_image, size=(40, 40)) # Adjust size as needed

        self.cart_button = ctk.CTkButton(master=self.topbar,image=self.cart_ctk_image,text="",hover_color="slate gray", height=30,width=30, fg_color="dark slate gray",command=self.cart_section)
        self.cart_button.place(x= 970,y=6)

        

        # # Create and pack the switch
        # self.theme_label = ctk.CTkLabel(self.topbar,text="Theme : ",font=("Helvetica",14,"bold"),text_color="snow")
        # self.theme_label.place(x=1050,y=13)
        
      


    def back_to_home(self,event):
        for widget in self.frame.winfo_children():
            widget.destroy()
       
        self.page.homepage()

    def Menu(self,event):
        for widget in self.frame.winfo_children():
            widget.destroy()
       
        self.c.catergary()
    def contact(self,event):
        for widget in self.frame.winfo_children():
            widget.destroy()
       
        self.phone.contact_us()
        

    def login(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.admin.admin_login()
        self.check_value()
    def check_value(self):
        if self.admin.check_return:
            for widget in self.frame.winfo_children():
             widget.destroy()
            self.edit_label.place(x=460,y=15)
            self.edit_label.bind("<Button-1>", self.admin.add_remove_items)
          
            
        else:
            self.frame.after(1000, self.check_value)
            
    
    def cart_section(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.c.cart()


    def toggle_theme(self):
        if self.switch.get():
            ctk.set_appearance_mode("Dark")
            self.switch.configure(text="Light")
        else:
            ctk.set_appearance_mode("Light")
            self.switch.configure(text="Dark")



ctk.set_appearance_mode("light")  # Automatically uses system theme)
root = ctk.CTk()
root.title("Brew haven cafe")
root.geometry("1200x590")
cafeapp(root)
root.mainloop()
