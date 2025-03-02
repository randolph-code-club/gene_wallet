import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import crypto
import wallet
from pathlib import Path
import socket

selected_email = "haha"

grid_count = 0
def clear():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame_send.pack_forget()

def on_send_button_click(email):
    clear()
    global selected_email
    selected_email = email
    frame_send.pack()
    tk.Label(frame_send, text=f"You are sending your files to {selected_email}. This is dangerous.", font=("Arial", 12)).pack()
    usb_drive_button.pack(side="left")
    keybase_button.pack(side="right")

def send_all():
    tk.Label(frame_send, text=f"Sent all files to {selected_email}", font=("Arial", 12)).pack()

def upload_file():
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text Files", "*.txt")])
    return file_path

def update_emails():
    global grid_count
    email = add_emails_text_box.get()
    add_emails_text_box.delete(0, tk.END)
    wallet.write_emails(email)
    email_frame = tk.Frame(frame2, width=100)
    email_label = tk.Label(email_frame, text=email, font=("Arial", 12), anchor="w", width=30)
    email_send_button = tk.Button(email_frame, text="Send", command=lambda: on_send_button_click(email))
    email_receive_button = tk.Button(email_frame, text="Receive", command=update_emails)
    email_label.grid_columnconfigure(1, weight=1)
    email_label.grid_columnconfigure(2, weight=1)
    email_label.grid(row=grid_count, column=0, sticky="w")
    email_send_button.grid(row=grid_count, column=1, sticky="ew")
    email_receive_button.grid(row=grid_count, column=2, sticky="ew")
    grid_count += 1
    email_frame.pack()

def add_file_to_wallet():
    file_path = upload_file()
    key = wallet.read_key_from_wallet("aes_key.bin")
    ciphertext = crypto.encrypt_file(file_path, key)
    wallet.add_to_wallet(f"{Path(file_path).stem}.bin", ciphertext)
    refresh_file_list()

def refresh_file_list():
    for label in file_list_frame.winfo_children():
        label.destroy()
    for file in wallet.list_wallet():
        file_list_label = tk.Label(file_list_frame, text=Path(file).name, font=("Arial", 12))
        file_list_label.pack()
    file_list_frame.pack()

# Functions to be executed when the button is clicked
def on_button1_click():
    clear()
    frame1.pack()
    label1.pack()
    IPlabel.pack()
    Dirlabel.pack()

def on_button2_click():
    clear()
    frame2.pack()
    label2.pack()
    send_receive_frame.pack()
    add_emails_button.pack(side="left")
    add_emails_text_box.pack(side="right", pady=10)

def on_button3_click():
    clear()
    frame3.pack()
    label3.pack()
    home_dir = Path.home()
    wallet_path = home_dir / ".gene_wallet"
    if wallet_path.exists() and wallet_path.is_dir():
        wallet_is_created_label.pack(pady=10)
    else:
        aes_key = crypto.create_key()
        wallet.init_wallet()
        wallet.add_key_to_wallet("aes_key.bin", aes_key)
        created_wallet_label.pack(pady=10)
    add_to_wallet_button.pack()
    file_list_frame.pack()
    refresh_file_list()

def on_button4_click():
    clear()
    frame4.pack()
    label4.pack()

# Create the main window
root = tk.Tk()
root.title("GeneWallet")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
window_height = root.winfo_height()
left_frame = tk.Frame(root, width=100)
left_frame.pack(side="left", fill="y")
title = tk.Label(root, text="GeneWallet", font=("Arial", 30))
title.pack()
frame1 = tk.Frame(root, width=100)
frame2 = tk.Frame(root, width=100)
frame3 = tk.Frame(root, width=100)
frame4 = tk.Frame(root, width=100)
frame_send = tk.Frame(root, width=100)

# Create buttons
home_image = Image.open("icons/home.png")
home_image = home_image.resize((100, 100))
home_icon = ImageTk.PhotoImage(home_image)
send_image = Image.open("icons/email.png")
send_image = send_image.resize((100, 100))
send_icon = ImageTk.PhotoImage(send_image)
wallet_image = Image.open("icons/wallet.png")
wallet_image = wallet_image.resize((100, 100))
wallet_icon = ImageTk.PhotoImage(wallet_image)
settings_image = Image.open("icons/settings.png")
settings_image = settings_image.resize((100, 100))
settings_icon = ImageTk.PhotoImage(settings_image)
button1 = tk.Button(left_frame, image=home_icon, command=on_button1_click, font=("Arial", 12), width=200, height=3)
button2 = tk.Button(left_frame, image=send_icon, command=on_button2_click, font=("Arial", 12), width=200, height=3)
button3 = tk.Button(left_frame, image=wallet_icon, command=on_button3_click, font=("Arial", 12), width=200, height=3)
button4 = tk.Button(left_frame, image=settings_icon, command=on_button4_click, font=("Arial", 12), width=200, height=3)
button1.pack(expand=True, fill="y")
button2.pack(expand=True, fill="y")
button3.pack(expand=True, fill="y")
button4.pack(expand=True, fill="y")

# label 1 vars

# Create a socket and connect to an external server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IPAddr = s.getsockname()[0]
s.close()
IPlabel = tk.Label(frame1, text=IPAddr, font=("Arial", 16))
Dirlabel = tk.Label(frame1, text=(wallet.get_wallet_path()), font=("Arial",16))

# Create temp labels

label1 = tk.Label(frame1, text="Home", font=("Arial", 16))
label2 = tk.Label(frame2, text="Send/Receive", font=("Arial", 16))
label3 = tk.Label(frame3, text="Manage Wallet", font=("Arial", 16))
label4 = tk.Label(frame4, text="Settings", font=("Arial", 16))

# frame2 vars
send_receive_frame = tk.Frame(frame2, width=100)
add_emails_button = tk.Button(send_receive_frame, text="Add Emails", command=update_emails)
add_emails_text_box = tk.Entry(send_receive_frame, width=30)

# frame3 vars
created_wallet_label = tk.Label(frame3, text="Created Wallet", font=("Arial", 12))
wallet_is_created_label = tk.Label(frame3, text="Wallet is already created.", font=("Arial", 12))
add_to_wallet_button = tk.Button(frame3, text="Add File to Wallet", command=add_file_to_wallet)
file_list_frame = tk.Frame(frame3, width=100)

# frame_send vars
usb_drive_button = tk.Button(frame_send, text="USB Drive", command=send_all)
keybase_button = tk.Button(frame_send, text="Keybase.io", command=send_all)

on_button1_click()

# Run the GUI event loop
root.mainloop()
