import sqlite3

def get_airport_by_icao(icao_code):
    conn = sqlite3.connect("airports.sqlite")
    cur = conn.cursor()

    cur.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao_code,))
    row = cur.fetchone()

    conn.close()

    if row:
        print(f"Airport name: {row[0]}")
        print(f"Location (town): {row[1]}")
    else:
        print("No airport found with that ICAO code.")


if __name__ == "__main__":
    code = input("Enter ICAO code: ").strip().upper()
    get_airport_by_icao(code)
