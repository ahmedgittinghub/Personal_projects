Where-have-you-Bean team project repo

<h1 align="center"> Where-have-you-Bean </h1>

<p align="center"> Team - Rifa, Aisha, Ahmed, Christina, Hannibal  </p>

Hello, Super-Café!

Introducing "Where Have Bean" - the app that will elevate your cafe's operations to new heights! With our powerful app, accurate demand forecasting becomes a breeze. In today's dynamic markets, data should be at the core of all your business decisions.

Gone are the days of relying on guesswork to cafe operations. No more uncertainties about how much inventory you need for the week, risking running out of stock or having items go to waste. Say goodbye to the guessing game of staff scheduling, where you're either understaffed and compromising customer service or overstaffed and facing unnecessary losses.

"Where Have Bean" empowers you with data-driven insights that accurately predict your demand, allowing you to achieve the "mug-nificent" taste of optimum efficiency.

Don't miss this opportunity to gain a competitive edge and outperform your competition. Stay ahead of the game by fulfilling your caffeinated community's demands with precision. The choice is yours - embrace the power of data and let "Where Have Bean" transform your cafes' success.
Introducing "Where Have Bean" - the app that will elevate operations to new heights! With our powerful app, accurate demand forecasting becomes a breeze. In today's dynamic markets, data should be at the core of all your business decisions.

Gone are the days of relying on guesswork to operate each cafe. No more uncertainties about how much inventory you need for the week, risking running out of stock or having items go to waste. Say goodbye to the guessing game of staff scheduling, where you're either understaffed and compromising customer service or overstaffed and facing unnecessary losses.

"Where Have Bean" empowers you with data-driven insights that accurately predict demand, allowing you to achieve the "mug-nificent" taste of optimum efficiency.

Don't miss this opportunity to gain a competitive edge and outperform your competition. Stay ahead of the game by fulfilling your caffeinated community's demands with precision. The choice is yours - embrace the power of data and let "Where Have Bean" transform your outlook on sales.

---

<h1 align="center"> How our Repository is structured </h1>

---

The folders are organised into each week's respective work, so there are remote backups we can use in case we need to look back and reference/reuse previous work.

<ins>[Sprint_1:](https://github.com/generation-DE-X4-LLe/Where-have-you-Bean/tree/main/sprint_1)<ins>

Includes work files required to set up and connect to a local MySQL database (Docker-compose.yml, .env and requirements.txt) and the code (whyb_code.py and whyb_utils.py) that will extract our data from the CSV file, Transform it and Load it to the SQL database, as well as one CSV file to test it's functionality with.

<ins>[Sprint_2:](https://github.com/generation-DE-X4-LLe/Where-have-you-Bean/tree/main/sprint_2)<ins>

Has been subdivided into 3 folders:
1) <ins>[Example_code_for_redshift:](https://github.com/generation-DE-X4-LLe/Where-have-you-Bean/tree/main/sprint_2/example_code_for_redshift)<ins>

   Files that we can use to reference when trying to recreate a Redshift database and set up the cloud formation process.

   
2) <ins>[Phase_1_using_postgres:](https://github.com/generation-DE-X4-LLe/Where-have-you-Bean/tree/main/sprint_2/phase_1_using_postgres)<ins>
   
   Includes work files required to set up and connect to a local PostgreSQL database (Docker-compose.yml, .env and requirements.txt) and the code (whyb_code_postgres_guid.py and whyb_utils_postgres_guid.py) that    will extract our data from the CSV file, Transform it and Load it to the PostgreSQL database, as well as one CSV file to test its functionality with.

3) <ins>[Phase_2_using_redshift:](https://github.com/generation-DE-X4-LLe/Where-have-you-Bean/tree/main/sprint_2/phase_2_using_redshift)<ins>

   Includes work files required to set up and connect to the remote Amazon Redshift database cloud_formation.yml, deployment-bucket-stack.yml, requirements-lambda.txt, and requirements.txt) and the code we will     run (sql_utils.py, data_utils.py, and lambda_function.py) to extract, Transform, and Load data from the CSV files inserted into our S3 Bucket to the Amazon Redshift database. 


**Each Sub-folder has its own unique README.md file with instructions on how to run the files. Please reference those to learn more!**





---
<h1 align="center"> How to - Run the application</h1>

---

In order to run the most updated version of the Application, please reference the latest sprint folder

(**Currently: Sprint_2/Phase_2_using_redshift:**)

---
<h1 align="center"> Resources</h1>

Click [here](https://trello.com/b/ZPgPrsHR/where-have-you-bean) to view our TrelloBoard



