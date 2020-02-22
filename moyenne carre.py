
def moyenne():
    n=(int(input("nb eleves=")))
    somme=0
    for ele in range(n):
        note=int(input("notes eleve n°"+ str(ele+1)+ " ?"))
        somme+=note
        moyenne=somme/n
    print("Moyenne classe="+str(moyenne))
    
def xcarre():
    n= int(input("donnez un entier"))
    resultat=2
    if n==1:
        return(resultat)
    
    else:
        for occurence in range(n-1):
            resultat=resultat*2
        return(resultat)
   
    