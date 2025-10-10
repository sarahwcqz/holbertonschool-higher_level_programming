#!/usr/bin/python3
"""Module to learn about the basic security of APIs"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt
from flask_jwt_extended import JWTManager

# pour generer clee aleatoire
import secrets


#----- creer l'appli flask, server's entry point
app = Flask(__name__)
#----- creer obj d'identification basic
auth = HTTPBasicAuth()



users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}



############################## authentification client -> serveur ##############################

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username)["password"], password):
        return username
    
@app.route('/basic-protected')
@auth.login_required
def index():
    return "Basic Auth: Access Granted"



############################## renvoi du token par serveur ####################################
#genere cle forte aleatoire
strong_key = secrets.token_urlsafe(64)
app.config["JWT_SECRET_KEY"] = strong_key
#initialise extension JWT avec Flask
jwt = JWTManager(app)


#creer route pour authentifier user et retourner le token
@app.route("/login", methods=["POST"])
def login():
    # creer var username contenant le nom du user passe en request POST, si inex on met None par default
    username_json = request.json.get('username', None)
    # creer var paswd contenant le password passe en request POST, si inex => None
    pswd_json = request.json.get('password', None)
    #creer var user contenant le dictionnaire de donnees associe a ce user
    user_dict = users.get(username_json)

    #check si le user existe en memoire et pswd donne correspond a celui en memoire
        #si ca correspond pas
    if not user_dict or not check_password_hash(user_dict["password"], pswd_json):
        return jsonify({"error": "Unauthorized"}), 401

        #si ca correspond
    #creer un token
    access_token = create_access_token(identity=username_json, additional_claims={"role": user_dict["role"]})
    # attention a passer uniquement le nom et pas tout le dict du user
    # inserer le role (admin/pas admin)
    return jsonify(access_token=access_token)



############################################ creer des routes proteges en fonction du bon token #######################
@app.route("/jwt-protected")
# exige un token valide
@jwt_required()
def protected():
    current_user = get_jwt_identity()   #renvoi cle du dictionnaire du user => user1 / admin1
    return "JWT Auth: Access Granted"

#gestion d'erreur
    #token inexistant
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

    # token invalide
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401



@app.route("/admin-only")
@jwt_required()
def admin():
    user_id = get_jwt()     # renvoi un dictionnaire du token (playload)
    if user_id.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


########################### lancer le serveur si fichier exe directmnt ##############################33
if __name__ == '__main__':
    app.run()
