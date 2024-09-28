import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database=DATABASE_NAME,
    user=DATABASE_USERNAME,
    password=DATABASE_PASSWORD,
    autocommit=True
)

def main():
    iso_country = country_selection()

# This function will prompt user to select a country, then return the selected country's iso_country
def country_selection():
    player_countries_raw = fetch_data(
        "SELECT country.name as name, player_country.iso_country FROM player_country, country WHERE country.iso_country = player_country.iso_country"
    )
    player_countries = []
    for i in player_countries_raw:
        player_countries.append(i)
    count = 1
    print("Select a country: ")
    for country in player_countries:
        print(f"{count}: {country[0]}")
        count += 1
    selected_country = player_countries[int(input("Selection: ")) - 1]
    print(f"Selected country: {selected_country[0]}")
    return selected_country[1]


def fetch_data(query: str, params: tuple = None) -> list:
    cursor = connection.cursor()
    if params is not None:
        cursor.execute(query, params)
        return cursor.fetchall()
    else:
        cursor.execute(query)
        return cursor.fetchall()



if __name__ == '__main__':
    main()