from requests import get, ConnectionError

params = {"ll": "36.511726,55.569949",
          "spn": "0.016457,0.00619","pt":"36.511726,55.569949",
          "l": "map"}
try:
    response = get("https://static-maps.yandex.ru/1.x/", params=params)
except ConnectionError:
    print("Проверка подключение к сети.")
else:
    with open("map.png", "wb") as file:
        file.write(response.content)

