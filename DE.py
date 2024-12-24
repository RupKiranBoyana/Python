import csv
import mysql.connector

# MySQL connection parameters
cnx = mysql.connector.connect(user='root', password='Root', host='127.0.0.1', database='DE1')
cursor = cnx.cursor()

# CSV file path
csv_file_path = r'C:\Users\kiran\Downloads\batting_stats.csv'

with open(csv_file_path, mode='r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute("INSERT INTO batting_stats(Date,	Batsmen,	Dismissal,	Runs, Balls, 4s,	6s,	dot, SR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", row)

cnx.commit()
cursor.close()
cnx.close()