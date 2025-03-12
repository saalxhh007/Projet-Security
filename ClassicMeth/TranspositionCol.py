
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
    
    def transpositionColonneEncrypt(self):
        key = sorted((char, i) for i, char in enumerate(self.key))
        
        c = ''
        for _, col in key:
            for row in self.matrice:
                if row[col]:
                    c += row[col]
        
        return c
    def transpositionColonneDecrypt(self):
        key = sorted((char, i) for i, char in enumerate(self.key))
        cols = len(self.key)
        rows = len(self.text) // cols + (len(self.text) % cols > 0)
        
        columns = ['' for _ in range(cols)]
        index = 0
        for _, col in key:
            for row in range(rows):
                if index < len(self.text):
                    columns[col] += self.text[index]
                    index += 1
                    
        c = ''
        for row in range(rows):
            for col in range(cols):
                if row < len(columns[col]):
                    c += columns[col][row]
        return c