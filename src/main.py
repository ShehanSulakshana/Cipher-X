from colorama import Fore, Style
from classical_cipher.caesar_cipher import CaesarCipher


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
        print(f"\n{self.tab_space *3}[1]. Classical Ciphers")
        print(f"{self.tab_space *3}[2]. Advanced Ciphers")


    def handle_options(self):
        correct_input = False
        input_value = None
        while not correct_input:

            try:
                input_value = int(input(f"\n{self.tab_space}[?] Choice : "))

                if input_value == 1 :
                    # FIXME : Only a single cipher from planned list is called here , need to show a list here
                    caesar_cipher = CaesarCipher()
                    caesar_cipher.get_inputs()
                    correct_input = True

                elif input_value == 2 :
                    print("Option 2")       #TODO : Implement option method call
                    correct_input = True

                elif input_value ==3 :
                    print("Option 3")       #TODO : Implement option method call
                    correct_input = True

                else:
                    print(f"{self.tab_space}{Fore.RED}[!] Invalid input {Style.RESET_ALL}")
            except Exception as e:
                print(f"{self.tab_space}{Fore.RED}[!] Invalid input {Style.RESET_ALL}")
                print(e)


    def run(self):
        self.display_banner()
        self.display_menu()
        self.handle_options()


if __name__ == '__main__':
    main = Main()
    main.run()
