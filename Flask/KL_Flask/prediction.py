import pickle
from pandas import DataFrame,get_dummies
model = pickle.load(open('finalized_model.sav' , 'rb'))
real_columns = pickle.load(open('real_colomn.sav' , 'rb'))
dummy_columns = pickle.load(open('x_dummies_colomn.sav' , 'rb'))

def prediction(data):
    df = DataFrame(data,index = [0])
    df = get_dummies(df)
    df = df.reindex(columns=dummy_columns, fill_value=0)
    hasil = model.predict(df)
    return hasil

print(real_columns)