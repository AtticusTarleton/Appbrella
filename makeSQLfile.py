## This is the file creates the database for keeping track of the weather


# Importing necessary packages
import sqlite3
import datetime

# Connect to the database and create the cursor
con = sqlite3.connect('weather.db', isolation_level = None)
cur = con.cursor()

# Remove table during subsequent runs
cur.execute("DROP TABLE IF EXISTS WeatherPredictions;")

# Create WeatherPredictions table
create_table_weather = '''CREATE TABLE WeatherPredictions('date', 'guess_made', 'city', 'country')'''
cur.execute(create_table_weather)


today = datetime.date.today()
date = str(today)
cur.execute('INSERT into WeatherPredictions ("guess_made", "date")'
f'VALUES ("testing123", "{date}")')
preds = cur.execute(f'SELECT guess_made FROM WeatherPredictions WHERE '
                   f'date = "{date}"').fetchall()

for i in preds:
    print(i[0])

preds2 = cur.execute(f'SELECT date FROM WeatherPredictions').fetchall()
for i in preds2:
    print(i[0])
    print(i[0] == date)


con.close()