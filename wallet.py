from pathlib import Path

def get_wallet_path():
	home_dir = Path.home()
	new_path = home_dir / ".gene_wallet"
	return new_path

def init_wallet():
	dir_path = get_wallet_path()
	dir_path.mkdir(parents=True, exist_ok=True)

def add_to_wallet(name, content):
	new_path = get_wallet_path() / name
	with open(new_path, "wb") as f:
		f.write(content)

def read_from_wallet(name):
	new_path = get_wallet_path() / name
	with open(new_path, "rb") as f:
		return f.read()