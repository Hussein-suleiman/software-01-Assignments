import mysql.connector
from geopy.distance import geodesic

# Database connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="airportdb"
)

cursor = connection.cursor()

icao1 = input("Enter first ICAO code: ").upper()
icao2 = input("Enter second ICAO code: ").upper()

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor.execute(sql, (icao1,))
coord1 = cursor.fetchone()

cursor.execute(sql, (icao2,))
coord2 = cursor.fetchone()

if coord1 and coord2:
    distance_km = geodesic(coord1, coord2).kilometers
    print(f"Distance between {icao1} and {icao2}: {distance_km:.2f} km")
else:
    print("One or both ICAO codes not found in the database.")

cursor.close()
connection.close()
