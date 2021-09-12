import glob

for i in glob.glob("*.ovpn"):
    with open(i, "r") as f:
        config = f.read()
    
    if ("block-outside-dns" not in config):
        with open(i, "a") as f:
            f.write("\nblock-outside-dns")
