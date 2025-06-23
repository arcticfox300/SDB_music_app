from Domain.Song import Song
from Domain.exceptions import CustomExceptions
from Repository.Repository import Repository
from Service.MyUtilities import MyUtilities

class SongService:
    def __init__(self, song_repository : Repository):
        self.__song_repository = song_repository

    def add_song(self, new_song : Song):
        """
        This method adds a new song to the list
        :param new_song: the song to be added
        """
        self.__song_repository.add_entity(new_song)

    def delete_song(self, to_delete : Song):
        """
        This mothod delets a song from the list
        :param to_delete: the song to be deleted
        """
        self.__song_repository.delete_entity(to_delete)

    def avrage_duration(self):
        """
        This method finds the avrage duration of the songs in the list
        :return: the avrage duration of the songs in the list
        """
        return MyUtilities.average(self.__song_repository.get_all_entities())

    def get_play_list(self):
        """
        Returns the list of all the songs
        :return: the list of all the songs
        """
        return self.__song_repository.get_all_entities()

    def most_popular_genre(self):
        """
        Finds the most popular genre in the repository
        :return: the most popular genre
        """
        if len(self.__song_repository.get_all_entities()) == 0:
            raise CustomExceptions(f"The list of songs is empty.")

        genres = {}
        for index in range(len(self.__song_repository.get_all_entities())):
            genre = self.__song_repository.get_all_entities()[index].get_genre()
            if genre not in genres:
                genres[genre] = 1
            else:
                genres[genre] += 1

        maxx = 0
        most_frequent = ""
        for genre in genres:
            if genres[genre] > maxx:
                maxx = genres[genre]
                most_frequent = genre

        return most_frequent