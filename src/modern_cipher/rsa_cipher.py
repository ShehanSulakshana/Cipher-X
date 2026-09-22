import os
from abc import ABC
from colorama import Back, Fore, Style
from .Modern_BaseCipher import ModernBaseCipher

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa


class RSAcipher(ModernBaseCipher, ABC):

    def __init__(self):
        super().__init__("RSA Crypto-System")


    def get_inputs(self):
        super().get_inputs()
        if self.mode == 'decrypt':
            self.decrypt()

    def encrypt(self):
        try:
            if not hasattr(self, "plaintext_input") or not self.plaintext_input:
                raise ValueError("Plaintext input is missing or empty.")

            plaintext = self.plaintext_input.encode("utf-8")

            #KeyGeneration
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048
            )
            public_key = private_key.public_key()

            cipher_text = public_key.encrypt(
                plaintext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            #Save key
            pem_private_key = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
            pem_public_key = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            with open("RSA/public_key.pem", "wb") as pub:
                pub.write(pem_public_key)
            with open("RSA/private_key.pem", "wb") as pri:
                pri.write(pem_private_key)

            # convert ciphertext to hex
            cipher_text = cipher_text.hex()
            # Save ciphertext
            with open("RSA/ciphertext.txt", "w") as key_file:
                key_file.write(cipher_text)

            # Display
            self.display_encryption(cipher_text)

        except TypeError as e:
            print(f"\n{self.tab_space}{Fore.RED}[!] Invalid input data: {e} {Style.RESET_ALL}")

        except ValueError as e:
            print(f"\n{self.tab_space}{Fore.RED}[!] Input Error: {e} {Style.RESET_ALL}")

        except Exception as e:
            print(f"\n{self.tab_space}{Fore.RED}[!] Encryption Failed: {e} {Style.RESET_ALL}")



    def decrypt(self):

        try :
            # Load private key from file
            if os.path.exists("RSA/private_key.pem"):
                with open("RSA/private_key.pem", "rb") as pri:
                    private_key = serialization.load_pem_private_key(
                        pri.read(),
                        password=None
                    )
            else:
                print(f"\n{self.tab_space}{Fore.RED}[!] File doesn't exists : RSA/private_key.pem {Style.RESET_ALL}")
                print(f"{self.tab_space}{Fore.WHITE}[!] Create the missing file in RSA directory and add your private key inside the file. {Style.RESET_ALL}")
                return

            # Load cipher text and convert hex to bytes
            if os.path.exists("RSA/ciphertext.txt" ):
                with open("RSA/ciphertext.txt", "r") as ct:
                    ciphertext = ct.read()
                try:
                    ciphertext = bytes.fromhex(ciphertext)
                except Exception:
                    print(f"\n{self.tab_space}{Fore.RED}[!] Malformed ciphertext ! {Style.RESET_ALL}")
                    print(f"\n{self.tab_space}{Fore.RED}[!] Ciphertext must have been encoded in HEX to continue... {Style.RESET_ALL}")
            else:
                print(f"\n{self.tab_space}{Fore.RED}[!] File doesn't exists : RSA/ciphertext.txt {Style.RESET_ALL}")
                print(f"{self.tab_space}{Fore.WHITE}[!] Create the missing file in RSA directory and,\n{self.tab_space}    add your ciphertext( must be hex ) inside the file. {Style.RESET_ALL}")
                return

            plaintext = private_key.decrypt(
                ciphertext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            # Display plaintext
            self.display_decryption(plaintext)

        except Exception as e:
            print(f"\n{self.tab_space}{Fore.RED}[!] Decryption Failed : {e} {Style.RESET_ALL}")

    def display_encryption(self , cipher_text):
        # Displaying encryption output with formatted plaintext
        print(f"\n\n{self.tab_space}{Fore.GREEN}{Back.BLACK} [@] Cipher Text (HEX) : {Style.RESET_ALL}   {cipher_text}")
        print(f"\n{self.tab_space}{Fore.GREEN} [#] Cipher Text successfully saved to 'RSA/ciphertext.bin'. {Style.RESET_ALL}")
        print(f"{self.tab_space}{Fore.GREEN} [#] Private key successfully saved to 'RSA/private_key.pem'. {Style.RESET_ALL}")
        print(f"{self.tab_space}{Fore.GREEN} [#] Public key successfully saved to 'RSA/public_key.pem'. {Style.RESET_ALL}")



    def display_decryption(self , dectypted_data):
        print(f"\n{self.tab_space}{Fore.GREEN}{Back.BLACK} [@] Decrypted Plaintext: : {Style.RESET_ALL}   {dectypted_data.decode("utf-8")}")


