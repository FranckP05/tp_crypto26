# ce fichier presente les algorithmes de chiffrement, dechiffrement du cryptosysteme de vigenere
# On rappelle que la fonction de chiffrement fonctionne ainsi: C = (x+k) mod 26
# L'algorithme de dechiffrement est ainsi: D = (x-k) mod 26
# Nous travaillons ici dans l'anneau Z/26Z. 
# (j'ai d'abord fait cela avec l'anneau Z/128Z et ça a fonctionné, mais le msg chiffré était souvent bizarre pour le user)

# Dictionnaires pour mapper les lettres de l'alphabet à leurs valeurs numériques
dict = {"A":0, "B":1,"C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, 
        "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
invert_dict = {number:letter for letter, number in dict.items()} #on inverse le dictionnaire

# fonction de chiffrement

def chiffrement(msg:str, k:str):
#Nous nous servons des dictionnaires pour puvoir avoir l'equivalent numeriques des lettres selon
# l'alphabet standard
   char_correspondant = ''
   position_correspondant = 0
   msg_chiffre = ""
   j=0
   if len(k)>len(msg):
      return "Impossible de chiffré car la taille de la clef ne peut pas etre superieure au message."
   else:
      for el in msg.upper().replace(" ", ""):
         position_correspondant = (dict[el] + dict[k[j]]) % 26
         char_correspondant = invert_dict[position_correspondant]
         if(j==len(k)-1): 
             j = 0
         else:
             j+=1
         print(f"position du chiffre: {position_correspondant}, caractere chiffre: {char_correspondant}")
         msg_chiffre += char_correspondant
      return  msg_chiffre


def dechiffrement(cyphertext:str, k:str):
   # Fonction pour dechiffrer un mot chiffré
   j=0
   texte_clair = ""
   next_char=''
   if len(cyphertext) < len(k):
      return "Impossible de dechiffré parceque la clef ne peut pas etre plus grande que le message"
   else:
      for el in cyphertext:
         position_clair = (dict[el] - dict[k[j]]) % 26
         next_char = invert_dict[position_clair]
         texte_clair += next_char
         if(j==len(k)-1): 
             j = 0
         else:
             j+=1
      return texte_clair


message_original = "CRYPTOGRAMME"
clef = "MINET"

message_crypte = chiffrement(message_original, clef)
print("\nTexte chiffré :", message_crypte)

print("\nMessage décrypté: ", dechiffrement(message_crypte, clef))
