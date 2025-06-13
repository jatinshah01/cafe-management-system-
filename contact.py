import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import json
from PIL import Image

class ContactUsApp(ctk.CTk):
    def __init__(self,frame):
        self.frame = frame

    def  contact_us(self):
        # Create main frame
        self.contact_frame = ctk.CTkFrame(self.frame, height=500, width=400, fg_color="snow", border_width=2)
        self.contact_frame.place(x=380, y=10)

        # Load and place the image
        image_path = "C:\\Users\\jatin\\Desktop\\cafe managment\\images\\contact_icon.png"  # Update the path accordingly
        image = Image.open(image_path)
        ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(80, 80))
        head_img = ctk.CTkLabel(self.contact_frame, image=ctk_image, text="")
        head_img.place(x=150, y=10)

        # Name label and entry
        name_label = ctk.CTkLabel(self.contact_frame, text="Name:", font=("Arial", 20, "bold"))
        name_label.place(x=20, y=100)
        self.name_entry = ctk.CTkEntry(self.contact_frame, width=350, height=40, font=("Arial", 16))
        self.name_entry.place(x=20, y=130)

        # Email label and entry
        email_label = ctk.CTkLabel(self.contact_frame, text="Email:", font=("Arial", 20, "bold"))
        email_label.place(x=20, y=180)
        self.email_entry = ctk.CTkEntry(self.contact_frame, width=350, height=40, font=("Arial", 16))
        self.email_entry.place(x=20, y=210)

        # Phone label and entry
        phone_label = ctk.CTkLabel(self.contact_frame, text="Phone:", font=("Arial", 20, "bold"))
        phone_label.place(x=20, y=260)
        self.phone_entry = ctk.CTkEntry(self.contact_frame, width=350, height=40, font=("Arial", 16))
        self.phone_entry.place(x=20, y=290)

        # Message label and textbox
        message_label = ctk.CTkLabel(self.contact_frame, text="Message:", font=("Arial", 20, "bold"))
        message_label.place(x=20, y=340)
        self.message_textbox = ctk.CTkTextbox(self.contact_frame, width=350, height=80, font=("Arial", 14),border_width=2,corner_radius=5)
        self.message_textbox.place(x=20, y=370)

        # Submit button
        submit_button = ctk.CTkButton(self.contact_frame, text="Submit", font=("Arial", 20, "bold"),fg_color="green", hover_color="slate gray", command=self.submit_form)
        submit_button.place(x=120, y=460)
    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        message = self.message_textbox.get("0.0", "end").strip()

        # Display the submitted information
        info = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        messagebox.showinfo("Submitted Information", info)

