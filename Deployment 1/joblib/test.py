import joblib

# load the model
model = joblib.load('predict_80.pkl')

data = model.predict([[1,1,1,1,1,1,1,1]])

if data[0] == 0:
    print('not diabitic')
else:
    print('diabitic')