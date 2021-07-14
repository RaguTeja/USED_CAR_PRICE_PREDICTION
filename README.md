# CarPricePrediction
DATASET is from cardekho.com

Problem statement: Based on various parameters we need to estimate the selling price of the car.

Aim: To predict the selling price of a car based on it's properties like 'presentprice', 'how old it is?', 'fuel type' etc...

Deployment: HEROKU PLATFORM

Framework : Flask

FILES INFORMATION: 
1. Procfile : This file is important for deployment in heroku platform. Here we are telling the dynos applications of heroku to start the execution of source code from specified file with gunicorn server.
2. car_price_pred.ipynb : Here goes the steps of initial Data pipeline -> DATA COLLECTION, DATA ANALYSIS, FEATURE ENGINEERING, DATA PREPARATION, DATA MODELING, HYPERPARAMETER TUNING, MODEL EVALUATION, MODEL SELECTION and STORING THE MODEL IN THE PHYSICAL FILE.
3. app.py: In this file we create flask application. Through this web application we take query from the user and provide the results.
4. templates: This is the folder where we have our html files. This folder is automatically recognized by the flask application.
5. models: we have all machine learning models stored here.

 


