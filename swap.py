def swap(t,i,j):

    save=t[i]
    t[i]=t[j]
    t[j]=save

    return t

def swap2(t,i,j):

    t[i] , t[j] = t[j] , t[i]

    return t




def testswap():

    t=[8,9]
    i=0
    j=1

    save=t[i]
    t[i]=t[j]
    t[j]=save

    return t




def testswap2():

    t=[8,9]
    i=0
    j=1

    t[i] , t[j] = t[j] , t[i]

    return t
