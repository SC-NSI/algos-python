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




def insertion_sort_in_place(t):

    for i in range(1, len(t)):
        insert(t,i)

    return t




def testinsertion_sort_in_place():
    t=[9,8,7,6,5,4,3,2,1]

    for i in range(1, len(t)):
        insert(t,i)

    return t