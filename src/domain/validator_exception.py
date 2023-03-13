class ValidatorException(Exception):
    def __init__(self, message):
        self.__message = message

    def get_message(self):
        return self.__message

    def __str__(self):
        return self.__message