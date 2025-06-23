class Listener:
    def __init__(self, name, age, song_title):
        self.__name = name
        self.__age = age
        self.__song_title = song_title

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_song_title(self):
        return self.__song_title

    def __str__(self):
        return f'name {self.__name}, age {self.__age}, song title {self.__song_title}'

    def __eq__(self, other):
        return self.__name == other.get_name() and self.__age == other.get_age() and self.__song_title == other.get_song_title()

    def __repr__(self):
        return str(self)