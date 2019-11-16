from datetime import datetime, timedelta
from dateutil.parser import parse


def generate(_from):
    from_time = parse(_from) + timedelta(minutes=15)
    to_time = from_time + timedelta(hours=8, minutes=25)
    from_time_ratp = to_time + timedelta(minutes=20)
    to_time_ratp = from_time_ratp + timedelta(minutes=36)

    return  {
        "arrivalDateTime": to_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "cost": 8599,
        "duration": 8 * 60 + 10,
        "startDateTime": from_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": "intercountryCoach",
        "steps": [
            {
                "departurePoint": {
                    "additionalProperties": [],
                    "commonName": "London Victoria",
                    "icsCode": "1000129",
                    "lat": 51.4952103,
                    "lon": -0.1460866,
                    "naptanId": "940GZZLUKSX",
                    "placeType": "StopPoint",
                    "platformName": ""
                },
                "arrivalPoint": {
                    "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                    "additionalProperties": [],
                    "commonName": "Paris (Bercy Seine)",
                    "icsCode": "1000138",
                    "lat": 48.79955,
                    "lon": 2.38102,
                    "naptanId": "940GZZLULVT",
                    "placeType": "StopPoint",
                    "platformName": ""
                },
                "type": "coach"
            }
        ]
    },{
       "arrivalDateTime": to_time_ratp.strftime("%Y-%m-%dT%H:%M:%SZ"),
       "cost": 240,
       "duration": 36,
       "startDateTime": from_time_ratp.strftime("%Y-%m-%dT%H:%M:%SZ"),
       "type": "localPublicTransport",
       "steps": [
           {
               "departurePoint": {
                   "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                   "additionalProperties": [],
                   "commonName": "Bercy",
                   "icsCode": "1000138",
                   "lat": 48.8353,
                   "lon": 2.3854,
                   "naptanId": "940GZZLULVT",
                   "placeType": "StopPoint",
                   "platformName": ""
               },
               "arrivalPoint": {
                   "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                   "additionalProperties": [],
                   "commonName": "Place d'Italie",
                   "icsCode": "1000138",
                   "lat": 48.8309,
                   "lon": 2.3559,
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
                   "lat": 48.8309,
                   "lon": 2.3559,
                   "naptanId": "940GZZLUKSX",
                   "placeType": "StopPoint",
                   "platformName": ""
               },
               "arrivalPoint": {
                   "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                   "additionalProperties": [],
                   "commonName": "Porte d'Italie",
                   "icsCode": "1000138",
                   "lat": 48.8167,
                   "lon": 2.3640,
                   "naptanId": "940GZZLULVT",
                   "placeType": "StopPoint",
                   "platformName": ""
               },
                "type": "bus"
           }
       ]
   }
