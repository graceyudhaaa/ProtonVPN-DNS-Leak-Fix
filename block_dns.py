import glob

fix = """script-security 2
up /etc/openvpn/update-resolv-conf
down /etc/openvpn/update-resolv-conf"""

for i in glob.glob("*.ovpn"):
    with open(i, "r") as f:
        config = f.read()
    
    if (fix not in config):
        with open(i, "a") as f:
            f.write(fix)
