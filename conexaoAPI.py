import requests

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json"
resposta = requests.get(url)
print(resposta.json())