import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("detik_scrapping.html")


@app.route('/detik-populer')
def detik_populer():
    url = requests.get("https://www.detik.com/terpopuler", params={"tag_from": "wp_cb_mostPopular_more"})
    soup = BeautifulSoup(url.text, "html.parser")
    popular_area = soup.find(attrs={"class": "grid-row list-content"})
    titles = popular_area.find_all(attrs={"class": "media__title"})
    images = popular_area.find_all(attrs={"class": "media__image"})

    return render_template("detik_scrapping.html", images=images)

@app.route('/idr-currency')
def idr_currency():
    url = requests.get("http://www.floatrates.com/daily/idr.json")
    json_data = url.json()
    return render_template("idr_currency.html", datas=json_data.values())


if __name__ == "__main__":
    app.run(debug=True)
