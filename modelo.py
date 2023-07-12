class Movie:
    def __init__(self, name: str, year:int , duration: float):
        self.__name = name.title()
        self.__year = year
        self.__duration = duration
        self.__likes = 0
    
    def like(self):
        self.__likes += 1

    @property
    def get_name(self):
        return self.__name

    @property
    def get_year(self):
        return self.__year

    @property
    def get_duration(self):
        return self.__duration

class TVShows:
    def __init__(self, name:str, year:int , seasons:int ):
        self.__name = name
        self.__year = year
        self.__seasons = seasons
        self.__likes = 0
    
    def like(self):
        self.__likes += 1

    @property
    def get_name(self):
        return self.__name.title()

    @property
    def get_year(self):
        return self.__year

    @property
    def get_seasons(self):
        return self.__seasons