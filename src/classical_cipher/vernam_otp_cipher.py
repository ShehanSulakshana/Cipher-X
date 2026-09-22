import string
import sys
from pathlib import Path
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))


from abc import ABC
import random

from typing_extensions import override
from colorama import Fore, Style ,Back
from cipher import Cipher
from time import sleep

class VernamCipher(Cipher, ABC):

    def __init__(self):
        super().__init__()
        self.plaintext_input = None
        self.plaintext_list = []
        self.key = None
        self.ciphertext_list = []
        self.tab_space = "\t"
        self.shift_value = 3


    def execute(self):
        print(f"\n\t{Fore.GREEN}{'*' * 5} [ Vernam Cipher - OTP ] {'*' * 45}{Style.RESET_ALL}")
        self.get_inputs()
        self.encrypt()



    def get_inputs(self):

        # Plaintext input and validate/process
        self.plaintext_input = str(input(f"\n{self.tab_space}[?] Plaintext : "))
        self.plaintext_list = self.validate_input(self.plaintext_input.upper())
        self.filter_plaintext()

        # Random key generation & display
        self.key_generation()


    def key_generation(self):
        input_len = len(self.plaintext_input)
        characters = string.ascii_uppercase

        self.key = random.choices(population= characters  ,k=input_len)  # Random Key generation

        print(f"\n{self.tab_space}[*] Random Key : {", ".join(map(str, self.key))}")


    def encrypt(self):
        plaintext_binary_list = [format(ord(c), '08b') for c in self.plaintext_list]
        key_binary_list = [format(ord(c), '08b') for c in self.key]

        # Debug prints
        # print(f"plaintext binary length = {len(plaintext_binary_list)} \n {' '.join(plaintext_binary_list)} \n \n")
        # print(f"Key binary length = {len(key_binary_list)} \n {' '.join(key_binary_list)} \n \n")

        for index in range(len(plaintext_binary_list)) :
            encrypted_decimal_value = int(plaintext_binary_list[index] , 2) ^ int(key_binary_list[index] ,2)
            self.ciphertext_list.append(encrypted_decimal_value)

        self.display_encryption()


    def filter_plaintext(self):
        filtered_temp = []
        for char in self.plaintext_list:
            if char.isalpha():
                filtered_temp.append(char)
        self.plaintext_list = filtered_temp  # Filtered input plaintext = only contain letters


    def display_encryption(self):
        # Displaying encryption output with formatted plaintext
        print(f"\n\n{self.tab_space}{Back.BLACK} [@] Plain Text  : {Style.RESET_ALL}   {''.join([char for char in self.plaintext_list if char.isalpha()])}")

        ciphertext_integers = ", ".join(map(str, self.ciphertext_list))
        ciphertext_binary = ", ".join(format(x, "08b") for x in self.ciphertext_list)

        print(f"\n{self.tab_space}{Fore.GREEN}{Back.BLACK} [#] Cipher Text (Integers) : {Style.RESET_ALL}   {ciphertext_integers}")
        print(f"{self.tab_space}{Fore.GREEN}{Back.BLACK} [#] Cipher Text (Binary)   : {Style.RESET_ALL}   {ciphertext_binary}")