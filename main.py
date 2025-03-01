import tkinter as tk
from tkinter import filedialog
import crypto
import wallet
#from tkinter import ttk as tk

file_path = ""

def clear():
    label1.pack_forget()
    #label2.pack_forget()
    upload_file_button.pack_forget()
    file_label.pack_forget()
    encrypt_button.pack_forget()
    label3.pack_forget()
    label4.pack_forget()

def upload_file():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        file_label.config(text=f"Uploaded: {file_path}")  # Display file path

def encrypt_file():
    crypto.encrypt_file(file_path, "encrypted.bin", aes_key)

# Function to be executed when the button is clicked
def on_button1_click():
    clear()
    label1.pack()

def on_button2_click():
    clear()
    upload_file_button.pack()
    file_label.pack()
    encrypt_button.pack()

def on_button3_click():
    clear()
    aes_key = crypto.create_key()
    wallet.init_wallet()
    wallet.add_to_wallet("aes_key.bin", aes_key)
    #label3.pack()

def on_button4_click():
    clear()
    label4.pack()

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
button1.place(x=0, y=0, height=window_height/4)
button2.place(x=0, y=window_height/4, height=window_height/4)
button3.place(x=0, y=window_height/4*2, height=window_height/4)
button4.place(x=0, y=window_height/4*3, height=window_height/4)

# Create temp labels
label1 = tk.Label(root, text="Home", font=("Arial", 16))
#label2 = tk.Label(root, text="Send/Receive", font=("Arial", 16))
label3 = tk.Label(root, text="Wallet", font=("Arial", 16))
label4 = tk.Label(root, text="Settings", font=("Arial", 16))

# label 2 
# Create upload button
upload_file_button = tk.Button(root, text="Upload a .txt File", command=upload_file)

# Label to show uploaded file
file_label = tk.Label(root, text="No file selected", wraplength=300)

# Create encrypt button
encrypt_button = tk.Button(root, text="Encrypt File", command=encrypt_file)


# Run the GUI event loop
root.mainloop()