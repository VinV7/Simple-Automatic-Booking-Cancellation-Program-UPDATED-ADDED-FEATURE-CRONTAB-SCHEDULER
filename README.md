# Simple Automatic Booking Cancellation Program (UPDATED + ADDED FEATURE CRONTAB SCHEDULER) 

Automatic Booking Cancellation Program is program made to automatically cancel bookings if certain requirements are not met. Such as the payment time exceeds more than the given time which is 15 minutes (Modifiable). First the program will connect to the database which is [PostgreSQL](https://www.postgresql.org/) (You can use other kinds of databases e.g [MySql](https://www.mysql.com/), [Oracle](https://www.oracle.com/uk/), Etc) using [Psycopg2](https://pypi.org/project/psycopg2/) module. Secondly after connecting to the database, the program will then continue to check if certain requirements are met such as the order is booked but the payment status is still unpaid and if it has been more than 15 minutes since the given time to transfer the payments. Third, the program then will send a PATCH (Update) request to the [YCBM](https://youcanbook.me/) API cancelling the booking session and making the booking session appear again in the website. This program is still very simple yet very useful. This program can also be upgraded making it automate the process using a [CRON](https://en.wikipedia.org/wiki/Cron) scheduler. In the future i will be updating this program adding a Cron scheduler using [Apache Airflow](https://airflow.apache.org/) 

## Installation : 

First clone the code

```bash
git clone https://github.com/VinV7/Simple-Automatic-Booking-Cancellation-Program.git
```

Install the modules used in the code using [pip](https://pip.pypa.io/en/stable/)

```bash
pip install psycopg2
pip install requests
```
## Setting up to match up to your database / needs

Updating the required amount of time to proceed to update the database (e.g, Mine's need 15 minutes to proceed to update the database)

```bash
TIME_GIVEN = 900 #900 = 15 minutes, 1 minute = 60 seconds
```

If you're confused on how to change your database's table name just search for the line that has a script needing of certain database table then change it to your actual database name (e.g, my database's table names are orders_book and transactions. Don't forget to change the other ones too)

```bash
read_table_script = "SELECT * FROM [YOUR FIRST TABLE NAME HERE] INNER JOIN [YOUR SECOND TABLE NAME HERE] ON ([YOUR FIRST TABLE NAME HERE].book_code = [YOUR SECOND TABLE NAME HERE].book_code)"
```

## Setting up CRONTAB scheduler

First, check if your terminal already has a CRONJOB using the command

```bash
crontab -l
```

Second, if there is no CRONJOB then you're ready to go to schedule and add your CRONJOB using the command

```bash
crontab -e
```
Third, Check your python path location using the command

```bash
which python
```

Fourth, the terminal will then show a guide on how to set a CRONJOB. 

```bash
Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
* * * * * /usr/bin/python3 ~/path/to/your/python/projects.py #* * * * * means your script will run every minute

Then press CTRL + X and press Y to save
```

To setting when your cronjob will run go to [CRONTAB GURU](https://crontab.guru/) for further explanation

If you want to eliminate the crontab just type the command

```bash
crontab -r
```

## Modules and Database used : 

Database : 

[PostgreSQL](https://www.postgresql.org/)

Modules : 

[Psycopg2](https://pypi.org/project/psycopg2/)

[Requests](https://pypi.org/project/requests/)

## Features :

Connecting to a Database

Reading and Updating data inside the Database

Deleting and Updating booking sessions

## Technical Documentation References :
[https://api.youcanbook.me/docs/index.html](https://api.youcanbook.me/docs/index.html)

[https://www.psycopg.org/docs/](https://www.psycopg.org/docs/)

## Tutorial References :

[https://www.youtube.com/watch?v=KuQUNHCeKCk&ab_channel=BekBrace](https://www.youtube.com/watch?v=KuQUNHCeKCk&ab_channel=BekBrace)

[https://www.youtube.com/watch?v=Q8iYj2ypWss&ab_channel=BekBrace](https://www.youtube.com/watch?v=Q8iYj2ypWss&ab_channel=BekBrace)

[https://www.youtube.com/watch?v=8w3zHsEPFnQ&ab_channel=BekBrace](https://www.youtube.com/watch?v=8w3zHsEPFnQ&ab_channel=BekBrace)

[https://www.youtube.com/watch?v=a_1AEYxwLi8&ab_channel=BekBrace](https://www.youtube.com/watch?v=a_1AEYxwLi8&ab_channel=BekBrace)

[https://www.youtube.com/watch?v=7cbP7fzn0D8&ab_channel=LearnLinuxTV](https://www.youtube.com/watch?v=7cbP7fzn0D8&ab_channel=LearnLinuxTV)

## Licence

MIT License

Copyright (c) 2023 Albin Ivandito

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.