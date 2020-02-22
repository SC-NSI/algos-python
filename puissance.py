def puissance(n):
    """n compris entre 1 et 600
    si n>7000 retourne l'erreur 0"""
    resultat=2
    if n==1:
        return resultat
    elif n>7000:
        return(0)
    else:
        for i in range(n):
            resultat=resultat*2
    return resultat