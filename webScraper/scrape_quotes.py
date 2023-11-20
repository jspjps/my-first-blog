# Module importieren
import requests
import csv
from bs4 import BeautifulSoup

# Adresse der Webseite
url = "http://quotes.toscrape.com/"

# GET-Request ausführen
response = requests.get(url)

# BeautifulSoup HTML-Dokument aus dem Quelltext parsen
html = BeautifulSoup(response.text, 'html.parser')

# Alle Zitate und Autoren aus dem HTML-Dokument extrahieren
quotes_html = html.find_all('span', class_="text")
authors_html = html.find_all('small', class_="author")

# Die Zitate in einer Liste sammeln
quotes = list()
for quote in quotes_html:
    quotes.append(quote.text)

# Die Autoren in einer Liste sammelnls
authors = list()
for author in authors_html:
    authors.append(author.text) 

# Zum Testen: Einträge beiden Listen kombinieren und ausgeben
for t in zip(quotes, authors):
    print(t)

# Die Zitate und Autoren in einer CSV-Datei im aktuellen Verzeichnis speichern
# Öffnen Sie die Datei mit Excel / LibreOffice, etc.
with open('./zitate.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))
