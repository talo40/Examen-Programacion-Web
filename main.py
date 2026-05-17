from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = int(request.form.get('edad'))
        cantidad = int(request.form.get('cantidad_tarros'))

        total = cantidad * 9000

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total * (1 - descuento)

        resultado = {
            'nombre': nombre,
            'total': total,
            'total_con_descuento': total_con_descuento,
            'descuento': int(descuento * 100)
        }

    return render_template('ejercicio1.html', resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form.get('usuario').lower()
        password = request.form.get('password')

        if usuario == 'juan' and password == 'admin':
            mensaje = "Bienvenido administrador juan"
        elif usuario == 'pepe' and password == 'user':
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)