''' Programa principal de MovieDB'''
from flask import Flask, request, url_for, render_template, redirect
import os
import random
import movie_classes as mc

app = Flask(__name__)
sistema = mc.SistemaCine()
archivos_actores = "datos/movies_db - actores.csv"
archivos_peliculas = "datos/movies_db - peliculas.csv"
archivos_relaciones = "datos/movies_db - relacion.csv"
archivos_usuarios = "datos/movies_db - users_hashed.csv"
sistema.cargar_csv(archivos_actores, mc.Actor)
sistema.cargar_csv(archivos_peliculas, mc.Pelicula)
sistema.cargar_csv(archivos_relaciones, mc.Relacion)
sistema.cargar_csv(archivos_usuarios, mc.User)

@app.route('/')
def index():
    '''pagina principal de la aplicacion'''
    actores = sistema.actores.values()
    return render_template('actores.html', actores=actores)

if __name__ == '__main__':
    app.run(debug=True)