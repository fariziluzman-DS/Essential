from flask import Flask,render_template,request
from datas import locations,property_type
from prediction import prediction
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        data['Bathrooms'] = int(data['Bathrooms'])
        data['Rooms'] = int(data['Rooms'])
        data['Size Num'] = int(data['Size Num'])
        hasil = prediction(data)
        return render_template('result.html' , hasil_pred=hasil)
    return render_template('prediction.html',
    data_location = sorted(locations), prop = property_type)

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
    app.run(debug=True)