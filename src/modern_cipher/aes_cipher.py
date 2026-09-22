import os
from abc import ABC
from base64 import encode

from colorama import Back, Fore, Style
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag

from .Modern_BaseCipher import ModernBaseCipher


class AEScipher(ModernBaseCipher, ABC):

    def get_inputs(self):
        super().get_inputs()
        if self.mode == 'decrypt':
            self.ciphertext_input = str(input(f"\n{self.tab_space}[?] Cipher text : "))
            self.key_input = str(input(f"{self.tab_space}[?] Key : "))
            self.nonce_input = str(input(f"{self.tab_space}[?] Nonce : "))
            self.decrypt()

    def encrypt(self):
        try:
            if not hasattr(self, "plaintext_input") or not self.plaintext_input:
                raise ValueError("Plaintext input is missing or empty.")

            plaintext = self.plaintext_input.encode("utf-8")
            key = AESGCM.generate_key(bit_length=128)
            aesgcm = AESGCM(key)
            nonce = os.urandom(12)

            cipher_text = aesgcm.encrypt(nonce, plaintext, None)
            self.display_encryption(cipher_text, key, nonce)

        except TypeError as e:
            print(f"\n{self.tab_space}[!] Invalid input data: {e}")
        except ValueError as e:
            print(f"\n{self.tab_space}[!] Input Error: {e}")
        except Exception as e:
            print(f"\n{self.tab_space}[!] Encryption Failed: {e}")


    def decrypt(self):
        try:
            ciphertext = bytes.fromhex(self.ciphertext_input)
            key = bytes.fromhex(self.key_input)
            nonce = bytes.fromhex(self.nonce_input)

            aesgcm = AESGCM(key)
            decrypted_bytes = aesgcm.decrypt(nonce, ciphertext, None)

            self.display_decryption(decrypted_bytes)

        except ValueError:
            print("\n[!] Input Error: Key, Nonce, or Ciphertext is not valid Hex.")
        except InvalidTag:
            print("\n[!] Decryption Failed: Wrong Key/Nonce or corrupted Ciphertext.")


    def display_encryption(self , cipher_text , key , nonce):
        # Displaying encryption output with formatted plaintext
        print(f"\n\n{self.tab_space}{Back.BLACK} [@] Cipher Text (HEX)  : {Style.RESET_ALL}   {cipher_text.hex()}")
        print(f"\n{self.tab_space}{Fore.GREEN}{Back.BLACK} [#] Key (HEX) : {Style.RESET_ALL}   {key.hex()}")
        print(f"\n{self.tab_space}{Fore.GREEN}{Back.BLACK} [#] Nonce (HEX) : {Style.RESET_ALL}   {nonce.hex()}")


    def display_decryption(self , dectypted_data):
        print(f"\n{self.tab_space}{Fore.GREEN}{Back.BLACK} [@] Decrypted Plaintext: : {Style.RESET_ALL}   {dectypted_data.decode("utf-8")}")



    def __init__(self):
        super().__init__("Advanced Encryption Standard - GCM")


