def swap(t,i,j):

    save=t[i]
    t[i]=t[j]
    t[j]=save

    return t

def swap2(t,i,j):

    t[i] , t[j] = t[j] , t[i]

    return t