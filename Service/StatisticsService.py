from Repository.Repository import Repository


class StatisticsService:
    def __init__(self, song_repository : Repository, listener_repository : Repository):
        self.__song_repository = song_repository
        self.__listener_repository = listener_repository

    def get_song_without_listeners(self):
        song_list = self.__song_repository.get_all_entities()
        no_listeners_list = []
        for song in song_list:
            if not self.__has_listener(song):
                no_listeners_list.append(song)
        return no_listeners_list

    def __has_listener(self, song):
        listener_list = self.__listener_repository.get_all_entities()
        for listener in listener_list:
            if listener.get_song_title() == song.get_title():
                return True
        return False