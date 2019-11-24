import folium
from folium.plugins import HeatMap
from flask import Flask,render_template,request,redirect,url_for
from datas import city,property_type,room_type,bed_type,fullframe,featureframe,rateframe,fullrateframe
from prediction import prediction,residue_price
from recommendation import get_recommendation
from plots import EDA_Type1,EDA_Type2,EDA_Type3,EDA_Type4,EDA_Type5,EDA_Type6,EDA_Type7

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            data = request.form
            data = data.to_dict()
            data['accommodates'] = int(data['accommodates'])
            data['bedrooms'] = int(data['bedrooms'])
            data['bathrooms'] = int(data['bathrooms'])
            data['minimum_nights'] = int(data['minimum_nights'])
            data['maximum_nights'] = int(data['maximum_nights'])
            hasil,index_hasil = prediction(data)
            return redirect(url_for('result',hasil=hasil,index_hasil = index_hasil,page = 1))
        except:
            return redirect(url_for('error'))
    return render_template('prediction.html',
    data_all = sorted(city) , prop_all = property_type,
    room_all = room_type, bed_all = bed_type )

@app.route('/EDA/<int:page>')
def EDA(page):
    dfx = fullrateframe()
    data1 = EDA_Type1()
    data2 = EDA_Type2()
    data3 = EDA_Type3()
    data4 = EDA_Type4()
    data5 = EDA_Type5()
    data6 = EDA_Type6()
    data7 = EDA_Type7(dfx[dfx['category'] == 'Superb']['clean_text'])
    data8 = EDA_Type7(dfx[dfx['category'] == 'Good']['clean_text'])
    data9 = EDA_Type7(dfx[dfx['category'] == 'Average']['clean_text'])
    data10 = EDA_Type7(dfx[dfx['category'] == 'Poor']['clean_text'])
    all_judul = ['Heatmap of Features Correlation','Comparison Between Maximum Nights and Minimum Nights',
    'Insight of Bedtype on Melbourne Airbnb Assets', 'Comparison Between Melbourne Airbnb Asset Types',
    'Insight of Melbourne Airbnb Assert with Highest Prices', 'Simple Animation of Melbourne Airbnb Assets Development',
    'Important Words for Superb Class','Important Words for Good Class','Important Words for Average Class',
    'Important Words for Poor Class']
    judul = all_judul[page-1]

    all_data = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]
    data = all_data[page-1]
    return render_template('EDA.html',data1 = data,judul=judul,page=page)
  
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/result')
def result():
        try:
            dfx = rateframe()
            page = request.args.get('page')
            page = int(page)
            residue = request.args.get('hasil')
            residue = float(residue)
            residue_frame = residue_price(residue)
            index = request.args.getlist('index_hasil')
            new_index = [int(x) for x in index]
            data_frame = dfx.loc[new_index]
            all_rec_pred = [data_frame,residue_frame]
            rec_pred = all_rec_pred[page-1]
            return render_template('result.html',hasil_pred=request.args.get('hasil'),rec_pred = rec_pred,page = page)
        except:
            return redirect(url_for('error'))
    
@app.route('/recommendation',methods=['GET','POST'])
def recomm():
    if request.method == 'POST':
        try:
            dfx = rateframe()
            rec_data = request.form
            rec_data = rec_data.to_dict()
            rec_asset = rec_data['Recomm1']
            rec_index =int(rec_data['Recomm2'])
            rec = get_recommendation(rec_asset,rec_index)
            rec = list(rec)
            new_index = [int(x) for x in rec]
            data_frame = dfx.loc[new_index]
            return render_template('recommendation.html', frame_rec = data_frame,hasil=True)
        except:
            return redirect(url_for('error'))
    return render_template('recommendation.html',hasil=False)

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/geo')
def geojson():
    dfx = fullframe()
    list_lat_long = []

    for index,value in dfx.iterrows():
        temp = [value['latitude'], value['longitude']]
        list_lat_long.append(temp)

    total_price_mean = dfx.groupby(['property_type']).mean()[['price']].sort_values(by='price')

    map_melbourne = folium.Map(location=[-37.8136,144.9631],zoom_start=10,tiles='OpenStreetMap',control_scale=True)
    HeatMap(data=list_lat_long, radius=10, oppacity=0.1).add_to(map_melbourne)

    folium.Marker([-37.8136,144.9631],
                    popup='Melbourne',
                    icon = folium.Icon(color = 'red', icon ='home', prefix = 'fa')
                    ).add_to(map_melbourne)

    for item in range (len(total_price_mean)):
        folium.Circle([-37.8136,144.9631],
                        radius=list((total_price_mean.values[item]+2)*50),
                        tooltip=str(total_price_mean.index[item]),
                        ).add_to(map_melbourne)

    return map_melbourne._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)
