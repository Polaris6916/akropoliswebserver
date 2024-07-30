#Importation des bibliothèque
from flask import Flask, render_template, request, jsonify #Serveur web
from werkzeug.utils import send_from_directory
from akropolis_point_classe import * #Calcule des points
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

app = Flask(__name__)

@app.route("/static/<path:path>") #Route pour les appels des pages statiques
def static_dir(path):
    return send_from_directory("static", path) #il renvoie vers le dossier corespondant

@app.route('/') #Route par défaut lorsque on arrive sur le site sans paramètre
def index():
    return render_template('index.html') #Renvoie l'index.html

@app.route('/score.html/', methods=['GET']) #Route pour la page résultat (obsolète car on utilise la route getScore)
def computePlayerScore():
    result = request.args
    username = result['username']
    stone = int(result['stones'])
    star = int(result['stars'])
    quartiers = quartiersStrToArray(result['quartiers']) 
    score = playerScore(username, stone,star,quartiers)
    return render_template("resultat.html", score=score, nom=username)

@app.route('/getScore.html/<string:username>/<int:stones>/<int:stars>/<string:quartiersStr>', methods=['GET']) #Route pour renvoyer le score
def getScore(username,stones,stars,quartiersStr):
    quartiers = quartiersStrToArray(quartiersStr) # décode la chaîne de caractère
    score = playerScore(username, stones,stars,quartiers) # calcul le score du joueur
    return str(score)

# lance le serveur web
print("Start Flask")
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5400)