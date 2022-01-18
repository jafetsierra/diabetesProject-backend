# DiabetesProject_backend
django backend build up for a diabetes prediction app employing xgboost

## The entire backend project is deployed on Heroku, if you want to use it, go to the next URL:
https://diabetes-app-v-1.herokuapp.com/ 

(This is only the backend API, if you want to user a graphic interface go to the frontend repository of this project https://github.com/jafetsierra/diabetesProject_frontend )


## Run this app in your pc as a server 

### Clone the repository and do the following comands:

*(note: you will prefer to use a virtual environment)*

For this, use the comand below in a bash terminal or a cmd window: 

>python3 -m venv your_virtual_env_name

and then in order to activate it, type

Linux:  

>source env/bin/activate

Windows: 

>env/Scripts/activate


### Install all dependencies:

>pip install -r requirements.txt

### Run the server

>python3 manage.py runserver

## Make a prediction

Now you can test the app creating a new user

http://127.0.0.1:8000/user/

Next you can make a new prediction using the following URL

http://127.0.0.1:8000/prediction/create/


