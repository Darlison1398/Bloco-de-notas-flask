from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
    



if __name__ == "__main__":
    app.run(debug=True)
    
# nesse caso, usamos o debug apenas em ambiente de desenvolvimento. 
# o ideal é tirar ele depois