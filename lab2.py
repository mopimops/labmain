import requests
city = "Moscow,RU"
appid = "3c211ea758fa910484bf5ccc4d69b593"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("____________________________\n","Дата <", i['dt_txt'], "> \r\nТемпература <",
'{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <",
i['weather'][0]['description'], ">","\r\nвидимость <",i['visibility'],' >','\r\nСкорость ветра <',i['wind']['speed'],' >')
print("____________________________")
