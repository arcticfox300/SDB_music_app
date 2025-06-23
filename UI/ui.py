from Service.MyUtilities import MyUtilities
from Domain.Listener import Listener
from Domain.Song import Song
from Service.MyUtilities import MyUtilities
from Service.SongService import SongService
from Service.ListenerService import ListenerService
from Domain.exceptions import CustomExceptions
from Service.StatisticsService import StatisticsService


class UI:
    def __init__(self, song_service : SongService, listener_service : ListenerService, statistics_service : StatisticsService):
        self.__song_service = song_service
        self.__listener_service = listener_service
        self.__statistics_service = statistics_service
        self.__commands = {
            "1": self.__add_song,
            "2": self.__add_listener,
            "3": self.__delete_song,
            "4": self.__delete_listener,
            "5": self.__get_avrage_duration,
            "6": self.__get_avrage_age,
            "7": self.__print_all_songs,
            "8": self.__print_all_listeners,
            "9": self.__print_most_popular_genre,
            "10": self.__print_songs_without_listener,
        }

    def __print_commands(self):
        print("0. Exit")
        print("1. Add song")
        print("2. Add listener")
        print("3. Delete song")
        print("4. Delete listener")
        print("5. Average duration")
        print("6. Average listener age")
        print("7. Print all songs")
        print("8. Print all listeners")
        print("9. Most popular genre")
        print("10. Songs without listeners")

    def run(self):
        while True:
            self.__print_commands()
            command = input()
            try:
                if command == "0":
                    return
                if command in self.__commands:
                    self.__commands[command]()
                else:
                    print(f"{command} is not a valid command. Try again with a different command.")
            except ValueError as ve:
                print(f"{command} is not a valid command. Try again with a different command")

            except CustomExceptions as se:
                print(se)

    def __add_song(self):
        song = self.__read_song()
        self.__song_service.add_song(song)

    def __read_song(self):
        title = input("title: ")
        artist = input("artist: ")
        genre = input("genre: ")
        duration = input("duration: ")

        return Song(title, artist, genre, duration)

    def __add_listener(self):
        listener = self.__read_listener()
        self.__listener_service.add_listener(listener)

    def __valid_song_title(self, song_title):
        song_list = self.__song_service.get_play_list()
        for song in song_list:
            if song.get_title() == song_title:
                return True
        return False

    def __read_listener(self):
        name = input("name: ")
        age = input("age: ")
        song_title = input("song title: ")

        if self.__valid_song_title(song_title):
            return Listener(name, age, song_title)
        raise CustomExceptions(f"This song does not exist in the list.")

    def __print_all_listeners(self):
        MyUtilities.print_array(self.__listener_service.get_all_listeners())

    def __print_all_songs(self):
        MyUtilities.print_array(self.__song_service.get_play_list())

    def __delete_song(self):
        song = self.__read_song()
        self.__song_service.delete_song(song)

    def __delete_listener(self):
        listener = self.__read_listener()
        self.__listener_service.delete_listener(listener)

    def __get_avrage_duration(self):
        print(f"The avrage duration of the songs in {self.__song_service.avrage_duration()}.")

    def __get_avrage_age(self):
        print(f"The avrage age of the listeners is {self.__listener_service.avrage_age()}.")

    def __print_most_popular_genre(self):
        print(f"The most popular genre is {self.__song_service.most_popular_genre()}.")

    def __print_songs_without_listener(self):
        no_listener_list = self.__statistics_service.get_song_without_listeners()
        MyUtilities.print_array(no_listener_list)
