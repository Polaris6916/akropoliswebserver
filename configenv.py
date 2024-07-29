import socket

def get_local_ip():
    try:
        # Créer une connexion réseau à un serveur DNS public (Google DNS)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Erreur lors de l'obtention de l'adresse IP locale: {e}")
        return "127.0.0.1"

# Fonction pour mettre à jour le fichier .env
def update_env_file():
    local_ip = get_local_ip()
    with open('.env', 'w') as env_file:
        env_file.write(f"SERVER_URL=http://{local_ip}:5400\n")