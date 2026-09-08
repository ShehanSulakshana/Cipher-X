from abc import ABC,abstractmethod

class Cipher(ABC):

    def __init__(self):
        pass


    @abstractmethod
    def get_inputs(self):
        pass


    @abstractmethod
    def encrypt(self):
        pass


    @staticmethod
    def validate_input(input_plaintext):
        list_plaintext = []

        # Trim leading and trailing spaces
        input_plaintext = input_plaintext.strip()

        # Convert string which is in valid length into a list
        if len(input_plaintext) <= 200:
            list_plaintext = list(input_plaintext)
            return list_plaintext
        else :
            return Exception("Input plaintext is too lengthy.")


