import ClassicMeth.PlayFaire as pl
import ClassicMeth.Vigenere as vg
import ClassicMeth.TranspositionCol as cl
import ModerMeth.DES as ds

playfairCipher= pl.PlayfairCipher("key", "text to decrypt")
playfairCipherD = pl.PlayfairCipher("key", "bqszztldpfrk")
vigenere = vg.VigenereCipher("key", "text to decrypt")
vigenereD = vg.VigenereCipher("key", "divdxmniabcnd")
col = cl.TranspositionColonne("key", "text to decrypt")
colD = cl.TranspositionColonne("key", col.transpositionColonneEncrypt())
des = ds.AlgorithmeDES("key", "text to decrypt")

print(playfairCipher.playfaireEncrypt())
print(playfairCipherD.playfaireDecrypt())
print(vigenere.vigenereCipherEncrypt())
print(vigenereD.vigenereCipherDecrypt())
print(col.transpositionColonneEncrypt())
print(colD.transpositionColonneDecrypt())

print(des.DESAlgorithme())