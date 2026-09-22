import sys
from pathlib import Path
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))


from time import sleep
from colorama import Fore, Style, Back
from cipher import Cipher


class MonoalphabeticCipher(Cipher):


    def __init__(self):
        super().__init__()
        self.plaintext_input = None
        self.plaintext_list = []
        self.ciphertext_list = []
        self.tab_space = '\t'
        self.map_alphabet = {
            'A': 'Q',
            'B': 'W',
            'C': 'E',
            'D': 'R',
            'E': 'T',
            'F': 'Y',
            'G': 'U',
            'H': 'I',
            'I': 'O',
            'J': 'P',
            'K': 'A',
            'L': 'S',
            'M': 'D',
            'N': 'F',
            'O': 'G',
            'P': 'H',
            'Q': 'J',
            'R': 'K',
            'S': 'L',
            'T': 'Z',
            'U': 'X',
            'V': 'C',
            'W': 'V',
            'X': 'B',
            'Y': 'N',
            'Z': 'M'
        }

    def execute(self):
        print(f"\n\t{Fore.GREEN}{'*' * 5} [ Mono-alphabetic Cipher ] {'*' * 43}{Style.RESET_ALL}")
        self.get_inputs()
        self.encrypt()

    def get_inputs(self):
        # Plaintext input and validate/process
        self.plaintext_input = str(input(f"\n{self.tab_space}[?] Plaintext : "))
        self.plaintext_list = self.validate_input(self.plaintext_input.upper())
        self.filter_plaintext()


        # Let User Know About Alphabet Mapping
        print(f"\n{self.tab_space}[*] Using default alphabet mapping for encryption : \n")
        sleep(1.5)



    def filter_plaintext(self):
        filtered_temp = []
        for char in self.plaintext_list:
            if char.isalpha():
                filtered_temp.append(char)
        self.plaintext_list = filtered_temp # Filtered input plaintext = only contain letters




    def encrypt(self):
        indent_value = 0
        for char in self.plaintext_list:
            map_value = self.map_alphabet.get(char)

            # Format the mapping sequence representation.
            if indent_value == 4 :
                print(f"{self.tab_space}{char} -> {map_value}")
                indent_value = 0
            else:
                print(f"{self.tab_space if indent_value==0 else ""}{self.tab_space}{char} -> {map_value}" , end=f'{self.tab_space}')
                indent_value += 1
            self.ciphertext_list.append(map_value)
        self.display_encryption()


    def display_encryption(self):
        # Displaying encryption output with formatted plaintext
        print(f"\n\n{self.tab_space}{Back.BLACK} [@] Plain Text  : {Style.RESET_ALL}   {"".join([char for char in self.plaintext_list if char.isalpha()])}")
        print(f"\n{self.tab_space}{Fore.GREEN}{Back.BLACK} [#] Cipher Text : {Style.RESET_ALL}   {"".join(self.ciphertext_list)}")

