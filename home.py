import customtkinter as ctk
from PIL import Image
import tkinter as tk

class Home(ctk.CTk):
    def __init__(self, root):
        self.frame  =root

    def homepage(self):
        # Create the home frame
        self.home_frame = ctk.CTkFrame(self.frame, height=545, width=1200, fg_color="snow", border_width=2)
        self.home_frame.place(x=0, y=0)

        # Load and place the café logo
        image_path = "C:\\Users\\jatin\\Desktop\\cafe managment\\images\\logo dark.png"  # Update with your logo path
        image = Image.open(image_path)
        ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(440, 440))
        logo_label = ctk.CTkLabel(self.home_frame, image=ctk_image, text="")
        logo_label.place(x=100, y=10)

        # Welcome message
        welcome_label = ctk.CTkLabel(self.home_frame, text="Welcome to Café Delight!", font=("Arial", 34, "bold"), text_color="black")
        welcome_label.place(x=600, y=170)

        # Additional description
        self.description = (
            "Experience the finest brews and delightful treats."
        )
        self.description_label = ctk.CTkLabel(self.home_frame, width=200, text=self.description, font=("Arial", 26), justify="left", text_color="black")
        self.description_label.place(x=600, y=260)


        self.discover_button = ctk.CTkButton(self.home_frame, text="Discover More", font=("Arial", 18, "bold"), fg_color="dark slate gray", text_color="white", hover_color="slate gray",command=self.update_description)
        self.discover_button.place(x=600, y=320)

    def update_description(self):
        # Update the description text dynamically
        self.description_label.configure(text="Join us for a cozy atmosphere,\nexceptional service, and a menu crafted with love.\nYour perfect coffee moment awaits!")
        self.discover_button.configure(command=self.reset, text="Discover Less")
        self.discover_button.place(x=600, y=370)
    def reset(self):
        self.description_label.configure(text=self.description)
        self.discover_button.configure(command=self.update_description)
        self.discover_button.place(x=600, y=320
            )
