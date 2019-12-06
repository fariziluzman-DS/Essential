from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Ini Index <h1>'

@app.route('/about')
def about():
    return render_template('about.html', nama = 'Asep')

if __name__ == '__main__':
    app.run(debug=True, port=3000)


