# Deployment-basics

`Deployment 1`

### Method 1: Create model library and save

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

------------
### Method 2: Flask 

(Folder: [Web Dev]() )   
**Flask:** Framework for building web applications in Python   
Use html to display the webpage operations, link stays active only when the code is running in VSCode.  

- **[main.py]() :** - Create file for Flask running for Web development
- **[readme.md]() :** - To note down steps
  - ```
      # install the flask package
      terminal >> pip install flask
      Now run the main.py file on command prompt
    ```
    After running the `main.py` , in command prompt it will appear -
    ![image](https://user-images.githubusercontent.com/38161827/191633186-fbb04b1e-15fb-4c18-b0f0-fb255860ed40.png)
    
-------------
### Method 3: AWS

**AWS :**
AWS CodeDeploy is a service that automates code deployments to any instance, 
including Amazon EC2 instances and instances running on-premises. 
