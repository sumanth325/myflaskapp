from flask import Flask, render_template
from data import Articles

app = Flask (__name__)

Articles = Articles()

@app.route('/')
def index ():
    return render_template('home.html')

@app.route('/about')
def about ():
    return render_template('about.html')

@app.route('/contact')
def contact ():
    return render_template('contact.html')

@app.route('/articles')
def articles ():
    return render_template('articles.html', articles = Articles)
    
@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

@app.route('/BCI')
def bci ():
    return render_template('bci.html')

@app.route('/connectomics')
def connectomics ():
    return render_template('connectomics.html')

@app.route('/memory')
def memory ():
    return render_template('memory.html')

@app.route('/sensors')
def sensors ():
    return render_template('sensors.html')

@app.route('/Vision')
def vision ():
    return render_template('vision.html')



if __name__ == "__main__":
    app.run(debug=True)