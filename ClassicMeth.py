class VigenereCipher:
    def __init__(self, key, text):
        self.key = key.replace(" ", "")
        self.text = text.replace(" ", "")
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def vigenereCipher(self):
        C = []
        P = [self.alphabet.index(i) for i in self.text if i in self.alphabet]
        K = [self.alphabet.index(i) for i in self.key if i in self.alphabet]
        K_repeated = [K[i % len(K)] for i in range(len(P))]

        for i in range (len(self.text)):
            C.append((P[i] + K_repeated[i]) % 26)
        
        return "".join(self.alphabet[i] for i in C)

class PlayfairCipher:
    def __init__(self, key, text):
        self.key = key.replace(" ", "")
        self.text = text.replace(" ", "")
        self.alphabet = "abcdefghiklmnopqrstuvwxyz"
        self.matrice5x5 = self.matrice()
    def removeDuplicate(self):
        repeated = set()
        not_repeated = []
        for char in self.key:
            if char not in repeated:
                repeated.add(char)
                not_repeated.append(char)
        
        return "".join(not_repeated)
    def matrice(self):
        matrice = []
        for char in self.removeDuplicate():
            matrice.append(char)
        for char in self.alphabet:
            if char not in matrice:
                matrice.append(char)

        return [matrice[i:i + 5] for i in range(0, 25, 5)]
    
    def paires(self):
        paires = []
        for i in range (0, len(self.text), 2):
            a = self.text[i]
            b = self.text[i + 1]
            if a == b:
                b = "x"
            paires.append((a, b))
        return paires
    def findPosition(self, char):
        for i, row in enumerate(self.matrice5x5):
            if char in row:
                return i, row.index(char)
        return None
    def playfaire(self):
        paires = self.paires()
        c = []
        for a, b in paires:
            rowA, colA = self.findPosition(a)
            rowB, colB = self.findPosition(b)

            if rowA == rowB:
                c.append(self.matrice5x5[rowA][(colA + 1) % 5])
                c.append(self.matrice5x5[rowB][(colB + 1) % 5])

            elif colA == colB:
                c.append(self.matrice5x5[(rowA + 1) % 5][colA])
                c.append(self.matrice5x5[(rowB + 1) % 5][colB])

            else:
                c.append(self.matrice5x5[rowB][colA])
                c.append(self.matrice5x5[rowA][colB])

        return "".join(c)

class TranspositionColonne:
    def __init__(self, key, text):
        self.key = key.replace(" ", "")
        self.text = text.replace(" ", "")
        self.alphabet = "abcdefghiklmnopqrstuvwxyz"
        self.matrice = self.matrice()

    def matrice(self):
        cols = len(self.key)
        rows = len(self.text) // cols + (len(self.text) % cols > 0)
        matrice = [['' for _ in range(cols)] for _ in range(rows)]

        for i, char in enumerate(self.text):
            row = i // cols
            col = i % cols
            matrice[row][col] = char
        
        return matrice
    
    def transpositionColonne(self):
        key = sorted((char, i) for i, char in enumerate(self.key))
        
        c = ''
        for _, col in key:
            for row in self.matrice:
                if row[col]:
                    c += row[col]
        
        return c
key = "key"
text = "texte a chiffrer"
cipher = TranspositionColonne(key, text)
result = cipher.transpositionColonne()
print(result)