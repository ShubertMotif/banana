from flask import Flask, render_template

app = Flask(__name__)

# Variabile per tenere traccia delle visite totali
visite_totali = 0

@app.route('/')
def home():
    global visite_totali
    # Incrementa il conteggio delle visite totali ad ogni richiesta
    visite_totali += 1
    return render_template('index.html', visite=visite_totali)

if __name__ == '__main__':
    app.run(debug=True)
