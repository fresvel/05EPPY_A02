import os
from dotenv import load_dotenv
from flask import Flask, render_template

from web_store.testing import TestWebStore
from web_store.basket import Basket

load_dotenv()

PATH= os.path.dirname(os.path.abspath(__file__))
PORT= os.getenv("SERVER_PORT") or 5000 

app = Flask(__name__, template_folder=os.path.join(PATH, 'templates'), static_folder=os.path.join(PATH, 'static'))


@app.route('/')
def index():
    return home()

@app.route('/home') # Página de inicio
def home():
    return render_template('home.html')

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/basket')
def basket():
    return render_template('basket.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/building')
def building():
    return render_template('building.html')

@app.route('/bought')
def bought():
    return render_template('bought.html')

@app.route('/<dinamic>')
def dinamic(dinamic):
    return f"Esta es una ruta dinamic! {dinamic}"

def main():
    print("Initiating Web Store")
    print(TestWebStore.test)
    app.run(host='0.0.0.0', port=PORT, debug=False)

if __name__ == "__main__":
    main()