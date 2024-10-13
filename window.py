import tkinter as tk
from tkinter import ttk

class Window:
    def __init__(self, master, chatbot):
        self.master = master
        self.master.title("Cook&Eat")
        self.master.resizable(width=False, height=False)
        self.chatbot = chatbot

        bx_color = "#262626"  # Box background
        bg_color = "#161616"  # background
        bt_color = "#2f2f2f"  # button color
        fg_color = "#FAFAFA"  # text
        ac_bg_color = "#04AA77"  # Active background color when pressed
        ac_fg_color = "#FFFF00"  # Active foreground color when pressed
        self.master.configure(bg=bg_color)
        # Create a frame for layout
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)
        self.frame.configure(bg=bg_color)
        
        title_label = tk.Label(self.frame, text="Cook&Eat ~ HackPSU Demo 2024", font=("Hack", 16), bg=bg_color, fg=fg_color)
        title_label.pack(pady=(0, 10))  # Add some padding below the title
        # Dropdown menu variable
        self.dropdown_var = tk.StringVar(value="Select an option")

        # Create a dropdown menu
        self.dropdown = ttk.Combobox(self.frame, textvariable=self.dropdown_var, 
                                      values=["Your Pantry", "Your Appliances", "Desired Meal"])
        self.dropdown.pack(side=tk.TOP, padx=5)
        self.dropdown.bind("<<ComboboxSelected>>", self.update_input_box)
        self.dropdown.config(background=ac_bg_color)

        # Create input box
        self.input_box = tk.Text(self.frame, height=10, width=80, 
                                 bg=bx_color, fg=fg_color)
        self.input_box.pack(padx=5, pady=5)

        # Create output box with a scrollbar
        self.output_frame = tk.Frame(self.frame)
        self.output_frame.pack(padx=5, pady=5)

        # Scrollbar for output box
        self.output_scrollbar = tk.Scrollbar(self.output_frame, bg=bt_color, activebackground=ac_bg_color)
        self.output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Output box
        self.output_box = tk.Text(self.output_frame, height=10, width=80, 
                                   yscrollcommand=self.output_scrollbar.set, bg=bx_color, fg=fg_color)
        self.output_box.pack(side=tk.LEFT)

        # Configure the scrollbar
        self.output_scrollbar.config(command=self.output_box.yview)

        # Submit button
        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit_input, bg=bt_color, fg=fg_color, activebackground=ac_bg_color)
        self.submit_button.pack(pady=5)

        # Idea button
        self.idea_button = tk.Button(self.frame, text="Get Idea", command=self.idea_input, bg=bt_color, fg=fg_color, activebackground=ac_bg_color)
        self.idea_button.pack(pady=5)

    def update_input_box(self, event):
        selected_item = self.dropdown_var.get()
        self.input_box.delete(1.0, tk.END)
        if selected_item == "Your Pantry":
            open("ingredients.txt", "a")
            file = open("ingredients.txt", "r")
            ingredients = file.read()
            file.close()
            self.input_box.insert(tk.END, ingredients)
        elif selected_item == "Your Appliances":
            open("appliances.txt", "a")
            file = open("appliances.txt", "r")
            utensils = file.read()
            file.close()
            self.input_box.insert(tk.END, utensils)
        elif selected_item == "Desired Meal":
            self.input_box.insert(tk.END, "I want to make: ")

    def submit_input(self):
        input_text = self.input_box.get(1.0, tk.END).strip()
        selected_item = self.dropdown_var.get()
        if selected_item == "Your Pantry":
            file = open("ingredients.txt", "w")
            file.write(input_text)
            file.close()
            print("Updated Pantry")
            self.output_box.delete(1.0, tk.END)
            self.output_box.insert(tk.END, "Updated Pantry")
        elif selected_item == "Your Appliances":
            file = open("appliances.txt", "w")
            file.write(input_text)
            file.close()
            print("Updated Appliances")
            self.output_box.delete(1.0, tk.END)
            self.output_box.insert(tk.END, "Updated Appliances")
        elif selected_item == "Desired Meal":
            self.output_box.delete(1.0, tk.END)
            self.output_box.insert(tk.END, "Generating a recipe for you...")
            response = self.chatbot.prompt_specific(input_text);
            self.output_box.delete(1.0, tk.END)
            self.output_box.insert(tk.END, response)
        else:
            self.output_box.delete(1.0, tk.END)

    def idea_input(self):
            self.output_box.delete(1.0, tk.END)
            self.output_box.insert(tk.END, "Generating a recipe for you...")
            response = self.chatbot.prompt_list();
            self.output_box.delete(1.0, tk.END)
            self.output_box.insert(tk.END, response)

if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
