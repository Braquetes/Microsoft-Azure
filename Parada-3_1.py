# import requests

# import matplotlib.pyplot as plt
# import matplotlib.image as img

# pokemon = input("Introduce el nombre de un pokemón: ")
# url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
# res = requests.get(url)

# if res.status_code != 200: 
#     print("Pokemón no encontrado")
#     exit()

# image  = img.imread(res.json()['sprites']['clsfront_default'])
# plt.title(res.json()['name'])
# imgplot = plt.imshow(image)
# plt.show()

import requests
from PIL import Image
import matplotlib.pyplot as plt

url = "https://integradora.ml/API-solteca/sucursales.php"
res = requests.get(url)

if res.status_code != 200:
    print("No encontrado")
    exit()

img = Image.open(requests.get(res.json()[0]['Director'], stream=True).raw)
plt.title(res.json()[0]['Nombre'])
imgplot = plt.imshow(img)
plt.show()