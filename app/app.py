from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1>Hola mundo</h1>"
    return render_template("index.html")

@app.route('/hombre')
def hombre():
    return render_template("hombre.html")

@app.route('/mujer')
def mujer():
    return render_template("mujer.html")

@app.route('/niño')
def niño():
    return render_template("kid.html")

@app.route('/servicios')
def servicios():
    return render_template('servicio.html')

@app.route('/conocenos')
def conocenos():
    return render_template('conocenos.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# @app.get('/api/users')
# def get_users():
#     return 'getting users'

# @app.post('/api/users')
# def create_users():
#     print(request.get_json())
#     return 'creating users'

# @app.delete('/api/users/1')
# def delete_users():
#     return 'deleting users'

# @app.put('/api/users/1')
# def update_users():
#     return 'updating users'

# @app.get('/api/users/1')
# def get_user():
#     return 'getting user 1'