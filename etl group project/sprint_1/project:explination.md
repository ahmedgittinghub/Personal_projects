
## Overview
This sprint focuses on developing a series of functions written in python code to extract data from the csv and load it up into a MySQL database

## Files and purpose
- chesterfield_25-08-2021_09-00-00.csv : This file constains the sales data written in csv format which will be extracted and loaded into a MYSQL database.
- docker-compose.ymL : This file conatins instructions to set up a local MYSQL database written in yml form.
- requirements.txt : This file conatins a list of python dependencies required for the MYSQL database set up.
- whyb_code.py : this file contains  functions and code to extract and clean data from the chesterfield_25-08-2021_09-00-00.csv into python.
- whyb_utils.py : contains all code needed to load the data extract from chesterfield_25-08-2021_09-00-00.csv into a MYSQL database.


## Usage
To run the project:
1. open terminal.
2. check for containers runnig on docker by the following command : docker ps -a.
3. remove the existing containers by the following set of code: 
    docker stop <container> <container>
    docker rm <container> <container>
4. In the terminal run the following command to run the python code "py whyb_utils_postgres_guid.py"
5. now log onto the database you created by inserting the following link your browser http://localhost:8080
6. select a MYSQL database for type.
7. insert the following : 
    password : password
    username : postgres
8. once you log in, go ahead and view the data by writing sql qurries.




