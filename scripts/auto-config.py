import os
from netmiko import ConnectHandler

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "..", "configs", "routers")

def load_devices():
    # Defina aqui a lista de devices ou leia de um CSV
    return [
        {"host": "192.168.1.1", "device_type": "cisco_ios", "username": "admin", "password": "senha"},
        {"host": "192.168.1.2", "device_type": "cisco_ios", "username": "admin", "password": "senha"}
    ]

def main():
    devices = load_devices()
    for dev in devices:
        cfg_file = os.path.join(CONFIG_DIR, f"{dev['host']}.cfg")
        if not os.path.isfile(cfg_file):
            print(f"[WARN] Config não encontrada para {dev['host']}")
            continue

        print(f"[INFO] Conectando em {dev['host']}...")
        with ConnectHandler(**dev) as conn:
            print(f"[INFO] Enviando config {cfg_file}")
            with open(cfg_file) as f:
                lines = f.read().splitlines()
            output = conn.send_config_set(lines)
            print(output)
            conn.save_config()
            print(f"[INFO] Config aplicada em {dev['host']}")

if __name__ == "__main__":
    main()