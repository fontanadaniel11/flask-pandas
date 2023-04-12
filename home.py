from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
dati_film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep=";")

@app.route('/')
def home():
    film_ING = dati_film[dati_film['Language'] =='English']
    table = film_ING.to_html()
    return render_template('home.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)