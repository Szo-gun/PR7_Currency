import requests
import csv
import os
from flask import Flask, render_template, request

#Otwórz api na stronie
response = requests.get("https://api.nbp.pl/api/exchangerates/tables/c/?format=json")
currency_list = response.json()[0]['rates']

#Otwórz nowy plik do zapisu
f = open(f'C:\\Users\\Piotr.Cianciara\\Desktop\\Python-Kodilla\\Flask\\6\\dane_nowe.csv', 'w', encoding="utf-8", newline='')
writer = csv.writer(f)
header_placed = False

#Zapisz dane z api
for currency_element in currency_list:
    w = csv.DictWriter(f, currency_element.keys())
    if not header_placed:
        w.writeheader()
        header_placed = True
    w.writerow(currency_element)
f.close()

#Otwórz zapisany plik
with open(f'C:\\Users\\Piotr.Cianciara\\Desktop\\Python-Kodilla\\Flask\\6\\dane_nowe.csv', encoding="utf-8", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
#print(data)

#Wyszukaj po kodzie
finded = []
sz = []
for i in data:
    if(i[1] == "USD"):
        finded = i
        value = (i[3])
        break
#print(i[0])
#print(value)

app = Flask(__name__)

@app.route('/test',methods = ['GET'])
def show_index_html():
    return render_template('waluty.html')

@app.route('/test', methods = ['POST'])
def get_data_from_html():
        ile = request.form['ilosc']
        waluta = request.form['waluta']
        print(f"Wybrana waluta: {waluta}")
        print (f"Wybrana ilosc:  {ile}")
        for i in data:
            if (i[1] == waluta):
                kurs = (i[3])
                print(kurs)
        ile_int = int(ile)        
        kurs_float = float(kurs)
        wartosc = ile_int * kurs_float
        wynik = round(wartosc , 2)
        print(wynik)
        return render_template("waluty.html", wynik=wynik, waluta=waluta,ile=ile)

        


if __name__ == '__main__':
    app.run(debug=True) 