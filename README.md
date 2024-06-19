# Web Scraping and Data Storage Solution

This repository contains a Python script that extracts information from a list of websites and stores it into a MySQL/MariaDB database. The script uses web scraping techniques to gather meta information, social media links, tech stack details, and payment gateways from each website.

## Instructions to Run the Solution

### Prerequisites

Before running the script, ensure you have the following installed and set up:

- Python 3.x (with pip)
- MySQL/MariaDB server

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/aryam643/Web_Scraping
2. **Install Required Python Libraries:**
Use pip to install the necessary Python libraries (requests, beautifulsoup4, mysql-connector-python):
  
  pip install requests beautifulsoup4 mysql-connector-python

3. **Database Setup**:

-Create Database:
Connect to your MySQL/MariaDB server and create a database named WebsiteData:
```
CREATE DATABASE IF NOT EXISTS WebsiteData;
USE WebsiteData;
```

-Create Tables:

Execute the SQL script create_tables.sql to create the necessary tables (WebsiteInfo, SocialMediaLinks, TechStack, PaymentGateways) in the WebsiteData database. Adjust the script as per your database configuration if needed.

4. **Configure Script (Optional):**
If necessary, modify the database connection details (user, password, host) in the Python script scrape_and_store.py to match your MySQL/MariaDB setup.

5.**Run the Script:**
Execute the Python script to scrape websites and store data into the database:
```
python web_scraper.py
```
This script will iterate through a predefined list of websites, extract meta information, social media links, tech stack details, and payment gateways, and store them in the WebsiteData database.

6.**Verify Data:**

After running the script, connect to your MySQL/MariaDB server and verify that data has been correctly stored in the database tables (WebsiteInfo, SocialMediaLinks, TechStack, PaymentGateways). You can use SQL queries to inspect the stored data as needed.
