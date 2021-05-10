# Landing Page for A Future Product
An animated one page website as a teaser for a possible future project. 

Backend: Python / Flask / Mysql / !?Cloudsql?!
Frontend: HTML / CSS / javaScript

___Detailed dependencies are listed in a seperate requirements.txt file.___

IMPORTANT => Some environment variables related to database connection must be fed to system before deployment, these are listed below. . These can be either added into an .env file or coppied into activate file in virtual environment.

export DB_USER=           # e.g. "my-database-user"
export DB_PASS=           # e.g. "my-database-password"
export DB_NAME=          # e.g. "my-database-name"
export DB_HOST=         # e.g. "127.0.0.1:3306"

##There are two functionalities of the website:

1- Before rendering; it tries to connect to a database to fetch all rows from a table called Users, (which can be replicated with commands from initilize.sql) and counts them. Then it renders the homepage either with data that it fetched or with dumy data as part of a promotional campaign.

2- It saves the email and consent data from users to database.

#Acknowledgements

-System returns plain text after submit. This is intentional.
-The main aim of this project is to be a proof of ability for Berlin CODE University SE Foundations 2020/2021 Spring class assesment.
-Altough a version of this is available at https://h0m3gr33n.ey.r.appspot.com/ on gcp servers, I couldn't manage to connect it to an instance of cloud sql.