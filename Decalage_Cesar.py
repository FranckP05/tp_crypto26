# Il s'agit de realiser les fonctions de chiffrement, de dechiffrement et de decryptage dans le cryptosysteme par decalage
# le chiffrement de Cesar est un cas particulier, il represente le cas ou l'on fait un 3-decalage.

"""
    def encryption (msg:str, key:int): 
        # cette premiere fonction fait usage des nombres et est limitee au 26 lettres classiques l'aphabet Français
        cypher = ""
        dict = {"A":0, "B":1,"C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, 
                        "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
        invert_dict = {letter:number for number, letter in dict.items()}
    
        if key >= 26:
            return "La valeur de la cle est trop grande"
        else:
            for el in msg.upper().replace(" ", ""):   
                next_position = (dict[el] + key) % 26
                cypher += invert_dict[next_position]
    
        return cypher
"""

def encryption(msg:str, k:int):
    # Dans cette fonction ci, nous nous donnons maintenant un defis:
        # - utiliser le ASCII au lieu du dictionnaire limité

    cyphertext = ""
    # pour l'utilisation du ASCII en python, il existe les fonctions ord() et chr().
    # Deja, nous sommes dans un anneau Z/128Z
    # ord() renvoie la valeur correspondante en decimal d'une lettre
    # chr() renvoie la valeur alphabetique correspondante d'un nombre decimal
    for letter in msg:
        next_position = (ord(letter)+k) % 128 
        cyphertext += chr(next_position)

    return cyphertext


def decryption(cyphertext:str, k:int):
    # Nous nous servons toujours de l'ASCII sous l'anneau Z/128Z.
    plain_text=""
    for letter in cyphertext:
        corresponding_position  = (ord(letter)-k) % 128
        plain_text += chr(corresponding_position)

    return plain_text 


# Maintenant, le defis est de trouver un moyen de retrouver le texte clair, a partir du texte chiffre. 
# cela reviens en fait a trouver la cle. Dans le cours, la methode recommandee est de procede par force brute
# cela signifie que l'on vas essayer de deviner la cle. Dans le contexte de l'anneau Z/26Z, cela equivaut à tester de 0 à 25
# comme nous sommes en ASCII standard (Z/128Z), nous allons tester de 0 à 127. c'est 128 combinaisons

# Est-ce possible de le faire en O(n) ? 
 
def decypher(cyphertext:str, plain_text:str):
    for i in range(128):
        result_cypher = encryption(plain_text, i)
        if result_cypher == cyphertext:
            return f"found: {i}"
        else:
            print (f"tested {i}")
    return "key not found!"
    
cyphertext = encryption("Bonjour le monde", 36)   
# on est oblige de fonctionner ainsi parceque en ASCII et meme en ASCII etendu, le transformé contient souvent des caractères
# invisibles. Donc si l'on copie juste le texte, on risque avoir des messages d'erreur incoherent.   
print(decypher(cyphertext, "Bonjour le monde"))

# Note : Faire avec Cesar revient juste a choisir la clef à 3.