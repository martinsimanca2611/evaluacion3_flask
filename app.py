from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Página principal: menú con los 2 botones
@app.route("/")
def index():
    return render_template("index.html")


# Si alguien entra a /inicio, lo redirigimos al menú
@app.route("/inicio")
def inicio():
    return redirect(url_for("index"))


# Ejercicio 1: promedio de 3 notas y asistencia
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = None
    error = None

    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                error = "Las notas deben estar entre 10 y 70."
            elif not (0 <= asistencia <= 100):
                error = "La asistencia debe estar entre 0 y 100."
            else:
                promedio = round((nota1 + nota2 + nota3) / 3, 1)
                if promedio >= 40 and asistencia >= 75:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"
        except ValueError:
            error = "Debes ingresar solo números."

    return render_template("ejercicio1.html", promedio=promedio, estado=estado, error=error)


# Ejercicio 2: nombre con más caracteres
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre_largo = None
    cantidad = None
    error = None

    if request.method == "POST":
        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        if nombre1 == "" or nombre2 == "" or nombre3 == "":
            error = "Debes ingresar los 3 nombres."
        elif nombre1.lower() == nombre2.lower() or nombre1.lower() == nombre3.lower() or nombre2.lower() == nombre3.lower():
            error = "Los 3 nombres deben ser diferentes."
        else:
            nombre_largo = nombre1
            if len(nombre2) > len(nombre_largo):
                nombre_largo = nombre2
            if len(nombre3) > len(nombre_largo):
                nombre_largo = nombre3
            cantidad = len(nombre_largo)

    return render_template("ejercicio2.html", nombre_largo=nombre_largo, cantidad=cantidad, error=error)


if __name__ == "__main__":
    app.run(debug=True)