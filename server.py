from flask import Flask, jsonify

from Ressources import demineur

app = Flask(__name__)

demineur_ressource = demineur.demineurRessource()


@app.route('/')
def index():
    return "Bienvenue sur l'api-generator !"


@app.route('/demineur/<size_x>/<size_y>/<nb_bombs>')
def get_demineur(size_x, size_y, nb_bombs):
    res, status_code = demineur_ressource.get_game(size_x, size_y, nb_bombs)
    return jsonify(res)


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(500)
def ma_page_erreur(error):
    return "Erreur {}".format(error.code), error.code


if __name__ == '__main__':
    app.run(debug=True)


