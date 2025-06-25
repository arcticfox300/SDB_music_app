from Domain.exceptions import CustomExceptions


class MyUtilities:
    def __init__(self, array):
        self.__array = array

    @staticmethod
    def average(array):
        if len(array) == 0:
            raise CustomExceptions(f"The list in empty.")

        sum = 0
        count = 0

        for index in range (0, len(array)):
            sum += int(array[index].get_duration())
            count += 1

        return sum / count

    @staticmethod
    def print_array(array):
        for element in array:
            print(element)