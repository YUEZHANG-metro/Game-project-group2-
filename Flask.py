from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='spy',   
        password='spy',  
        database='spy'  
    )
    return connection


@app.route('/get_country', methods=['GET'])
def get_country_initial_data():
    nation = request.args.get('country')  
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"""
        SELECT name, initial_capa_value 
        FROM player_country 
        JOIN country ON player_country.iso_country = country.iso_country
        WHERE country.iso_country = '{nation}'
    """)
    user_initial_data = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if user_initial_data:
        return jsonify(user_initial_data)  
    else:
        return jsonify({"error": "Country not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)