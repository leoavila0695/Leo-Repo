import requests
from bs4 import BeautifulSoup
import json
import os

# Wikipedia URL  
URL = "https://en.wikipedia.org/wiki/ASEAN"
FILE_NAME = "asean_data.json"

# function to get the page and parse it
def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser") 
    else:
        raise Exception(f"Error {response.status_code}: was not possible to get the page")

# function to extract the data from the 'Urban areas' table"
def extract_data(soup):
    table = soup.find("table", class_="wikitable")
    if not table:
        raise Exception("Urban areas was not found")
    
    rows = table.find_all("tr")[1:]  # in order to avoid the first line in the headers
    countries_dict = {}
    
    for row in rows:
        columns = row.find_all("td")
        if len(columns) < 4:
            continue  # To jump line without enough columns
        
        country = columns[0].text.strip()
        city = columns[1].text.strip()
        population = int(columns[2].text.replace(",", ""))  # To convert to number(Int)
        area_km2 = float(columns[3].text.replace(",", ""))  # To convert to number(Float)
        
        density = round(population / area_km2, 2) if area_km2 else 0 
        
        if country not in countries_dict:  
            countries_dict[country] = {"cities": []}
        
        countries_dict[country]["cities"].append({
            "name": city,
            "population": population, 
            "area_km2": area_km2, 
            "density": density
        })
    
    return countries_dict

# In order to compare with saved data and to update  
def save_data(new_data, filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            old_data = json.load(file)
            if old_data == new_data:
                print("There are no data updated.")
                return
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(new_data, file, indent=4, ensure_ascii=False) 
        print("Updated data saved to the file.")

# Ejecutar el script
if __name__ == "__main__":
    soup = get_soup(URL)
    countries_data = extract_data(soup)
    save_data(countries_data, FILE_NAME)
    print(json.dumps(countries_data, indent=4, ensure_ascii=False))
