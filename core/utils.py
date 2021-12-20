import requests

from bs4 import BeautifulSoup


# getting horoscope by day
def get_horoscope_by_day(zodiac_sign, day:str):
    if not "-" in day:
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}")
    else:
        day = day.replace("-", "")
        res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs = {'class':'main-horoscope'})
    return data.p.text

# getting horoscope for a week
def get_horoscope_by_week(zodiac_sign: int):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-weekly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class':'main-horoscope'})
    return data.p.text

#getting horoscope by month
def get_horoscope_by_month(zodiac_sign:int):
    res = requests.get(f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class':'main-horoscope'})
    return data.p.text

