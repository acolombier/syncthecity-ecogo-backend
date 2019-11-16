import requests
from config import TFL_ENDPOINT, TFL_APP_ID, TFL_APP_KEY



FIXED_POINTS = {
    'plane': [51.4700223, -0.4564842], # Heathrow
    'eurostar': [51.5316991, -0.1258251], # St Pancras
    'coach': [51.4952103, -0.1460866] # Victoria
}


class TflSearch:
    """
    Class for being able to search through the different TFL journeys available
    """
    AREA = (51.4745, -0.1346)
    RADIUS = (0.018, 0.35)

    def __init__(self):
        self.url = TFL_ENDPOINT
        self.app_id = TFL_APP_ID
        self.app_key = TFL_APP_KEY
        self.client_querystring = f'?app_id={self.app_id}&app_key={self.app_key}'

    def search(self, fromLat: float, fromLon: float, toLat: float, toLon: float):
        r = requests.Session()
        try:
            # Get to plane
            plane_r = r.get(f'{self.url}{str(fromLat)},{str(fromLon)}/to/{str(FIXED_POINTS["plane"][0])},{str(FIXED_POINTS["plane"][1])}{self.client_querystring}')
            plane_r.raise_for_status()
            plane_data = self.retrieve_train_steps(plane_r.json())
        except Exception as e:
            print(f'Unable to retrieve distance to plance {e}')

        try:
            # Get to train
            train_r = requests.get(f'{self.url}{str(fromLat)},{str(fromLon)}/to/{str(FIXED_POINTS["eurostar"][0])},{str(FIXED_POINTS["eurostar"][1])}{self.client_querystring}')
            train_r.raise_for_status()
            train_data = self.retrieve_train_steps(train_r.json())
        except Exception as e:
            print(f'Unable to retrieve distance to train {e}')

        try:
            coach_r = requests.get(f'{self.url}{str(fromLat)},{str(fromLon)}/to/{str(FIXED_POINTS["coach"][0])},{str(FIXED_POINTS["coach"][1])}{self.client_querystring}')
            coach_r.raise_for_status()
            coach_data = self.retrieve_train_steps(coach_r.json())
        except Exception as e:
            print(f'Unable to retrieve distance to coach {e}')

        return plane_data, train_data, coach_data

    def retrieve_train_steps(self, tfl_data):
        instructions = {
            'steps': []
        }
        journey = tfl_data['journeys'][0]
        for leg in journey['legs']:
            if leg['mode']['name'] != 'walking':
                instructions['steps'].append({
                    'departurePoint': {k:v for k, v in leg['departurePoint'].items() if k != "$type"},
                    'arrivalPoint': {k:v for k, v in leg['arrivalPoint'].items() if k != "$type"},
                    'type': "bus"
                })
        instructions['duration'] = journey['duration']
        instructions['startDateTime'] = journey['startDateTime']
        instructions['arrivalDateTime'] = journey['arrivalDateTime']

        if 'fare' in journey:
            instructions['cost'] = journey['fare']['totalCost']
        return instructions
