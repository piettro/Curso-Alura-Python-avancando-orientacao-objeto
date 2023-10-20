class Programa:
    def __init__(self, name: str, year:int ):
        self._name = name.title()
        self._year = year
        self._likes = 0
    
    def like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, new_year):
        self._year = new_year

class Movie(Programa):
    def __init__(self,  duration: float, name: str, year:int):
        super().__init__(name, year)
        self._duration = duration
        
    @property
    def get_duration(self):
        return self._duration

class TVShows(Programa):
    def __init__(self, seasons:int, name: str, year:int):
        super().__init__(name, year)
        self._seasons = seasons

    @property
    def get_seasons(self):
        return self._seasons