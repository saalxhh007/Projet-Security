class AlgorithmeDES:
    def __init__(self, key, text):
        self.key = key
        self.text = text
        
    PC1 = [ 57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27, 19,
            11, 3, 60, 52, 44, 36, 63, 55,
            47, 39, 31, 23, 15, 7,
            62, 54, 46, 38, 30, 22, 14, 6,
            61, 53, 45, 37, 29, 21, 13, 5,
            28, 20, 12, 4 ]

    PC2 = [ 14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]

    shifts = [ 1, 1, 2, 2, 2, 2, 2, 2,
                1, 2, 2, 2, 2, 2, 2, 1]
        
    IP = [ 58, 50, 42, 34, 26, 18, 10, 2,
            60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6,
            64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1,
            59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5,
            63, 55, 47, 39, 31, 23, 15, 7]

    FP = [ 40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]

    def toBinary(self):
        return ''.join(format(ord(c), '08b') for c in self.text)
    
    def ToText(self, c):
        text = ''
        for i in range(0, len(c), 8):
            text += chr(int(c[i:i+8], 2))
        return text
    
    def permute(self, text, tab):
        return ''.join(text[i - 1] for i in tab)
    
    def shiftLeft(self, bits, shift):
        return bits[shift:] + bits[:shift]

    def generateRounds(self, key):
        key = self.permute(key, self.PC1)
        C, D = key[:28], key[28:]

        rkeys = []

        for shift in self.shifts:
            C, D = self.shiftLeft(C, shift), self.shiftLeft(D, shift)
            rKey = self.permute(C + D, self.PC2)
            rkeys.append(rKey)

        return rkeys

    def feistelFunc(self, right, key):
        return ''.join(str(int(a) ^ int(b)) for a, b in zip(right, key))

    def DESAlgorithme(self):
        textToBin = self.toBinary()
        keyToBin = self.toBinary()

        textToBin = self.permute(textToBin, self.IP)
        L, R = textToBin[:32] , textToBin[32:]

        Rkeys = self.generateRounds(keyToBin)

        for Rkey in Rkeys:
            L = R
            R = self.feistelFunc(R, Rkey)
            R = "".join(str(int(a) ^ int(b)) for a, b in zip(R, L))

        c = self.permute(R + L, self.FP)

        return self.ToText(c)
