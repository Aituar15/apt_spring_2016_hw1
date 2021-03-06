from bottle import route, run, template
import requests
from bs4 import BeautifulSoup
import os 


@route('/')
def index():
	URL = "http://public.mig.kz/"
	resp = requests.get(URL)
	bs = BeautifulSoup(resp.content, "html.parser")
	usd = None
	eur = None
	rub = None
	for tag in bs.find_all('td'):
		if tag.has_attr('class') and 'currency':
			if tag.string == 'USD':
				temp = tag.parent.find('td', class_='buy')
				usd = temp.string
			if tag.string == 'EUR':
				temp = tag.parent.find('td', class_ = 'buy')
				eur = temp.string
			if tag.string == 'RUB':
				temp = tag.parent.find('td', class_ = 'buy')
				rub = temp.string
			

	return {"usd": usd, "eur": eur, "rub": rub}
    #return {"usd": 378, "eur": 415, "rub": 4.82}


URL = "https://github.com/giAtSDU/apt_spring_2016_hw1"

@route('/forks')
def forks():
    resp = requests.get(URL)
    bs4 = BeautifulSoup(resp.content, "html.parser")
    res = None
    for tag in bs4.find_all('a'):
        if tag.has_attr('class') and 'social-count' in tag.attrs['class']:
            res = int(tag.string)
    return {"forks": res}

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
