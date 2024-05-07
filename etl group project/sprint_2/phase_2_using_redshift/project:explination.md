## Introduction

This section marks a transition from sprint one to a new phase. In this phase, the project has shifted its database foundation from a local database to AWS Redshift.

## Overview

This sprint primarily focuses on migrating the functionality developed in the previous sprint to a PostgreSQL database, particularly AWS Redshift.

## Files and Purpose

- `chesterfield_25-08-2021_09-00-00.csv`: Contains sales data in CSV format to be extracted and loaded into a PostgreSQL database.
- `cloud_formation.yml`: YAML file that creates an AWS S3 bucket, attaches an IAM policy, and associates triggers to execute a lambda function.
- `deployment-bucket-stack.yml`: Creates an S3 bucket and attaches an IAM policy. This bucket will contain the CloudFormation files and the lambda files.
- `docker-compose.yml`: File for setting up Docker containers.
- `install.sh`: Shell script automating the launch and creation of the ETL pipeline.
- `requirements-lambda.txt`: Lists Python dependencies for the lambda function.
- `requirements.txt`: Lists all dependencies needed to load data from CSV files into a PostgreSQL database.
- `sql_for_grafana`: Contains queries for Redshift or Grafana to visualize sales data.
- `test-lambda.sh`: Shell script to test the ETL pipeline. Inserts a CSV file into the bucket, triggering the lambda function to process and load data into the ETL pipeline.
- `.gitignore`: Specifies which files to ignore and save when updating the Git directory.
- `src` directory:
    - `.gitignore`: Functions similarly to the previous `.gitignore` file.
    - `data_utils.py`: Contains Python functions to extract data from CSV files.
    - `sql_utils.py`: Contains Python functions to load data into tables on AWS Redshift.
    - `lambda_function.py`: Contains the lambda handler serving as the entry point and executing the code.

## Usage

To run the project:
1. Open the terminal.
2. Check for running containers on Docker with `docker ps -a`.
3. Remove existing containers with:
    ```
    docker stop <container> <container>
    docker rm <container> <container>
    ```
4. Run the Python code with `py whyb_utils_postgres_guid.py`.
5. Log into the database by visiting [http://localhost:8080](http://localhost:8080) in your browser.
6. Select PostgreSQL as the database type.
7. Enter the following credentials:
    - Username: postgres
    - Password: password
8. Once logged in, you can view the data by writing SQL queries.

