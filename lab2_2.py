import requests
city = "Moscow,RU"
appid = "3c211ea758fa910484bf5ccc4d69b593"
res=requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print('Видимость',data['visibility'])
print('Скорость ветра',data['wind']['speed'])