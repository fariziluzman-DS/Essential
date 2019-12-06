from flask import Flask,render_template
from pokemon_plots import count_type1
from pokemon_plots import sum_type2
from pokemon_data import data_pokemon
app = Flask(__name__)

# ROUTE
# RENDER TEMPLATE
# RENDER TEMPLATE WITH VARIABLE

@app.route('/')
def index():
    return render_template('pokemon_home.html')

@app.route('/data')
def data():
    data = data_pokemon().head()
    return render_template('pokemon_table_data.html' , data=data)


@app.route('/plots')
def plots():
    data = count_type1()
    data2 = sum_type2()
    return render_template('pokemon_plot.html' , data=data, data2 = data2)










# @app.route('/hello')
# def hello():
#     hasil = 5 + 19
#     return 'Ini Route Hello ' + str(hasil)

# @app.route('/template')
# def sabeb():
#     return render_template('contoh.html')

# @app.route('/template-with-data')
# def template_with_data():
#     # data = {
#     #     'name' : 'fikri',
#     #     'name2' : 'seto',
#     #     'name3' : 'Andi'
#     # }
#     data = ['Fikri' , 'Seto' , 'Andi']
#     return render_template('data.html', nama = data , panjang= len(data))

if __name__ == '__main__':
    app.run(debug=True, port=1234)
