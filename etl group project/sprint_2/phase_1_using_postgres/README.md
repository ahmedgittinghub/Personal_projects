## Introduction

This section marks a distinct difference from sprint one, as the project has now been migrated to PostgreSQL from MySQL.

## Overview

This sprint focuses on migrating the previous sprint's functionality to a PostgreSQL database.

## Files and Purpose

- `chesterfield_25-08-2021_09-00-00.csv`: Sales data in CSV format to be extracted and loaded into a PostgreSQL database.
- `chesterfield_13-08-2023_09-00-00.csv`: Sales data in CSV format to be extracted and loaded into a PostgreSQL database.
- `london_brixton_11-08-2023_08-00-00.csv`: Sales data in CSV format to be extracted and loaded into a PostgreSQL database.
- `docker-compose.yml`: Instructions for setting up a local PostgreSQL database in YAML format.
- `requirements.txt`: Python dependencies required for setting up the PostgreSQL database.
- `whyb_code.py`: Contains functions and code to extract and clean data from the CSV files into Python.
- `whyb_utils.py`: Contains all code needed to load the extracted data from CSV files into a PostgreSQL database.

## Usage

To run the project:
1. Open the terminal.
2. Check for running containers on Docker with the command: `docker ps -a`.
3. Remove existing containers with the following commands:
    ```
    docker stop <container> <container>
    docker rm <container> <container>
    ```
4. In the terminal, run the following command to execute the Python code: `py whyb_utils_postgres_guid.py`.
5. Log onto the database you created by entering the following link in your browser: [http://localhost:8080](http://localhost:8080).
6. Select PostgreSQL as the database type.
7. Enter the following credentials:
    - Password: password
    - Username: postgres
8. Once logged in, you can view the data by writing SQL queries.
