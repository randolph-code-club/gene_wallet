from pathlib import Path

def get_wallet_path():
	home_dir = Path.home()
	new_path = home_dir / ".gene_wallet"
	return new_path

def init_wallet():
	dir_path = get_wallet_path()
	dir_path.mkdir(parents=True, exist_ok=True)

def add_to_wallet(name, content):
	files_path = get_wallet_path() / "files"
	files_path.mkdir(parents=True, exist_ok=True)
	new_path = files_path / name
	with open(new_path, "wb") as f:
		f.write(content)

def read_from_wallet(name):
	new_path = get_wallet_path() / "files" / name
	with open(new_path, "rb") as f:
		return f.read()
	
def add_key_to_wallet(name, content):
	new_path = get_wallet_path() / name
	with open(new_path, "wb") as f:
		f.write(content)

def read_key_from_wallet(name):
	new_path = get_wallet_path() / name
	with open(new_path, "rb") as f:
		return f.read()
	
def list_wallet():
	files_path = get_wallet_path() / "files"
	files = [file.name for file in files_path.iterdir() if file.is_file()]
	return files

def write_emails(email):
	file_path = get_wallet_path() / "contacts.txt"
	if file_path.exists():
		with open(file_path, "a") as f:
			f.write(email + "\n")
	else:
		file_path.write_text(email + "\n")
