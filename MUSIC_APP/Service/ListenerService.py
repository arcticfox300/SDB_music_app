from Domain.Listener import Listener
from Repository.Repository import Repository
from Service.MyUtilities import MyUtilities


class ListenerService:
    def __init__(self, listener_repository : Repository):
        self.__listener_repository = listener_repository

    def add_listener(self, new_listener : Listener):
        """
        This method adds a new listener to the list
        :param new_listener:
        :param new_listener: the listener to be added
        """
        self.__listener_repository.add_entity(new_listener)

    def delete_listener(self, to_delete : Listener):
        """
        This mothod delets a listener from the list
        :param to_delete: the listener to be deleted
        """
        self.__listener_repository.delete_entity(to_delete)

    def avrage_age(self):
        return MyUtilities.average(self.__listener_repository.get_all_entities())

    def get_all_listeners(self):
        return self.__listener_repository.get_all_entities()