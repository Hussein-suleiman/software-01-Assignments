import sqlite3


def list_airports_by_country(area_code):
    conn = sqlite3.connect("airports.sqlite")
    cur = conn.cursor()

    cur.execute("""
                SELECT type, COUNT(*)
                FROM airport
                WHERE iso_country = ?
                GROUP BY type
                ORDER BY type
                """, (area_code,))

    rows = cur.fetchall()
    conn.close()

    if rows:
        print(f"Airports in {area_code}:")
        for airport_type, count in rows:
            print(f"{airport_type}: {count}")
    else:
        print("No airports found for that area code.")


if __name__ == "__main__":
    country = input("Enter country area code (e.g. FI): ").strip().upper()
    list_airports_by_country(country)
