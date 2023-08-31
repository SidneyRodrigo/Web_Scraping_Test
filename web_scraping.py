import csv 
import requests
from bs4 import BeautifulSoup

# URL of the page we want to scrape
url = "https://www.imdb.com/chart/top/"

# User-Agent header to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

# Making a GET request to the URL
response = requests.get(url, headers=headers)

# Checking if the request was successful (status 200)
if response.status_code == 200:
    # Parsing the page with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Finding HTML elements that contain movie details
    imdbs = soup.find_all("div", class_="sc-b85248f1-0 bCmTgE cli-children")
    
    # Creating a CSV file
    file = open('export_data.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    headers = ['Movie Title', 'Production Year', 'Movie Rating']
    writer.writerow(headers)
    
    # Looping through the elements and extracting information
    for imdb in imdbs:
        # Extracting the movie title
        title = imdb.find("h3", class_="ipc-title__text").text.strip()
        
        # Extracting the production year of the movie
        year = imdb.find("span", class_="sc-b85248f1-6 bnDqKN cli-title-metadata-item").text.strip()
                
        # Extracting the movie rating
        stars = imdb.find("span", class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text.strip()
        
        # Writing the information to the CSV file
        row = [title, year, stars]
        writer.writerow(row)
        
    file.close()
    print("Data exported to export_data.csv.")

else:
    print("Failed to access the page:", response.status_code)
