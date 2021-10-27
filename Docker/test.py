from json import decoder
import requests
import json

opa = requests.get('http://localhost:5555/images/json')

fim = list()

for image in json.loads(opa.content):
    fim.append(dict(image = image['RepoTags'][0], id = image['Id']))

print(fim)

# archive = open('text.txt', 'w')
# archive.write(str(opa.content))
# archive.close()