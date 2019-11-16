from datetime import timedelta

from dateutil.parser import parse


def generate(_from):
    from_time_eurostar = parse(_from) + timedelta(minutes=30)
    to_time_eurostar = from_time_eurostar + timedelta(minutes=150)
    from_time_ratp = to_time_eurostar + timedelta(minutes=20)
    to_time_ratp = from_time_ratp + timedelta(minutes=36)

    return {
               "arrivalDateTime": to_time_eurostar.strftime("%Y-%m-%dT%H:%M:%SZ"),
               "cost": 10000,
               "duration": 150,
               "startDateTime": from_time_eurostar.strftime("%Y-%m-%dT%H:%M:%SZ"),
               "type": "intercountryTrain",
               "steps": [
                   {
                       "departurePoint": {
                           "additionalProperties": [],
                           "commonName": "King's Cross St. Pancras Underground Station",
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
                           "commonName": "Paris Gare du Nord",
                           "icsCode": "1000138",
                           "lat": 48.8814,
                           "lon": 2.3575,
                           "naptanId": "940GZZLULVT",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "type": "eurostar"
                   }
               ]
           }, {
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
                           "commonName": "Paris Gare du Nord",
                           "icsCode": "1000138",
                           "lat": 48.8814,
                           "lon": 2.3575,
                           "naptanId": "940GZZLULVT",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "arrivalPoint": {
                           "$type": "Tfl.Api.Presentation.Entities.StopPoint, Tfl.Api.Presentation.Entities",
                           "additionalProperties": [],
                           "commonName": "Cité Universitaire",
                           "icsCode": "1000138",
                           "lat": 48.8214,
                           "lon": 2.3342,
                           "naptanId": "940GZZLULVT",
                           "placeType": "StopPoint",
                           "platformName": ""
                       },
                       "type": "bus"
                   },
                   {
                       "departurePoint": {
                           "additionalProperties": [],
                           "commonName": "Cité Universitaire",
                           "icsCode": "1000138",
                           "lat": 48.8214,
                           "lon": 2.3342,
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
