from flask import Flask, render_template, request, redirect
from mascota import Mascota  # Assuming Mascota is a class in mascota.py

app = Flask(__name__)

@app.route("/")
def index():
    # Invokes the get_all method to obtain all the pets
    mascotas = Mascota.get_all()
    print(mascotas)
    return render_template("index.html", todas_mascotas=mascotas)
@app.route("/agregar")
def agregar():
    return render_template("agregar.html")

@app.route("/registro")
def get_all():
    # Invokes the get_all method to obtain all the pets
    mascotas = Mascota.get_all()
    print(mascotas)
    return render_template("registro.html", todas_mascotas=mascotas)

@app.route("/crear_mascota", methods=['POST'])
def crear_mascota():
    datos = {
        'nombre': request.form['nombre'],
        'tipo': request.form['tipo'],
        'color': request.form['color']
    }
    Mascota.save(datos)
    return redirect('/registro')

if __name__ == "__main__":
    app.run(debug=True)
