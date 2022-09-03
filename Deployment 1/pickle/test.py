import pickle

#load the model

model = pickle.load(open('predict_80.pkl' , 'rb'))

result = model.predict([[1,2,3,4,5,6,7,8]])

print(result[0])
