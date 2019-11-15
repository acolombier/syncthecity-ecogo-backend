import requests
from config import TRIP_TO_CARBON_ENDPOINT
from enum import Enum


class ActivityType(Enum):
    miles = 1
    fuel = 2


class FuelType(Enum):
    motorGasoline = 1
    diesel = 2
    aviationGasoline = 3
    jetFuel = 4


class Mode(Enum):
    dieselCar = 1
    petrolCar = 2
    anyCar = 3
    taxi = 4
    economyFlight = 5
    businessFlight = 6
    firstclassFlight = 7
    anyFlight = 8
    motorbike = 9
    bus = 10
    transitRail = 11


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
