from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_airport_by_icao(icao):
    conn = sqlite3.connect("airports.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, municipality FROM airports WHERE ident = ?",
        (icao,)
    )
    result = cursor.fetchone()

    conn.close()
    return result  # (name, municipality) or None


@app.route("/airport/<string:icao>")
def airport_lookup(icao):
    icao = icao.upper()  # Normalize input
    data = get_airport_by_icao(icao)

    if data is None:
        return jsonify({"Error": "Airport not found"}), 404

    name, location = data

    return jsonify({
        "ICAO": icao,
        "Name": name,
        "Location": location
    })


if __name__ == "__main__":
    app.run(debug=True)
