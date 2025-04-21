#Importation des bibliothèque
from flask import Flask, render_template, request #Serveur web
from werkzeug.utils import send_from_directory
import os
from dotenv import load_dotenv
from importer_expoter_sort import selection_sort

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

app = Flask(__name__)

@app.route("/static/<path:path>") #Route pour les appels des pages statiques
def static_dir(path):
    return send_from_directory("static", path) #il renvoie vers le dossier corespondant

@app.route('/') #Route par défaut lorsque on arrive sur le site sans paramètre
def index():
    return render_template('index.html') #Renvoie l'index.html

@app.route("/spells.html/<sring:type>", methods=['GET'])
def sort(type):
    return jsonify(selection_sort(type))

# lance le serveur web
print("Start Flask")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5401)