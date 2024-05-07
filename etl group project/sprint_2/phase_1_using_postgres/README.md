## Introduction

This section is based upon sprint one but with a distinct diffrence, that diffrence being that in this phase we've moved the project to be based on a postgresql as opposed to Mysql.

## Overview
This sprint focuses on nigrating the previous sprint into a postgreSQL database.

## Files and purpose
- chesterfield_25-08-2021_09-00-00.csv : This file constains the sales data written in csv format which will be extracted and loaded into a postgreSQL database.
- chesterfield_13-08-2023_09-00-00.csv : This file constains the sales data written in csv format which will be extracted and loaded into a postgreSQL database.
- london_brixton_11-08-2023_08-00-00.csv : This file constains the sales data written in csv format which will be extracted and loaded into a postgreSQL database.
- docker-compose.ymL : This file conatins instructions to set up a local postgreSQL database written in yml form.
- requirements.txt : This file conatins a list of python dependencies required for the postgreSQL database set up.
- whyb_code.py : this file contains  functions and code to extract and clean data from the csv files into python.
- whyb_utils.py : contains all code needed to load the data extract from csv files into a postgreSQL database.

## Usage
To run the project:
1. open terminal.
2. check for containers runnig on docker by the following command : docker ps -a.
3. remove the existing containers by the following set of code: 
    docker stop <container> <container>
    docker rm <container> <container>
4. In the terminal run the following command to run the python code "py whyb_utils_postgres_guid.py"
5. now log onto the database you created by inserting the following link your browser http://localhost:8080
6. select a postgresql database for type.
7. insert the following : 
    password : password
    username : postgres
8. once you log in, go ahead and view the data by writing sql qurries.




