from flask import render_template, request, url_for
from main import app
import os
from werkzeug.utils import secure_filename

@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")

@app.route("/customizar", methods=["POST"])
def customizar():
    nome = request.form.get("nome")
    cor = request.form.get("cor") or "#ffffff"

    foto = request.files.get("foto")
    if foto and foto.filename:
        filename = secure_filename(foto.filename)
        caminho = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        foto.save(caminho)
        foto_url = url_for('static', filename=f'../uploads/{filename}')
    else:
        foto_url = url_for('static', filename='img/perfil_padrao.jpg')

    return render_template("homepage.html", nome=nome, foto_url=foto_url, cor=cor)
