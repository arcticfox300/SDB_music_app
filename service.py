from entities import Song

class ServiceException(Exception):
    pass

class Service:
    def __init__(self):
        self.__play_list = []

    def add_song(self, new_song : Song):
        """
        This method adds a new song to the list
        :param new_song: the song to be added
        """
        for song in self.__play_list:
            if song == new_song:
                raise ServiceException(f"The song {new_song.get_title()} has already been added.")
        self.__play_list.append(new_song)

    def delete_song(self, to_delete : Song):
        """
        This mothod delets a song from the list
        :param to_delete: the song to be deleted
        """
        for song in self.__play_list:
            if song == to_delete:
                self.__play_list.remove(to_delete)
                return
        raise ServiceException(f"The song {to_delete.get_artist()} does not exist.")

    def avrage_duration(self):
        """
        This method finds the avrage duration of the songs in the list
        :return: the avrage duration of the songs in the list
        """
        sum = 0
        count = 0

        for index in range(len(self.__play_list)):
            track = self.__play_list[index]
            count += 1
            sum += int(track.get_duration())

        return sum / count

    def get_play_list(self):
        """
        Returns the list of all the songs
        :return: the list of all the songs
        """
        return self.__play_list

    def most_popular_genre(self):
        genres = {}
        for index in range(len(self.__play_list)):
            genre = self.__play_list[index].get_genre()
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