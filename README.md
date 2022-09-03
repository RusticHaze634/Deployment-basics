# Deployment-basics

`Deployment 1`

### Step 1: Create model library and save

#### Option 1: The joblib Folder
Joblib works better for huge dataset or models (prefereably Deep Learning models).  
Loading time less than pickle.   
- **[train.py](https://github.com/RusticHaze634/Deployment-basics/blob/main/Deployment%201/joblib/train.py) :** - create model in this file and save the model in Pickle  
- **[predict_80.pkl](https://github.com/RusticHaze634/Deployment-basics/blob/main/Deployment%201/joblib/predict_80.pkl):** - File created where model made in train.py is saved  
- **[test.py](https://github.com/RusticHaze634/Deployment-basics/blob/main/Deployment%201/joblib/test.py) :**  - launch the model from pickle file and predict  

#### Option 2: The Pickle Folder
Pickle works well for smaller models.   
Same as joblib - Copy the files from model library and paste in this folder
- **[train.py](https://github.com/RusticHaze634/Deployment-basics/blob/main/Deployment%201/pickle/train.py) :** - create model in this file and save the model in Pickle  
- **[predict_80.pkl](https://github.com/RusticHaze634/Deployment-basics/blob/main/Deployment%201/pickle/predict_80.pkl):** - File created where model made in train.py is dumped and opened 
- **[test.py](https://github.com/RusticHaze634/Deployment-basics/blob/main/Deployment%201/pickle/test.py) :**  - launch the model from pickle file and predict  
