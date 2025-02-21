class CifraCesar:
    def __init__(self):
        self.ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, text: str) -> list:
        text = text.upper()
        indices = []
        for char in text:
            if char in self.ALFABETO:
                indices.append(self.ALFABETO.index(char)) 
        return indices

    def decode(self, indices: list) -> str:
        text = ""
        for index in indices:
            text += self.ALFABETO[index]
        return text

    def encrypt(self, enc_text: list, key: int) -> list:
        cipher_text = []
        for enc_char in enc_text:
            cipher_text.append((enc_char + key) % 26)  # Garantir que permanece dentro do alfabeto
        return cipher_text

    def decrypt(self, cipher_text: list, key: int) -> list:
        enc_text = []
        for char in cipher_text:
            enc_text.append((char - key) % 26)  # Garantir que permanece dentro do alfabeto
        return enc_text


# Código de teste fora da classe
a = CifraCesar()
text = "Hello World"
encoded = a.encode(text)
print(f"Encoded: {encoded}")

encrypted = a.encrypt(encoded, 2)
print(f"Encrypted: {encrypted}")

decoded = a.decode(encoded)
print(f"Decoded: {decoded}")

print("\nDecrypting...")
decrypted = a.decrypt(encrypted, 2)
print(f"Decrypted: {decrypted}")

decrypted_text = a.decode(decrypted)
print(f'Texto decriptado e decodificado: {decrypted_text}')
