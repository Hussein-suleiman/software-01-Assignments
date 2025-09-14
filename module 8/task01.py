import mysql.connector

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",        # your username
    password="password",# your password
    database="airportdb" # replace with your DB name
)

cursor = connection.cursor()

icao = input("Enter ICAO code: ").upper()

sql = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(sql, (icao,))
result = cursor.fetchone()

if result:
    print(f"Airport name: {result[0]}, Location: {result[1]}")
else:
    print("No airport found with that ICAO code.")

cursor.close()
connection.close()
