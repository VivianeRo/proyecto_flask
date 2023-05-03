from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homer-banking.html, saludo = persona1.salido()')

if __name__ == '__main__':

    from persona import Persona
    persona1 = Persona(356783,'Viviane')
    print(persona1.saludo())
    app.run(debug=True)