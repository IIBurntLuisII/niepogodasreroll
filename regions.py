import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab
import json

class RegionSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Select Screen Regions")
        self.root.geometry("300x440")
        self.root.resizable(False, False)

        self.regions = {}
        self.buttons = {}

        self.instructions = tk.Label(root, text="Select regions for quests and reroll buttons:", font=("Calibri", 12))
        self.instructions.pack(pady=10)

        self.create_selection_button("Select Quest 1 Region", "quest1")
        self.quest1_label = self.create_label("Empty")

        self.create_selection_button("Select Quest 2 Region", "quest2")
        self.quest2_label = self.create_label("Empty")

        self.create_selection_button("Select Quest 3 Region", "quest3")
        self.quest3_label = self.create_label("Empty")

        self.create_selection_button("Select Reroll Button 1 Position", "reroll1")
        self.reroll1_label = self.create_label("Empty")

        self.create_selection_button("Select Reroll Button 2 Position", "reroll2")
        self.reroll2_label = self.create_label("Empty")

        self.create_selection_button("Select Reroll Button 3 Position", "reroll3")
        self.reroll3_label = self.create_label("Empty")

        self.save_btn = tk.Button(root, text="Save Regions and Buttons", command=self.save_regions, font=("Calibri", 12), bg="violet", fg="white", bd=0)
        self.save_btn.pack(pady=20)

    def create_selection_button(self, text, key):
        btn = tk.Button(self.root, text=text, command=lambda: self.select_region(key) if "Region" in text else self.select_button(key), font=("Calibri", 10), bg="gray", fg="white", bd=0)
        btn.pack(pady=5)

    def create_label(self, text):
        label = tk.Label(self.root, text=text, font=("Calibri", 10))
        label.pack()
        return label

    def select_region(self, quest_number):
        self.root.withdraw()

        select_root = tk.Toplevel(self.root)
        select_root.attributes("-fullscreen", True)
        select_root.attributes("-topmost", True)
        select_root.configure(bg='gray')
        select_root.attributes("-alpha", 0.3)

        self.start_x = self.start_y = self.end_x = self.end_y = 0

        def on_mouse_down(event):
            self.start_x, self.start_y = event.x, event.y
            self.rect = canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red", width=2)

        def on_mouse_move(event):
            if self.rect:
                canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

        def on_mouse_up(event):
            self.end_x, self.end_y = event.x, event.y
            
            # Ensure start and end coordinates are correctly ordered
            if self.start_x > self.end_x:
                self.start_x, self.end_x = self.end_x, self.start_x
            if self.start_y > self.end_y:
                self.start_y, self.end_y = self.end_y, self.start_y
            
            self.region = (self.start_x, self.start_y, self.end_x, self.end_y)
            self.regions[quest_number] = self.region
            self.update_label(quest_number, self.region)
            self.root.deiconify()
            select_root.destroy()


        select_root.bind("<ButtonPress-1>", on_mouse_down)
        select_root.bind("<B1-Motion>", on_mouse_move)
        select_root.bind("<ButtonRelease-1>", on_mouse_up)

        canvas = tk.Canvas(select_root, bg="white", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        select_root.mainloop()

    def select_button(self, button_name):
        self.root.withdraw()

        select_root = tk.Toplevel(self.root)
        select_root.attributes("-fullscreen", True)
        select_root.attributes("-topmost", True)
        select_root.configure(bg='gray')
        select_root.attributes("-alpha", 0.3)

        def on_mouse_down(event):
            self.button_x, self.button_y = event.x, event.y
            self.rect = canvas.create_oval(self.button_x-5, self.button_y-5, self.button_x+5, self.button_y+5, outline="red", width=2)

        def on_mouse_up(event):
            self.buttons[button_name] = (self.button_x, self.button_y)
            self.update_label(button_name, (self.button_x, self.button_y))
            self.root.deiconify()
            select_root.destroy()

        select_root.bind("<ButtonPress-1>", on_mouse_down)
        select_root.bind("<ButtonRelease-1>", on_mouse_up)

        canvas = tk.Canvas(select_root, bg="white", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        select_root.mainloop()

    def update_label(self, name, coordinates):
        coord_text = f"{name.capitalize().replace('_', ' ')}: {coordinates}"
        if name == "quest1":
            self.quest1_label.config(text=coord_text)
        elif name == "quest2":
            self.quest2_label.config(text=coord_text)
        elif name == "quest3":
            self.quest3_label.config(text=coord_text)
        elif name == "reroll1":
            self.reroll1_label.config(text=coord_text)
        elif name == "reroll2":
            self.reroll2_label.config(text=coord_text)
        elif name == "reroll3":
            self.reroll3_label.config(text=coord_text)

    def save_regions(self):
        with open("regions.json", "w") as file:
            json.dump({'regions': self.regions, 'buttons': self.buttons}, file)
        messagebox.showinfo("Success", "Regions and buttons saved successfully!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = RegionSelector(root)
    root.mainloop()
