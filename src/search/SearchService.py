import math
from search.TflSearch import TflSearch
import data
from dateutil.parser import parse

from carbonfootprint.CarbonFootprintService import carbonSpecArgs

to_km = lambda a, o: (68.7 * a, 69 * math.cos(a) * o)

def compute_distance(step):
    laa, loa, lab, lob = step['departurePoint']['lat'], \
        step['departurePoint']['lon'], \
        step['arrivalPoint']['lat'], \
        step['arrivalPoint']['lon']

    (laa, loa), (lab, lob) = to_km(laa, loa), to_km(lab, lob)

    d = math.sqrt((laa - lab)**2 + (loa - lob)**2)
    return d


class SearchService:
    """
    Service to take a from lat lon and a to lat lon and return the steps needed to get to those
    locations including their carbon footprint
    """
    def __init__(self, carbonService):
        self.tfl_search = TflSearch()
        self.carbonService = carbonService

    def wrap(self, steps, best=False):
        estimation = self.carbonService()

        for m in steps:
            for s in m['steps']:
                s['distance'] = compute_distance(s)
                if s['type'] != "eurostar":
                    estimation.add_step(str(s['distance']), **carbonSpecArgs(s['type']))
                else:
                    estimation.add_static_step(s['distance'], 0.0018*1.6)

        return {
            "arrivalDateTime": steps[-1:][0]['arrivalDateTime'],
            "co2": estimation.calculate_journey(),
            "startCommonName": "Stratford, London",
            "arrivalCommonName": "PyParis 2019, Paris",
            "cost": sum([s.get('cost', 0) for s in steps]),
            "duration": (parse(steps[-1:][0]['arrivalDateTime']).replace(tzinfo=None) - parse(steps[0]['startDateTime']).replace(tzinfo=None)).total_seconds() / 60,
            "startDateTime": steps[0]['startDateTime'],
            "steps": steps
        }



    def search(self, fromLat: float, fromLon: float, toLat: float, toLon):
        """
        Search for potential journey options
        """
        airport, train, coach = self.tfl_search.search(fromLat, fromLon, toLat, toLon)

        for r in (airport, train, coach):
            r["type"] = "localPublicTransport"

        airport, train, coach = [airport, *data.airline.generate(airport["arrivalDateTime"])], \
                                [train, *data.eurostar.generate(train["arrivalDateTime"])], \
                                [coach, *data.coach.generate(coach["arrivalDateTime"])]

        return [self.wrap(airport), self.wrap(train), self.wrap(coach)]
        
        