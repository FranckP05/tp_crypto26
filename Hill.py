#Ce fichier presente les algorithmes de chiffrement, dechiffrement du cryptosyteme de Hill. 
# On utilise les matrices pour chiffrer et dechiffrer le message. Ici, la clef est donc une matrice;
# On se limite a l'anneau Z/26Z
#


def chiffrement(msg: str, k:list[list]):
    # fonction de chiffrement
    paire = [msg[i:i+2] for i in range(0, len(msg), 2)] # on a besoin d'obtenir des paires de lettres de taille 2
    dict = {"A":0, "B":1,"C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, 
            "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
    reversed_dict = {letter:number for number, letter in dict.items()}
    cypher = ""
    if len(k) > 2:
        return "Votre clef doit etre une matrice 2x2"
    elif len(k[0])>2 and len(k[1])>2:
        return "Votre clef doit etre une matrice 2x2"
    else:
        if len(paire[len(paire)-1]) == 1:
            paire[len(paire)-1] += 'X'
        for el in paire:
           C1 = ((k[0][0] * dict[el[0]]) + (k[0][1] * dict[el[1]])) % 26
           C2 = ((k[1][0] * dict[el[0]]) + (k[1][1] * dict[el[1]])) % 26
           cypher += reversed_dict[C1] + reversed_dict[C2]
        return cypher    

#test de chiffrement d'un mot
print("Le mot chiffré de SUPINFOX est: ", chiffrement("SUPINFO", [[9, 4], [5, 7]]))

#On peut compexifier les choses en changeant l'anneau, ou encore en ajoutant d'autres caracteres (les minuscules, les accents et autres)

#Etant donné que le chiffrement de Hill utilise les matrices et que l'on aura besoin de la valeur de 1/(ad-bc), dans 
# l'anneau Z/26Z, on creer donc une fonction qui vas retourner la valeur l'inverse d'un nombre modulo 26 en se servant de l'algorithme d'Euclide

def inverse_modulo_26(a):
    #Cette fonction calcule l'inverse de 'a' dans Z/26Z.
    #Retourne l'inverse si l'existence est vérifiée, sinon lève une exception.
    n = 26
    
    # On initialise les coefficients pour remonter les égalités de Bézout
    t, nouveau_t = 0, 1
    r, nouveau_r = n, a
    
    while nouveau_r != 0:
        quotient = r // nouveau_r
        # Mise à jour du reste et des coefficients
        r, nouveau_r = nouveau_r, r - quotient * nouveau_r
        t, nouveau_t = nouveau_t, t - quotient * nouveau_t
        
    # Si le dernier reste non nul (r) est supérieur à 1, il n'y a pas d'inverse
    if r > 1:
        raise ValueError(f"Le nombre {a} n'est pas inversible modulo 26 (PGCD({a}, 26) = {r} != 1).")
        
    if t < 0:
        t = t + n
        
    return t


#fonction de dechiffrement

def dechiffrement(cypher:str, k:list[list]):
    paire = [cypher[i:i+2] for i in range(0, len(cypher), 2)] # on a besoin d'obtenir des paires de lettres de taille 2
    dict = {"A":0, "B":1,"C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, 
            "O":14, "P":15, "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}
    reversed_dict = {letter:number for number, letter in dict.items()}
    plain_text = ""
    if len(k)!=2:
        return "Votre matrice doit etre exactement de taille 2x2" 
    elif len(k[0])!=2 or len(k[1])!=2:
        return "Votre matrice doit etre exactement de taille 2x2"
    else:
        inverse_coef = inverse_modulo_26(((k[0][0]*k[1][1]) - (k[0][1]*k[1][0]))) 
        a_prime = (k[1][1]*inverse_coef) % 26
        b_prime = (-k[0][1]*inverse_coef) % 26
        c_prime = (-k[1][0]*inverse_coef) % 26
        d_prime = (k[0][0]*inverse_coef) % 26
        
        inv_matrix = [[a_prime, b_prime], [c_prime, d_prime]] 
        print(inverse_coef, inv_matrix)
        if len(paire[len(paire)-1]) == 1:
            paire[len(paire)-1]+='X'
            for el in paire:
                P1 = ((inv_matrix[0][0]*dict[el[0]]) + (inv_matrix[0][1]*dict[el[1]])) % 26
                P2 = ((inv_matrix[1][0]*dict[el[0]]) + (inv_matrix[1][1]*dict[el[1]])) % 26
                plain_text += reversed_dict[P1] + reversed_dict[P2]
            return plain_text[0:len(plain_text)-1]
        else:
            for el in paire:
                P1 = ((inv_matrix[0][0]*dict[el[0]]) + (inv_matrix[0][1]*dict[el[1]])) % 26
                P2 = ((inv_matrix[1][0]*dict[el[0]]) + (inv_matrix[1][1]*dict[el[1]])) % 26
                plain_text += reversed_dict[P1] + reversed_dict[P2]
            return plain_text

# Test de la fonction de dechiffrement
print("le mot IWLBHWKX correspond à: ", dechiffrement("IWLBHWKX", [[9, 4], [5, 7]]))

