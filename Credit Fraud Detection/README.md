# Credit Fraud Detection

This dataset consists data about users info and credit card status, the goal is to predict which user that has fraud credit or not

### Data Source

From my mentor

### How to handle it ?

Please read the notebook

### How to handle the outliers ?

```python
  def UwU(a) :
    data = a
    listFeature = list(data.columns[1:])
    for item in listFeature:
        q3 = data[item].quantile(0.75)
        q1 = data[item].quantile(0.25)
        iqr = q3-q1
        lower_limit = q1-(1.5*iqr)
        upper_limit = q3+(1.5*iqr)
        return data[(data[item] < lower_limit) | (data[item] > upper_limit) & (data['flag_kredit_macet'] == 0)].index
```

### How to handle the imbalance from all of the target ?

Please read the notebook, i am using all of the possibility ( SMOTE, ROS, Undersampling etc.. )

