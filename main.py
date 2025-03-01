import tkinter as tk
#from tkinter import ttk as tk

# Function to be executed when the button is clicked
def on_button_click():
    print("Test complete")

# Create the main window
root = tk.Tk()
root.title("GeneWallet")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Create a button
button1 = tk.Button(root, text="Clickie clickie", command=on_button_click, font=("Comic Sans MS", 12), height=9)
button2 = tk.Button(root, text="Clickie clickie", command=on_button_click, font=("Comic Sans MS", 12), height=9)
button3 = tk.Button(root, text="Clickie clickie", command=on_button_click, font=("Comic Sans MS", 12), height=9)
button4 = tk.Button(root, text="Clickie clickie", command=on_button_click, font=("Comic Sans MS", 12), height=9)
# button1.pack(side="left")
# button2.pack(side="left")
# button3.pack(side="left")
# button4.pack(side="left")

button1.place(x=0, y=0)
button2.place(x=0, y=244)
button3.place(x=0, y=488)
button4.place(x=0, y=732)

# Run the GUI event loop
root.mainloop()