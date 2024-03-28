import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus
from pathlib import Path

def get_websites(csv_path: str) -> list[str]:
    websites = []
    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            website = row[1].strip()
            if "https://" not in website:
                websites.append(f"https://{website}")
            else:
                websites.append(website)
    return websites

def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome

def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value.value == status_code:
            description = f"({value.value} {value.name}) {value.description}"
            return description
    return "Status unbekannt"

def check_website(website: str, user_agent: str):
    try:
        response = requests.get(website, headers={'User-Agent': user_agent})
        print(website, get_status_description(response.status_code))
    except Exception as e:
        print(f"Keine Information zur Webseite: {website}. Fehler: {e}")

def main():
    csv_path = Path("test_websites.csv")
    sites = get_websites(csv_path)
    user_agent = get_user_agent()

    for site in sites:
        check_website(site, user_agent)

if __name__ == "__main__":
    main()
