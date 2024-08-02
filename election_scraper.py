"""
election_scraper.py: třetí projekt do Engeto Online Python Akademie
autor: Daniel Šadibol
email: sadibol.daniel@gmail.com
discord: dzonsnou. 512617534952833034
"""

import csv
import sys
import traceback
import requests
from bs4 import BeautifulSoup


def main() -> None:
    """
    Hlavní funkce skriptu.
    """
    check_arguments()
    url = sys.argv[1]
    file_name = sys.argv[2]
    scrape_election_results(url, file_name)


def scrape_election_results(url: str, file_name: str) -> None:
    """
    Tato funkce provádí web scraping a zpracování výsledků voleb.
    """
    soup = get_page_content(url)
    municipalities = extract_municipalities(soup)
    results = get_results(get_links(soup))

    for i in range(len(municipalities)):
        municipalities[i].update(results[i])
    save_to_csv(municipalities, file_name)


def check_arguments():
    """
    Tato funkce kontroluje, zda jsou poskytnuty správné argumenty pro spuštění programu.
    """
    if len(sys.argv) != 3:
        print(f"Skript: {sys.argv[0]} potřebuje 2 argumenty pro spuštění. Končím ...")
        exit()
    elif not sys.argv[1].startswith("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj="):
        print(f"Argument jedna {sys.argv[1]} není správný! Končím ...")
        exit()
    elif not sys.argv[2].endswith(".csv"):
        print(f"Skript: {sys.argv[2]} není CSV soubor! Končím ...")
        exit()
    else:
        print(f'Stahuji data z vybraného URL: {sys.argv[1]}')


def get_page_content(url: str):
    """
    Tato funkce získává obsah webové stránky.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
    }
    page = requests.get(url, headers=headers)
    return BeautifulSoup(page.content, 'html.parser')


def extract_municipalities(soup: 'BeautifulSoup') -> list:
    """
    Tato funkce extrahuje obce ze stránky.
    """
    municipalities = []
    for row in soup.select('tr', headers="t1sa1 t1sb2"):
        row = list(row.stripped_strings)
        if row[0].isnumeric():
            municipality = {'Kód': row[0], 'Obec': row[1]}
            municipalities.append(municipality)
        else:
            continue
    return municipalities


def get_links(soup: 'BeautifulSoup') -> list:
    """
    Tato funkce vytváří seznam odkazů.
    """
    links = [link.get('href') for link in soup.select('table a', href=True)]

    select_links = []

    for x in links:
        link = "https://www.volby.cz/pls/ps2017nss/" + x
        if len(link) < 80:
            continue
        elif link in select_links:
            continue
        else:
            select_links.append(link)

    return select_links


def get_results(select_links: list) -> list:
    """
    Tato funkce vrací seznam stran s jejich výsledky.
    """
    results = []
    for link in select_links:
        page = requests.get(link)
        link_soup = BeautifulSoup(page.content, 'html.parser')
        table_tag = link_soup.find("div", {"class": "topline"})
        td_tag = table_tag.find_all("td")

        result = {}
        for i in td_tag:
            g = len(td_tag)
            if td_tag.index(i) in range(g - (g - 10), g - 4, 5):
                result[td_tag[td_tag.index(i)].get_text()] = td_tag[td_tag.index(i) + 1].get_text()
            elif td_tag.index(i) == 3:
                result["Voliči v seznamu"] = td_tag[3].get_text()
            elif td_tag.index(i) == 4:
                result["Vydané obálky"] = td_tag[4].get_text()
            elif td_tag.index(i) == 7:
                result["Platné hlasy"] = td_tag[7].get_text()
            else:
                continue
        results.append(result)
    return results


def save_to_csv(data: list, file_name: str) -> None:
    """
    Uloží data (parametr 'data') do určeného souboru (parametr 'file_name').
    """
    with open(file_name, mode="w", newline='', encoding="utf-8") as csv_file:
        try:
            columns = data[0].keys()
        except FileExistsError:
            return traceback.format_exc()
        else:
            print(f'Ukládám do souboru: {sys.argv[2]}')
            writer = csv.DictWriter(csv_file, fieldnames=columns, extrasaction='ignore')
            writer.writeheader()
            for element in data:
                writer.writerow(element)
        finally:
            print(f'Končím election-scraper')
            csv_file.close()


if __name__ == "__main__":
    main()
