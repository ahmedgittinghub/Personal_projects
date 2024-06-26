## Overview
This sprint focuses on developing a series of Python functions to extract data from a CSV file and load it into a MySQL database.

## Files and Purpose
- `chesterfield_25-08-2021_09-00-00.csv`: Sales data in CSV format to be extracted and loaded into a MySQL database.
- `docker-compose.yml`: Instructions for setting up a local MySQL database in YAML format.
- `requirements.txt`: Python dependencies required for setting up the MySQL database.
- `whyb_code.py`: Contains functions and code to extract and clean data from `chesterfield_25-08-2021_09-00-00.csv`.
- `whyb_utils.py`: Contains code to load the extracted data into a MySQL database.

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
6. Select MySQL as the database type.
7. Enter the following credentials:
    - Password: password
    - Username: postgres
8. Once logged in, you can view the data by writing SQL queries.




