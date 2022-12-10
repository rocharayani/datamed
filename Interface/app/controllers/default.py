from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/noticia/<noticia>')
def noticia(noticia):
    return render_template('index.html', visivel=noticia)

