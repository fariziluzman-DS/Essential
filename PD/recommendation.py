import pickle
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from datas import fullrateframe

dfx = fullrateframe()

cv = CountVectorizer()
cv_amenities_result = cv.fit_transform(dfx['amenities'])
cv_df=pd.DataFrame(cv_amenities_result.todense(),columns=cv.get_feature_names(),index=dfx['asset'])
cos_sim_asset = cosine_similarity(cv_amenities_result)

def get_recommendation(asset,n):
    index_to_search=dfx[dfx['asset']==asset].index[0]
    series_similiar=pd.Series(cos_sim_asset[index_to_search])
    index_similiar = series_similiar.sort_values(ascending=False).head(n).index
    return index_similiar


