## This is the file creates the database for keeping track of the weather


# Importing necessary packages
import sqlite3

# Connect to the database and create the cursor
con = sqlite3.connect('weather.db', isolation_level = None)
cur = con.cursor()

# Remove table during subsequent runs
cur.execute("DROP TABLE IF EXISTS WeatherPredictions;")

# Create WeatherPredictions table
create_table_weather = '''CREATE TABLE WeatherPredictions('date', 'guess_made', 'city', 'country')'''
cur.execute(create_table_weather)