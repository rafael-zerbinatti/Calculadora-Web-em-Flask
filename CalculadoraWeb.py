
import os
from re import template
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('calculadora.html')


@app.route('/calculaform', methods=['POST', 'GET'])
def calculaform():
    valor1 = request.form['val1']
    valor2 = request.form['val2']
    operacao = request.form['operacao']

    print(operacao)

    v1 = int(valor1)
    v2 = int(valor2)

    if (operacao == 'somar'):
        resultado = v1 + v2
    elif (operacao == 'subtrair'):
        resultado = v1 - v2
    elif (operacao == 'multiplicar'):
        resultado = v1 * v2
    elif (operacao == 'dividir'):
        if (v2 == 0):
            resultado = 'Não divisivel por 0'
        else:
            resultado = v1 / v2

    return str(resultado)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='127.0.0.1', port=port)
