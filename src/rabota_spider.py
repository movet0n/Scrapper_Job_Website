import pandas as pd
import requests
from bs4 import BeautifulSoup

from src.decorators import total_runtime


@total_runtime
def scrapper_rabota_ua(keyword):
    url_rabota_ua = f"https://rabota.ua/jobsearch/vacancy_list?keyWords={keyword}"
    r = requests.get(url_rabota_ua)

    if r.status_code == requests.codes.ok:
        print(f"Status code: {r.status_code}")

        soup = BeautifulSoup(r.content, "html.parser")
        positions = soup.find_all("article", class_="card")
        payload = {
            "title": [],
            "company": [],
            "location": [],
            "url": []
        }

        for position in positions:
            title = position.find("a", class_="ga_listing").get_text().strip()
            company = position.find("a", class_="company-profile-name").get_text().strip()
            location = position.find("span", class_="location").get_text().strip()
            url_local = position.find("a", class_="ga_listing").get("href")
            url = "https://rabota.ua" + url_local

            #  store data in the dictionary
            payload["title"].append(title)
            payload["company"].append(company)
            payload["location"].append(location)
            payload["url"].append(url)

        print(payload)

        # write scrapped data to the excel file
        table = pd.DataFrame(payload, columns=["title", "company", "location", "url"])
        table.index = table.index + 1
        print(table)
        table.to_excel("/home/alex/Projects/Scrapper/data/Test_scrapper_data.xlsx")

    else:
        print(f"Ooops, status code: {r.status_code}")


input_keyword = str(input("Enter position: "))

scrapper_rabota_ua(input_keyword)
