import pandas as pd # pip install pandas
from sklearn.model_selection import train_test_split  # pip install scikit-learn
from sklearn.linear_model import LogisticRegression
import joblib

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']

dataframe = pd.read_csv(url, names = names)
array = dataframe.values
X = array[:,0:8]
y = array[:,8]

test_size = 0.2
random_state = 101

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=test_size,random_state=random_state)

model = LogisticRegression()
model.fit(X_train,y_train)

# accuracy
result = model.score(X_test, y_test)
print(' ')
print(f"Result :{result.round(4)*100}%")
print(' ')

# save the model
filename = 'predict_80.pkl' #filetype can be .pkl or .sav
joblib.dump(model , filename)