import os

TRIP_TO_CARBON_ENDPOINT = os.environ.get(
    'TRIP_TO_CARBON_URL',
    'https://api.triptocarbon.xyz/v1/footprint'
)

TFL_ENDPOINT = os.environ.get('TFL_ENDPOINT', 'https://api.tfl.gov.uk/journey/journeyresults/')
TFL_APP_ID = os.environ.get('TFL_APP_ID', '38a27002')
TFL_APP_KEY = os.environ.get('TFL_APP_KEY', '33bc54d78628e7522f0345e08ba3936b')