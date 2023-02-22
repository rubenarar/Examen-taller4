from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index_():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html')

@app.route('/acercade.html')
def acercade():
    return render_template('acercade.html')

@app.route('/productos.html')
def productos():
    return render_template('productos.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)