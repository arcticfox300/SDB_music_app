class Song:
    def __init__(self, title, artist, genre, duration):
        self.__title = title
        self.__artist = artist
        self.__genre = genre
        self.__duration = duration

    def get_title(self):
        return self.__title

    def get_artist(self):
        return self.__artist

    def get_genre(self):
        return self.__genre

    def get_duration(self):
        return self.__duration

    def __str__(self):
        return f'name: {self.__title}, artist: {self.__artist}, genre: {self.__genre}, duration: {self.__duration}'

    def __eq__(self, other):
        return self.__title == other.get_title() and self.__artist == other.get_artist() and self.__genre == other.get_genre() and self.__duration == other.get_duration()

