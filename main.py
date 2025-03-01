import tkinter as tk
#from tkinter import ttk as tk

def clear():
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    label4.pack_forget()
    print("cleared")

# Function to be executed when the button is clicked
def on_button1_click():
    clear()
    #label1.place(x=200, y=200)
    label1.pack()
    print("Test 1 complete")

def on_button2_click():
    clear()
    #label2.place(x=200, y=200)
    label2.pack()
    print("Test 2 complete")

def on_button3_click():
    clear()
    #label3.place(x=200, y=200)
    label3.pack()
    print("Test 3 complete")

def on_button4_click():
    clear()
    #label4.place(x=200, y=200)
    label4.pack()
    print("Test 4 complete")

# Create the main window
root = tk.Tk()
root.title("GeneWallet")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
window_height = root.winfo_height()
print(window_height)


# Create buttons
button1 = tk.Button(root, text="Home", command=on_button1_click, font=("Arial", 12))
button2 = tk.Button(root, text="Send/Receive", command=on_button2_click, font=("Arial", 12))
button3 = tk.Button(root, text="Wallet", command=on_button3_click, font=("Arial", 12))
button4 = tk.Button(root, text="Settings", command=on_button4_click, font=("Arial", 12))
# button1.pack(side="left")
# button2.pack(side="left")
# button3.pack(side="left")
# button4.pack(side="left")
button1.place(x=0, y=0, height=window_height/4)
button2.place(x=0, y=window_height/4, height=window_height/4)
button3.place(x=0, y=window_height/4*2, height=window_height/4)
button4.place(x=0, y=window_height/4*3, height=window_height/4)

#button1.place(x=0, y=0, width=150, height=50)

# Create labels
label1 = tk.Label(root, text="Home", font=("Arial", 16))
label2 = tk.Label(root, text="Send/Receive", font=("Arial", 16))
label3 = tk.Label(root, text="Wallet", font=("Arial", 16))
label4 = tk.Label(root, text="Settings", font=("Arial", 16))

# Run the GUI event loop
root.mainloop()