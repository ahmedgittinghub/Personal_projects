
## Introduction

This section is based upon sprint one but with a distinct diffrence, that diffrence being that in this phase we've moved the project to be based on a postgresql as opposed to Mysql.

## Overview
This sprint focuses on nigrating the previous sprint into a postgreSQL database.

## Files and purpose
- chesterfield_25-08-2021_09-00-00.csv : This file constains the sales data written in csv format which will be extracted and loaded into a postgreSQL database.
- cloud_formation.yml: This file written in yml format creates a AWS S3 bucket, Attaches a IAM policy then assocites triggers that trigger tha lambda function.
- deployment-bucket-stack.yml: This files creates a S3 bucket and attaches the IAM policy. The bucket will contain the cloud formation files and the lambda files.
- docker-compose.ymL: 
- install.sh : This contains a shell script which automates the luanch and creation of the etl pipeline.
- requirements-lambda.txt: this file contains  functions and code to extract and clean data from the csv files into python.
- requirements.txt: contains all code needed to load the data extract from csv files into a postgreSQL database.
- sql_for_grafana: This contains queries that can be wrriten in redshift or grafana to view sales data.
- test-lambda.sh: This is a shell script used to test the ETL pipeline once created. it will insert a csv file into the bucket which triggerts the lamdafunction to breakdown the data and load it up into etl pipeline.
- .gitignore: This file specifes functionality for git directory, it specififes to to git directory what files to ignore and what files to save when updating.
- src: 
    1. .gitignore: has the same functionality as the oner prior.
    2. data_utils.py : This contains all the python functions written to extract data from csv file.
    3. sql_utils.py : This contains all python functions to load the data into tables on AWS redshift.
    4. lambda_funtion.py : This contains the lambda handeler which serves as the entry point for the code and then also executes the code.

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

