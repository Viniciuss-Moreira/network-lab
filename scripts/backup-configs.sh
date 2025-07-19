CONFIG_DIR="$(dirname "$0")/../configs/routers"
BACKUP_DIR="$(dirname "$0")/../configs/backup-$(date +%F)"
DEVICES=( "192.168.1.1" "192.168.1.2" )

mkdir -p "$BACKUP_DIR"

for ip in "${DEVICES[@]}"; do
    dest="$BACKUP_DIR/${ip}.cfg"
    echo "[INFO] Backup de $ip -> $dest"
    scp admin@"$ip":/etc/network/config "$dest"
done

echo "[INFO] Backup concluído em $BACKUP_DIR"