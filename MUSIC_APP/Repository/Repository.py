from Domain.exceptions import CustomExceptions

class Repository:
    def __init__(self, entity_list):
        self.__entity_list = []

    def add_entity(self, new_entity):
        for entity in self.__entity_list:
            if entity == new_entity:
                raise CustomExceptions(f'The entity {new_entity} has already been added.')
        self.__entity_list.append(new_entity)

    def delete_entity(self, entity_to_delete):
        for index in range (0, len(self.__entity_list)):
            if entity_to_delete == self.__entity_list[index]:
                del self.__entity_list[index]
                return
        raise CustomExceptions(f"The entity {entity_to_delete} doesn't exist.")

    def get_all_entities(self):
        if len(self.__entity_list) == 0:
            raise CustomExceptions(f"The list of songs is empty.")
        return self.__entity_list