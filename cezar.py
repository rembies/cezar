class Cezar:
    def encrypt(self, text: str, key: int):
        result = ''
        for letter in text:
            encrypted_letter = chr(ord(letter) + key)
            result += encrypted_letter
        return result
    
    def decrypt(self, text: str, key: int):
        result = ''
        for letter in text:
            decrypted_letter = chr(ord(letter) - key)
            result += decrypted_letter
        return result

cesar = Cezar()
text_to_encrypt = "Bartek"
encrypted_text = cesar.encrypt(text_to_encrypt, 3)
print(encrypted_text)
decrypted_text =cesar.decrypt(encrypted_text, 3)
print(decrypted_text)