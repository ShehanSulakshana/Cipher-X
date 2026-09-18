from colorama import Fore, Style
from classical_cipher.caesar_cipher import CaesarCipher
from src.classical_cipher.monoalphabetic_cipher import MonoalphabeticCipher
from src.classical_cipher.vernam_otp_cipher import VernamCipher
from src.classical_cipher.vigenere_cipher import VigenereCipher
from src.modern_cipher.aes_cipher import AEScipher
from src.modern_cipher.rsa_cipher import RSAcipher


class Main :

    def __init__(self):
        self.banner = """
         ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗               ██╗  ██╗
        ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗              ╚██╗██╔╝
        ██║     ██║██████╔╝███████║█████╗  ██████╔╝    █████╗     ╚███╔╝ 
        ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗    ╚════╝     ██╔██╗ 
        ╚██████╗██║██║     ██║  ██║███████╗██║  ██║              ██╔╝ ██╗
         ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝              ╚═╝  ╚═╝                                     
        """
        self.tab_space = "\t"


    def display_banner(self):
        print(f"{Fore.GREEN}{self.banner}{Fore.RESET}")
        print(f"{self.tab_space *3}{Style.BRIGHT}{Fore.LIGHTWHITE_EX}-{Fore.GREEN} Script By Shehan Sulakshana                  {Style.RESET_ALL}")
        print(f"{self.tab_space *3}{Style.BRIGHT}-{Fore.GREEN} GITHUB : https://github.com/ShehanSulakshana{Style.RESET_ALL} \n")
        print(f"\t{Fore.GREEN}{'#' * 75}{Style.RESET_ALL}")

    def display_menu(self):
        print(f"\n{self.tab_space *2}{Fore.BLUE}{Style.BRIGHT}> Classical Ciphers  {Style.RESET_ALL}")
        print(f"{self.tab_space *3}[1]. Caesar Cipher")
        print(f"{self.tab_space *3}[2]. Substitution Cipher (Mono-alphabetic)")
        print(f"{self.tab_space *3}[3]. Vigenere Cipher (Poly-alphabetic)")
        print(f"{self.tab_space *3}[4]. Vernam Cipher / One Time Pad (OTP)")

        print(f"\n{self.tab_space * 2}{Fore.BLUE}{Style.BRIGHT}> Modern Ciphers {Style.RESET_ALL}")
        print(f"{self.tab_space *3}[5]. AES (Advanced Encryption Standard)")
        print(f"{self.tab_space *3}[6]. RSA (Public-Key Cryptography)")

        # print(f"\n{self.tab_space * 2}{Fore.BLUE}{Style.BRIGHT}> Steganography {Style.RESET_ALL}")
        # print(f"{self.tab_space *3}[9]. Image Steganography")




    def handle_options(self):
        correct_input = False
        input_value = None
        while not correct_input:

            try:
                input_value = int(input(f"\n{self.tab_space}[?] Choice : "))

                if input_value == 1 :
                    caesar_cipher = CaesarCipher()
                    caesar_cipher.execute()
                    correct_input = True

                elif input_value == 2 :
                    monoalphabetic_cipher = MonoalphabeticCipher()
                    monoalphabetic_cipher.execute()
                    correct_input = True

                elif input_value ==3 :
                    vigenere_cipher = VigenereCipher()
                    vigenere_cipher.execute()
                    correct_input = True

                elif input_value ==4 :
                    vernam_cipher = VernamCipher()
                    vernam_cipher.execute()
                    correct_input = True

                elif input_value ==5 :
                    aes_cipher = AEScipher()
                    aes_cipher.execute()
                    correct_input = True

                elif input_value ==6 :
                    rsa_cipher = RSAcipher()
                    rsa_cipher.execute()
                    correct_input = True

                else:
                    print(f"{self.tab_space}{Fore.RED}[!] Invalid input {Style.RESET_ALL}")
            except ValueError:
                print(f"{self.tab_space}{Fore.RED}[!] Invalid input {Style.RESET_ALL}")


    def run(self):
        self.display_banner()
        self.display_menu()
        self.handle_options()


if __name__ == '__main__':
    main = Main()
    main.run()
