from entities import Song
from service import Service, ServiceException

class UI:
    def __init__(self, service : Service):
        self.__service = service

    def __print_commands(self):
        print("1. Add song")
        print("2. Delete song")
        print("3. Average duration")
        print("4. Print all songs")
        print("5. Most popular genre")
        print("6. Exit")

    def run(self):
        while True:
            self.__print_commands()
            command_str = input()
            try:
                command = int(command_str)
                if command == 1:
                    self.__add_song()
                if command == 2:
                    self.__delete_song()
                if command == 3:
                    self.__get_avrage_duration()
                if command == 4:
                    self.__print_all_songs()
                if command == 5:
                    self.__print_most_popular_genre()
                if command == 6:
                    break
            except ValueError as ve:
                print(f"{command_str} is not a valid command. Try again with a different command")

            except ServiceException as se:
                print(se)

    def __add_song(self):
        song = self.__read_song()
        self.__service.add_song(song)

    def __read_song(self):
        title = input("title: ")
        artist = input("artist: ")
        genre = input("genre: ")
        duration = input("duration: ")

        return Song(title, artist, genre, duration)

    def __print_all_songs(self):
        play_list = self.__service.get_play_list()
        for song in play_list:
            print(song)

    def __delete_song(self):
        song = self.__read_song()
        self.__service.delete_song(song)

    def __get_avrage_duration(self):
        print(f"The avrage duration of the songs in {self.__service.avrage_duration()}.")

    def __print_most_popular_genre(self):
        print(f"The most popular genre is {self.__service.most_popular_genre()}.")
