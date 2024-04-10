class RailFenceCipher:
    def __init__(self) -> None:
        pass
    def railfence_encrypt(self, plain_text, key):
        encrypted_text = ""
        for i in range(key):
            for j in range(len(plain_text)):
                if (i + j) % key == 0:
                    encrypted_text += plain_text[j]
        return encrypted_text
    
    def railfence_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        for i in range(key):
            for j in range(len(encrypted_text)):
                if (i + j) % key == 0:
                    decrypted_text += encrypted_text[j]
        return decrypted_text