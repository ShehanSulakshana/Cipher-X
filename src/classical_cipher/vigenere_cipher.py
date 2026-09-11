from abc import ABC

from typing_extensions import override
from colorama import Fore, Style ,Back
from src.cipher import Cipher
from time import sleep

class VigenereCipher(Cipher, ABC):

    def __init__(self):
        super().__init__()
        self.plaintext_input = None
        self.key_input = None
        self.plaintext_list = []
        self.generated_key_index_list = []
        self.ciphertext_list = []
        self.tab_space = "\t"
        self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



    def execute(self):
        print(f"\n\t{Fore.GREEN}{'*' * 5} [ Vigenere Cipher ] {'*' * 49}{Style.RESET_ALL}")
        self.get_inputs()
        self.encrypt()



    def get_inputs(self):

        # Plaintext input and validate/process then filter them
        self.plaintext_input = str(input(f"\n{self.tab_space}[?] Plaintext : "))
        self.plaintext_list = self.validate_input(self.plaintext_input.upper())
        self.filter_plaintext()

        # Get Key Input and validate
        while True:
            self.key_input = str(input(f"\n{self.tab_space}[?] Key [0-{len(self.plaintext_list) if len(self.plaintext_list)<25 else "25"}] : "))
            try :
                key_validation_result = self.validate_key(self.key_input)
                break
            except Exception as e :
                 print(f"{self.tab_space}{Fore.RED}[!] {e}{Style.RESET_ALL}")

        self.key_generation()


    def key_generation(self):
        key_len , input_len = len(self.key_input) , len(self.plaintext_input)
        current = 0

        for i in range(input_len):
            if current < key_len:
                char = self.key_input[current].upper()
                self.generated_key_index_list.append((self.alphabet.index(char)))
                current += 1
            if current == key_len:  # Important : this same level if statement added to make sure current resets within same iteration
                current = 0         # without wasting an iteration round on else condition , which becomes reason to a key generation inconsistent.


    def filter_plaintext(self):
        filtered_temp = []
        for char in self.plaintext_list:
            if char.isalpha():
                filtered_temp.append(char)
        self.plaintext_list = filtered_temp # Filtered input plaintext = only contain letters


    def encrypt(self):
        current = 0
        for char in self.plaintext_list:
            index = self.alphabet.index(char)
            enc_index = divmod((index + self.generated_key_index_list[current]) , 26)[-1]  # implemented -> encipher = plaintext_value + index (mode26)
            enc_char = self.alphabet[enc_index]
            current +=1

            self.ciphertext_list.append(enc_char)
        self.display_encryption()


    def display_encryption(self):
        # Displaying encryption output with formatted plaintext
        print(f"\n\n{self.tab_space}{Back.BLACK} [@] Plain Text  : {Style.RESET_ALL}   {''.join([char for char in self.plaintext_list if char.isalpha()])}")
        print(f"\n{self.tab_space}{Fore.GREEN}{Back.BLACK} [#] Cipher Text : {Style.RESET_ALL}   {"".join(self.ciphertext_list)}")
