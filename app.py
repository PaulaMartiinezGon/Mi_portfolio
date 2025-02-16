from flask import Flask, render_template

app = Flask(__name__)  # Crear la aplicación Flask

#Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html')  # Muestra la plantilla index.html

#Ruta para la página "Sobre mí"
@app.route('/about')
def about():
    return render_template('about.html')  # Muestra la plantilla about.html

if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la app en modo debug

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']
    print(f"Nuevo mensaje de {nombre} ({email}): {mensaje}")
    return "Mensaje enviado con éxito"

if __name__ == '__main__':
    app.run(debug=True)


