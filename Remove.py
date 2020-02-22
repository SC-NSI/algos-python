def remove(t,i):

    resultat=[0]*(len(t)-1)
    for j in range(len(t)):
        if j<i:
            resultat[j]=t[j]
        if j>i:
            resultat[j-1]=t[j]

    return resultat
