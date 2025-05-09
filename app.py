from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

dados_usuario = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    global dados_usuario

    if request.method == 'POST':
        foto = request.files['foto']
        nome = request.form['nome']
        idade = request.form['idade']
        formacao = request.form['formacao']
        modalidade = request.form['modalidade']
        endereco = request.form['endereco']
        experiencia = request.form['experiencia']
        sobremim = request.form['sobremim']
        contato = request.form['contato']

        foto_path = ''
        if foto and foto.filename != '':
            foto_path = foto.filename
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], foto_path))

        dados_usuario = {
            'foto': foto_path,
            'nome': nome,
            'idade': idade,
            'formacao': formacao,
            'modalidade': modalidade,
            'endereco': endereco,
            'experiencia': experiencia,
            'sobremim': sobremim,
            'contato': contato
        }

        return render_template('principal.html', **dados_usuario)

    return render_template('inicial.html')


@app.route('/editar', methods=['GET', 'POST'])
def editar():
    global dados_usuario

    if request.method == 'POST':
        foto = request.files['foto']
        nome = request.form['nome']
        idade = request.form['idade']
        formacao = request.form['formacao']
        modalidade = request.form['modalidade']
        endereco = request.form['endereco']
        experiencia = request.form['experiencia']
        sobremim = request.form['sobremim']
        contato = request.form['contato']

        foto_path = dados_usuario.get('foto', '')
        if foto and foto.filename != '':
            foto_path = foto.filename
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], foto_path))

        dados_usuario = {
            'foto': foto_path,
            'nome': nome,
            'idade': idade,
            'formacao': formacao,
            'modalidade': modalidade,
            'endereco': endereco,
            'experiencia': experiencia,
            'sobremim': sobremim,
            'contato': contato
        }

        return render_template('principal.html', **dados_usuario)

    return render_template('editar.html', **dados_usuario)


if __name__ == '__main__':
    app.run(debug=True)