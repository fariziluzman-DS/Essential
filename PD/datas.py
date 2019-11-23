import pandas as pd
import pickle

city = ['Melbourne', 'East Melbourne', 'Port Melbourne', 'Parkville',
       'Carlton', 'North Melbourne', 'South Yarra', 'Flemington',
       'Southbank', 'West Melbourne', 'Docklands', 'Kensington',
       'South Wharf']

property_type = ['House', 'Apartment', 'Townhouse', 'Hotel', 'Guest suite',
       'Condominium', 'Bed and breakfast', 'Cottage', 'Guesthouse',
       'Loft', 'Boutique hotel', 'Bungalow', 'Tiny house',
       'Serviced apartment', 'Hostel', 'Villa', 'Barn', 'Cabin',
       'Camper/RV', 'Treehouse', 'Chalet', 'Other', 'Aparthotel',
       'Farm stay', 'Tent', 'Resort', 'Hut', 'Earth house', 'Castle',
       'Minsu (Taiwan)', 'Nature lodge', 'Boat', 'Campsite']

room_type = ['Private room', 'Entire home/apt', 'Shared room']

bed_type = ['Real Bed', 'Futon', 'Pull-out Sofa', 'Airbed', 'Couch']

def fullframe():
    # df1 = pd.read_csv('df2_clean.csv')
    df1 = pickle.load(open('df2_clean.sav' , 'rb'))
    return df1

def featureframe():
    df2 = pickle.load(open('data_feature_clean.sav' , 'rb'))
    return df2

def rateframe():
    df3 = pickle.load(open('df_rate1_clean.sav' , 'rb'))
    return df3

def predictframe():

    df4 = pickle.load(open('df_predict_clean.sav' , 'rb'))
    return df4

def fullrateframe():
    df5 = pickle.load(open('df_rate2_clean.sav' , 'rb'))
    return df5