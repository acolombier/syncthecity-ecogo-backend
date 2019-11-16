from datetime import timedelta

from dateutil.parser import parse


def generate(_from):
    from_time = parse(_from) + timedelta(hours=2)
    to_time = from_time + timedelta(hours=2, minutes=30)

    from_time_ac = to_time + timedelta(hours=1)
    to_time_ac = from_time_ac + timedelta(minutes=37)

    from_time_ratp = to_time_ac + timedelta(minutes=20)
    to_time_ratp = from_time_ratp + timedelta(minutes=37)

    return {
               "arrivalDateTime": to_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
               "cost": 65000,
               "duration": 75,
               "startDateTime": from_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
               "type": "intercountryAirplane",
               "steps": [
                   {
                       "departurePoint": {
                           "additionalProperties": [],
                           "commonName": "London Heathrow",
                           "icsCode": "1000129",
                           "lat": 51.52990049989,
                           "lon": -0.12398997808000001,
                           "naptanId": "940GZZLUKSX",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "arrivalPoint": {
                           "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                           "additionalProperties": [],
                           "commonName": "Paris Charles de Gaulle",
                           "icsCode": "1000138",
                           "lat": 48.8814,
                           "lon": 2.3575,
                           "naptanId": "940GZZLULVT",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "type": "plane"
                   }
               ]
           }, {
               "arrivalDateTime": to_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
               "cost": 18000,
               "duration": 60,
               "startDateTime": from_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
               "type": "airportConnection",
               "steps": [
                   {
                       "departurePoint": {
                           "additionalProperties": [],
                           "commonName": "Paris Charles de Gaulle",
                           "icsCode": "1000129",
                           "lat": 49.0063,
                           "lon": 2.5708,
                           "naptanId": "940GZZLUKSX",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "arrivalPoint": {
                           "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                           "additionalProperties": [],
                           "commonName": "Bir-Hakeim (Grenelle)",
                           "icsCode": "1000138",
                           "lat": 48.85389,
                           "lon": 2.28936,
                           "naptanId": "940GZZLULVT",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "type": "coach"
                   }
               ]
           }, {
               "arrivalDateTime": to_time_ratp.strftime("%Y-%m-%dT%H:%M:%SZ"),
               "cost": 240,
               "duration": 37,
               "startDateTime": from_time_ratp.strftime("%Y-%m-%dT%H:%M:%SZ"),
               "type": "localPublicTransport",
               "steps": [
                   {
                       "departurePoint": {
                           "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                           "additionalProperties": [],
                           "commonName": "Bir-Hakeim (Grenelle)",
                           "icsCode": "1000138",
                           "lat": 48.85389,
                           "lon": 2.28936,
                           "naptanId": "940GZZLULVT",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "arrivalPoint": {
                           "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                           "additionalProperties": [],
                           "commonName": "Place d'Italie",
                           "icsCode": "1000138",
                           "lat": 48.83088,
                           "lon": 2.35589,
                           "naptanId": "940GZZLULVT",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "type": "bus"
                   },
                   {
                       "departurePoint": {
                           "additionalProperties": [],
                           "commonName": "Place d'Italie",
                           "icsCode": "1000138",
                           "lat": 48.83088,
                           "lon": 2.35589,
                           "naptanId": "940GZZLUKSX",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "arrivalPoint": {
                           "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                           "additionalProperties": [],
                           "commonName": "ROGER SALENGRO - FONTAINEBLEAU",
                           "icsCode": "1000138",
                           "lat": 48.81490,
                           "lon": 2.36064,
                           "naptanId": "940GZZLULVT",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "type": "bus"
                   }
               ]
           }
