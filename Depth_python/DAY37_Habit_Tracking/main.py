import requests
from datetime import datetime

# # Get
# requests.get()

# # Post
# requests.post()

# # Put
# requests.put()

# # Delete
# requests.delete()

TOKEN = 'asdaf342fdsfsvxvfgd9094'
USERNAME = 'syarif'
GRAPH_ID = 'graph1'

pixela_enpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_enpoint, json=user_params)
# print(response.text)


graph_endpoint = f'{pixela_enpoint}/{USERNAME}/graphs'

graph_configuration = {
    'id': GRAPH_ID,
    'name': 'Coding Graph',
    'unit': 'minute',
    'type': 'float',
    'color': 'sora'
}

header = {
    'X-USER-TOKEN': TOKEN
}

# Create graphs
# response = requests.post(
#     url=graph_endpoint, json=graph_configuration, headers=header)

# print(response.text)

# Create Pixel
# now = datetime.now()
# date_time = now.strftime("%Y%m%d")
# print(date_time)

# pixel_config = {
#     'date': date_time,
#     'quantity': '45'
# }
# response = requests.post(
#     f'{pixela_enpoint}/{USERNAME}/graphs/{GRAPH_ID}', json=pixel_config, headers=header)
# print(response.text)

# Update pixel

# pixel_config = {
#     'quantity': '186'
# }

# response = requests.put(
#     f'{pixela_enpoint}/{USERNAME}/graphs/{GRAPH_ID}/20221127', json=pixel_config, headers=header)
# print(response.text)

# Delete
response = requests.delete(
    f'{pixela_enpoint}/{USERNAME}/graphs/{GRAPH_ID}/20221127', headers=header)
print(response.text)
