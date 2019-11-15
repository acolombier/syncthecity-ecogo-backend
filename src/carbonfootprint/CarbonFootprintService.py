import requests
from config import TRIP_TO_CARBON_ENDPOINT
from enum import Enum


class ActivityType(Enum):
    miles: str = 1
    fuel: str = 2


class FuelType(Enum):
    motorGasoline: str = 1
    diesel: str = 2
    aviationGasoline: str = 3
    jetFuel: str = 4


class Mode(Enum):
    dieselCar: str = 1
    petrolCar: str = 2
    anyCar: str = 3
    taxi: str = 4
    economyFlight: str = 5
    businessFlight: str = 6
    firstclassFlight: str = 7
    anyFlight: str = 8
    motorbike: str = 9
    bus: str = 10
    transitRail: str = 11


class CarbonFootprintService:
    """
    A Service to retrieve the total carbon footprint value in kilograms
    """
    def __init__(self):
        self.url = TRIP_TO_CARBON_ENDPOINT
        self.steps = []

    def add_step(self, activity: str, activityType: ActivityType, **kwargs):
        fuelType: FuelType = kwargs.get('fuelType', None)
        mode: Mode = kwargs.get('mode', None)
        country: str = kwargs.get('country', 'gbr')
        query: str = f'?activity={activity}&activityType={activityType.name}'
        if fuelType:
            query = f'{query}&fuelType={fuelType.name}'

        if mode:
            query = f'{query}&mode={mode.name}'

        query = f'{query}&country={country}'
        self.steps.append(query)

    def calculate_journey(self) -> float:
        total: float = 0.0
        for query in self.steps:
            try:
                r = requests.get(f'{self.url}{query}')
                r.raise_for_status()
                data = r.json()
                total = total + float(data['carbonFootprint'])
            except Exception as e:
                print(f'Error retrieving carbon footprint information: {e}')

        return total
