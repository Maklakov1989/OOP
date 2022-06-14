<<<<<<< HEAD
import requests
import json
origin = input("Вы хотите вылететь из:")
destination = input("Введите город прибытия:")
link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"+origin+"%20в%20"+destination
text = requests.get(link).text
data = json.loads(text)
iata_origin = data["origin"]["iata"]
iata_destination = data['destination']['iata']
print(f'IATA код {origin} -', iata_origin)
print(f'IATA код {destination} -', iata_destination)

=======
import requests
import json
origin = input("Вы хотите вылететь из:")
destination = input("Введите город прибытия:")
link = "https://www.travelpayouts.com/widgets_suggest_params?q=Из%20"+origin+"%20в%20"+destination
text = requests.get(link).text
data = json.loads(text)
iata_origin = data["origin"]["iata"]
iata_destination = data['destination']['iata']
print(f'IATA код {origin} -', iata_origin)
print(f'IATA код {destination} -', iata_destination)

>>>>>>> OOP/master
