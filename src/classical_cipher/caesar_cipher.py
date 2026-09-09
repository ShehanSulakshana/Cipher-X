from typing_extensions import override
from colorama import Fore, Style ,Back
from src.cipher import Cipher
from time import sleep

class CaesarCipher(Cipher):

    def __init__(self):
        super().__init__()
        self.plaintext_input = None
        self.plaintext_list = []
        self.ciphertext_list = []
        self.tab_space = "\t"
        self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.shift_value = 3


    def execute(self):
        print(f"\n\t{Fore.GREEN}{'*' * 5} [ Caesar Cipher ] {'*' * 52}{Style.RESET_ALL}")
        self.get_inputs()
        self.encrypt()




    def get_inputs(self):

        # Plaintext input and validate/process
        self.plaintext_input = str(input(f"\n{self.tab_space}[?] Plaintext : "))
        self.plaintext_list = self.validate_input(self.plaintext_input.upper())

        # Shift input and validation
        self.shift_value = int(input(f"\n{self.tab_space}[?] Shift by [1-25; Default 3 ]: "))
        if self.shift_value > 25 or self.shift_value < 1 :
            print(f"\n{self.tab_space}[!] Invalid shift value, Using default shift 3 . ")
            self.shift_value = 3
            sleep(1.5)
        else : pass


    def encrypt(self):
        for char in self.plaintext_list:
            if char.isalpha():
                index = self.alphabet.index(char)
                enc_index = divmod((index + self.shift_value) , 26)[-1]  # implemented -> encipher = plaintext_value + index (mode26)
                enc_char = self.alphabet[enc_index]

                self.ciphertext_list.append(enc_char)

        self.display_encryption()


    def display_encryption(self):
        # Displaying encryption output with formatted plaintext
        print(f"\n\n{self.tab_space}{Back.BLACK} [@] Plain Text  : {Style.RESET_ALL}   {''.join([char for char in self.plaintext_list if char.isalpha()])}")
        print(f"\n{self.tab_space}{Fore.GREEN}{Back.BLACK} [#] Cipher Text : {Style.RESET_ALL}   {"".join(self.ciphertext_list)}")

