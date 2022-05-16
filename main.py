from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def welcome():
    return 'My first flask application'


## this one in URL you can type /something and will print “Hello something”
@app.route("/<name>")
def wel(name):
    return f'Hello {name}'


## uses imports from flask and redirects to different URL
@app.route("/admin")
def admin():
    redirect(url_for(url_for("home")))


if __name__ == "__main__":
    app.run(debug=True)
