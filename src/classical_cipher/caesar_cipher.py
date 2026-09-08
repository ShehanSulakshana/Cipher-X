from src.cipher import Cipher

class CaesarCipher(Cipher):

    def __init__(self):
        super().__init__()
        self.plaintext_input = None
        self.tab_space = "\t"


    def get_inputs(self):
        self.plaintext_input = str(input(f"\n{self.tab_space}[?] Plaintext : "))
        print(self.validate_input(self.plaintext_input))

    def encrypt(self):
        pass
