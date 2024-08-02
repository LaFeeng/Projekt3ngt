
# Election Scraper

Třetí projekt do Engeto Online Python Akademie.

## Autor

- **Daniel Šadibol**
- **Email:** sadibol.daniel@gmail.com
- **Discord:** dzonsnou. 512617534952833034

## Popis

Tento projekt slouží k webovému scrappingu výsledků voleb z roku 2017. Skript načte data z webové stránky a uloží je do CSV souboru. 

## Požadavky

Projekt používá následující knihovny:

- beautifulsoup4==4.12.3
- soupsieve==2.5
- pip==24.2
- wheel==0.41.2
- certifi==2023.5.7
- idna==3.4
- setuptools==68.0.0
- requests==2.31.0
- urllib3==2.0.4

## Instalace

1. Vytvořte virtuální prostředí:
   ```sh
   python -m venv venv
   ```

2. Aktivujte virtuální prostředí:
   - **Windows:**
     ```sh
     venv\Scripts\activate
     ```
   - **MacOS/Linux:**
     ```sh
     source venv/bin/activate
     ```

3. Nainstalujte požadované balíčky:
   ```sh
   pip install -r requirements.txt
   ```

## Použití

Pro spuštění skriptu použijte následující příkaz:

```sh
python election_scraper.py "<URL>" <vysledny_soubor.csv>
```

Příklad:

```sh
python election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv
```

## Výstup

Skript vygeneruje CSV soubor, který obsahuje následující informace pro každou obec:

- Kód obce
- Název obce
- Voliči v seznamu
- Vydané obálky
- Platné hlasy
- Počet hlasů pro jednotlivé strany (každá strana má svůj sloupec)

## Struktura projektu

- `election_scraper.py`: Hlavní skript pro scrapování výsledků voleb.
- `requirements.txt`: Seznam požadovaných knihoven.
- `README.md`: Tento soubor s instrukcemi.

## Ukončení

Po úspěšném spuštění skriptu a vygenerování CSV souboru můžete ukončit virtuální prostředí příkazem:

```sh
deactivate
```

Pokud máte jakékoliv dotazy nebo problémy, neváhejte mě kontaktovat na uvedeném emailu nebo Discordu.

---

**Poznámka:** Ujistěte se, že máte přístup k internetu, aby mohl skript načíst potřebná data z webové stránky.
