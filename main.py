import tkinter as tk
from tkinter import filedialog
import crypto
import wallet
from pathlib import Path
#from tkinter import ttk as tk

def clear():
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    label4.pack_forget()
    created_wallet_label.pack_forget()
    wallet_is_created_label.pack_forget()
    add_to_wallet_button.pack_forget()

def upload_file():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text Files", "*.txt")])
    return file_path

def add_file_to_wallet():
    file_path = upload_file()
    key = wallet.read_from_wallet("aes_key.bin")
    ciphertext = crypto.encrypt_file(file_path, key)
    wallet.add_to_wallet("encrypted.bin", ciphertext)

# Function to be executed when the button is clicked
def on_button1_click():
    clear()
    label1.pack()

def on_button2_click():
    clear()
    label2.pack()
    add_to_wallet_button.pack()

def on_button3_click():
    clear()
    label3.pack()
    home_dir = Path.home()
    wallet_path = home_dir / ".gene_wallet"
    if wallet_path.exists() and wallet_path.is_dir():
        wallet_is_created_label.pack()
    else:
        aes_key = crypto.create_key()
        wallet.init_wallet()
        wallet.add_to_wallet("aes_key.bin", aes_key)
        created_wallet_label.pack()

def on_button4_click():
    clear()
    label4.pack()

# Create the main window
root = tk.Tk()
root.title("GeneWallet")
#root.configure(bg="darkgray")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
window_height = root.winfo_height()
left_frame = tk.Frame(root, width=100)
left_frame.pack(side="left", fill="y")
title =  tk.Label(root, text="GeneWallet", font=("Arial", 30))
title.pack()

# Create buttons
button1 = tk.Button(left_frame, text="Home", command=on_button1_click, font=("Arial", 12), width=20, height=3)
button2 = tk.Button(left_frame, text="Send/Receive", command=on_button2_click, font=("Arial", 12), width=20, height=3)
button3 = tk.Button(left_frame, text="Manage Wallet", command=on_button3_click, font=("Arial", 12), width=20, height=3)
button4 = tk.Button(left_frame, text="Settings", command=on_button4_click, font=("Arial", 12), width=20, height=3)
button1.pack(expand=True, fill="y")
button2.pack(expand=True, fill="y")
button3.pack(expand=True, fill="y")
button4.pack(expand=True, fill="y")

# Create temp labels
label1 = tk.Label(root, text="Home", font=("Arial", 16))
label2 = tk.Label(root, text="Send/Receive", font=("Arial", 16))
label3 = tk.Label(root, text="Manage Wallet", font=("Arial", 16))
label4 = tk.Label(root, text="Settings", font=("Arial", 16))

# label 2 

# Create encrypt button
add_to_wallet_button = tk.Button(root, text="Add File to Wallet", command=add_file_to_wallet)

# label 3
created_wallet_label = tk.Label(root, text="Created Wallet", font=("Arial", 12))
wallet_is_created_label = tk.Label(root, text="Wallet is already created.", font=("Arial", 12))


# Run the GUI event loop
root.mainloop()