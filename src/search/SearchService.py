from search.TflSearch import TflSearch


class SearchService:
    """
    Service to take a from lat lon and a to lat lon and return the steps needed to get to those
    locations including their carbon footprint
    """
    def __init__(self):
        self.tfl_search = TflSearch()

    def search(self, fromLat: float, fromLon: float, toLat: float, toLon):
        """
        Search for potential journey options
        """
        return self.tfl_search.search(fromLat, fromLon, toLat, toLon)
        
        