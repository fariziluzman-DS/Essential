import pickle
from pandas import DataFrame,get_dummies
from datas import predictframe,rateframe
Random_model = pickle.load(open('RandomForest_model.sav' , 'rb'))
Real_columns = pickle.load(open('Random_real_columns.sav' , 'rb'))
Dummy_columns = pickle.load(open('Random_dummies_columns.sav' , 'rb'))

def prediction(data):
    dfx = rateframe()
    df = DataFrame(data,index = [0])
    df = get_dummies(df)
    df = df.reindex(columns=Dummy_columns, fill_value=0)
    hasil = Random_model.predict(df)
    hasil = round(hasil[0])
    index_hasil = dfx[dfx['price'] == hasil].head(3).index
    index_hasil = list(index_hasil)
    return(hasil,index_hasil)

def residue_price(data):
    dfx = predictframe()
    dfx = dfx[dfx['Pred_Price'] == data].head(10).sort_values(by = 'Residue',ascending = False)
    return dfx





