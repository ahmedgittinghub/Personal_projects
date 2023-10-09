<h1 align="center"> Where-have-you-Bean </h1>

<p align="center"> Team - Aisha, Hannibal, Rifa, Christina and Ahmed  </p>

---

<ins> **How to - Create and load tables into SQL database:** <ins>


Run the whyb_utils.py file.

(As this will also import and run everything in whyb_code.py file)

---
<h1 align="center"> Events Log </h1>

---

 **01 Aug** 
 
- Compiled all functions to create required lists to load data from into one .py file named "whyb_code.py".

- Compiled all functions to create tables to load data to, setup the connection with MYSQL server and loads data into said lists into one .py file named "whyb_utils.py" which imports required lists and functions from whyb_code.py.

- Both have been pushed to branch "compiled-work". Will push to main branch once final steps (units testing) are added.

- Updated the todolist file.

- Verified all are working as intended and produce required 3NF tables on MYSQL local host. 

- Unit tests for work is still a work in progress. Will be updated soon. 

---

***Completed EXTRACT ticket.**

<ins>**transform-remove-sensitive-data**<ins>

**27 July**

- Reworked supercafe.py and supercafe_utils.py to keep CASH options and drop columns without a functions via exclusion. -Christina


**26 July**

- Added: drop functions, load functions, utilities file (supercafe_utils.py) and the
Tested with sample CSV and sample utils files to see if similar functions would run

- Issues: mode_of_payment is loading all as “CARD” and not “CASH or CASH” -Christina 

