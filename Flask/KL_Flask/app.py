from flask import Flask,render_template
from loc import locations
from loc import property_group

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('prediction.html', nama_daerah = sorted(locations), nama_property = sorted(property_group))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=1234)