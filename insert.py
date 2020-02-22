def swap(t,i,j):

    save=t[i]
    t[i]=t[j]
    t[j]=save

    return t



def insert(t,i):

    for index in range(i,0,-1):
        if t[index] < t[index-1]:
            swap(t, index-1, index)
        else:
            break

    return t



def testinsert():
    t=[3,4,2]
    i=2
    insert(t,i)
    return t
