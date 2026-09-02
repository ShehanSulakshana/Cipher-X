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

