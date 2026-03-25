from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


fila = []

@app.route('/')
def home():
    return render_template('index.html', lista=fila)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    if nome:
        fila.append({'nome': nome, 'status': 'Aguardando'})
    return redirect(url_for('home'))

@app.route('/atender/<int:posicao>')
def atender(posicao):
    fila[posicao]['status'] = 'Em Atendimento'
    return redirect(url_for('home'))

@app.route('/finalizar/<int:posicao>')
def finalizar(posicao):
    fila[posicao]['status'] = 'Finalizado'
    return redirect(url_for('home'))

@app.route('/limpar')
def limpar():
    fila.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
