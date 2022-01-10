import pandas as pd

def dic_to_dataframe(dictionary:dict):
    for k,v in dictionary.items():
        dictionary[k] = float(v)
    dictionary['user']  = int(dictionary['user'])
    dictionary_copy = dict(dictionary)
    dictionary_copy.pop('user')
    
    return pd.DataFrame(dictionary_copy, index=[0])

def transform_input(x):
    weight_class = pd.Series(["Under_weight","Normal_range","Overweight","Obesity_class_1","Obesity_class_2","Obesity_class_3"],dtype="category")
    insulin_class = pd.Series(["normal","abnormal"],dtype="category")
    x['insulin_new'] = insulin_class
    x['bmi_new'] = weight_class

    x.loc[ x['bmi']<=18.5, "bmi_new"] = weight_class[0]
    x.loc[(x['bmi']>18.5) & (x['bmi']<=24.9),"bmi_new"] = weight_class[1]
    x.loc[(x['bmi']>24.9) & (x['bmi']<=29.9),"bmi_new"] = weight_class[2]
    x.loc[(x['bmi']>29.9) & (x['bmi']<=34.9),"bmi_new"] = weight_class[3]
    x.loc[(x['bmi']>34.9) & (x['bmi']<=39.9),"bmi_new"] = weight_class[4]
    x.loc[x['bmi']>39.9, "bmi_new"] = weight_class[5]
    
    x.loc[(x['insulin']>=16) & (x['insulin']<=166),"insulin_new"] = insulin_class[0]
    x.loc[(x['insulin']<16) | (x['insulin']>166),"insulin_new"] = insulin_class[1]

    x_input = pd.get_dummies(x, columns=["bmi_new","insulin_new"])
    x_input = x_input.drop(['bmi'],axis=1)
   
    return x_input

def make_prediction(x_input):
    #First unpickle the lightGBM model previously trained on google colab
    xgb_model = pd.read_pickle(r'predictionApp/XGB/xbg_model.pickle')
    data = transform_input(dic_to_dataframe(x_input))
    x_input['rta']= bool(xgb_model.predict(data))
    #print(x_input)
    return x_input
