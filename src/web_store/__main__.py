import os
from dotenv import load_dotenv
from flask import Flask, render_template, session, request
from flask import redirect, url_for

from web_store.testing import TestWebStore
from web_store.basket import Basket
from flask_wtf.csrf import CSRFProtect

#from web_store.basket import Basket

load_dotenv()

PATH= os.path.dirname(os.path.abspath(__file__))
PORT= os.getenv("SERVER_PORT") or 5000 

app = Flask(__name__, template_folder=os.path.join(PATH, 'templates'), static_folder=os.path.join(PATH, 'static'))
app.secret_key="kejjsbdnwilllshybxhajhdhgadgbdloehgbnc"

#csrf = CSRFProtect(app) en html {{ csrf_token() }}

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        session["usuario"]=request.form["username"]
        return redirect(url_for('home'))
    else: 
        if "usuario" in session:
            return redirect(url_for('home'))
        return render_template('login.html')
    


@app.route('/')
def index():
    if "usuario" in session:
        return home()
    return render_template('login.html')

    

@app.route('/home') # Página de inicio
def home():
    if "usuario" in session:
        return render_template('home.html')
    return render_template('login.html')

@app.route('/store')
def store():
    if "usuario" in session:
        return render_template('store.html')
    return render_template('login.html')


@app.route('/basket')
def basket():
    if "usuario" in session:
        return render_template('basket.html')
    return render_template('login.html')


@app.route('/checkout')
def checkout():
    if "usuario" in session:
        return render_template('checkout.html')
    return render_template('login.html')


@app.route('/building')
def building():
    if "usuario" in session:
        return render_template('building.html')
    return render_template('login.html')


@app.route('/bought')
def bought():
    if "usuario" in session:
        return render_template('bought.html')
    return render_template('login.html')



@app.route("/add_item", methods=["POST"])
def add_item():
    print("Modificando carrito")
    if "usuario" in session:
        item = request.form.get("item")
        quantity = request.form.get("quantity", 1)
        if item:
            basket = session.get("basket", {})
            basket[item] = basket.get(item, 0) + int(quantity)
            session["basket"] = basket
            print(session["basket"])
        return redirect(url_for('store'))
    return render_template('login.html')


@app.route('/<dinamic>')
def dinamic(dinamic):
    if "usuario" in session:
        return f"Esta es una ruta dinamic! {dinamic}"
    return render_template('login.html')


def main():
    print("Initiating Web Store")
    print(TestWebStore.test)
    app.run(host='0.0.0.0', port=PORT, debug=False)

if __name__ == "__main__":
    main()