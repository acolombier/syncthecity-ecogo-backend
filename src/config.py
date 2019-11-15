import os

TRIP_TO_CARBON_ENDPOINT = os.environ.get(
    'TRIP_TO_CARBON_URL',
    'https://api.triptocarbon.xyz/v1/footprint'
)
