import cezar.cezar as cezar

class TestCezar:
    def testEncryptLetters(self):
        c = cezar.Cezar()
        name = 'Bartek'
        key = 3
        encrypted_text = c.encrypt(name, key)
        assert "Eduwhn" == encrypted_text
        print(encrypted_text)

    def testDecryptLetters(self):
        c = cezar.Cezar()
        name = 'Eduwhn'
        key = 3
        decrypted_text = c.decrypt(name, key)
        assert "Bartek" == decrypted_text
        print(decrypted_text)