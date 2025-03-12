class VigenereCipher:
    def __init__(self, key, text):
        self.key = key.replace(" ", "")
        self.text = text.replace(" ", "")
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def vigenereCipherEncrypt(self):
        C = []
        P = [self.alphabet.index(i) for i in self.text if i in self.alphabet]
        K = [self.alphabet.index(i) for i in self.key if i in self.alphabet]
        K_repeated = [K[i % len(K)] for i in range(len(P))]

        
        for i in range(len(P)):
            C.append((P[i] + K_repeated[i]) % 26)
        
        return "".join(self.alphabet[i] for i in C)
    
    def vigenereCipherDecrypt(self):
        C = []
        P = [self.alphabet.index(i) for i in self.text if i in self.alphabet]
        K = [self.alphabet.index(i) for i in self.key if i in self.alphabet]
        K_repeated = [K[i % len(K)] for i in range(len(P))]

        
        for i in range(len(P)):
            C.append((P[i] - K_repeated[i]) % 26)
        
        return "".join(self.alphabet[i] for i in C)