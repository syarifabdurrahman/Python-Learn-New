import requests

SHEETY_ENDPOINT = 'https://api.sheety.co/9562493db98ab6f8b6b4abcd0949e5bf/flightDeals/prices'


class DataManager:
    def __init__(self) -> None:
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']

        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f'{SHEETY_ENDPOINT}/{city["id"]}', json=new_data)
            print(response.text)


if __name__ == '__main__':
    data_manager = DataManager()
    print(data_manager.get_destination_data())
