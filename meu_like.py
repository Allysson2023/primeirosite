from flask import Flask, render_template

app = Flask(__name__)

#criar a 1 pagina do site
# route  -> hashtagtrinamento.com/contatos sempre vem depois da bara
# funçâo -> o que voce quer exibir naquela pagina
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)


if __name__ == "__main__":
    app.run(debug=True)

