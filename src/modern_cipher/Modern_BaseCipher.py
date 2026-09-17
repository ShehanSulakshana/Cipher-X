from src.cipher import Cipher
from abc import ABC, abstractmethod
from colorama import Fore, Style , Back

class ModernBaseCipher(Cipher, ABC):

    def __init__(self , cipher_name):
        super().__init__()

        self.cipher_name = cipher_name
        self.mode = None
        self.plaintext_input = None
        self.ciphertext_input = None
        self.nonce_input = None
        self.key_input = None
        self.tab_space = "\t"
        self.shift_value = 3

    def execute(self):
        print(f"\n\t{Fore.GREEN}{'*' * 5} [ {self.cipher_name} ] {'*' * 30}{Style.RESET_ALL}")
        print(f"\n{self.tab_space * 2}{Fore.GREEN}> Modes :  {Style.RESET_ALL}")
        print(f"{self.tab_space * 3}[1]. Encryption")
        print(f"{self.tab_space * 3}[2]. Decryption")

        correct_input = False
        while not correct_input:
            try:
                mode_input = int(input(f"\n{self.tab_space}[?] Select mode : "))
                if mode_input == 1:
                    self.mode = "encrypt"
                    correct_input = True
                elif mode_input == 2:
                    self.mode = "decrypt"
                    correct_input = True
                else:
                    print(f"{self.tab_space}{Fore.RED}[!] Invalid choice.{Style.RESET_ALL}")
            except ValueError:
                print(f"{self.tab_space}{Fore.RED}[!] Invalid input. {Style.RESET_ALL}")

        self.get_inputs()


    def get_inputs(self):

        if self.mode == "encrypt":
            print(f"\n{self.tab_space *2}{Fore.GREEN}>> Encryption{Style.RESET_ALL}")
            # Plaintext input and validate/process
            self.plaintext_input = str(input(f"\n{self.tab_space}[?] Plaintext : "))
            self.encrypt()
        else:
            print(f"\n{self.tab_space *2}{Fore.GREEN}>> Decryption{Style.RESET_ALL}")
            self.ciphertext_input = str(input(f"\n{self.tab_space}[?] CipherText : "))
            self.key_input = str(input(f"{self.tab_space}[?] Decrypt Key : "))



    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass


    @abstractmethod
    def display_decryption(self):
        pass
