def ka1 (t):
    i=0
    for index in range(len(t)-1):
        for index in range(len(t)-1):
            if t[index] > t[index+1]:
                temp = t[index]
                t[index]=t[index+1]
                t[index+1]=temp
                index =index-1
            #else:
            #    index +=1      pas necessaire
    return(t)


def ka2 (t):
    i=0

    for index in range(len(t)-1):

        if t[index] > t[index+1]:
            temp = t[index]
            t[index]=t[index+1]
            t[index+1]=temp
            ka2(t)



        #else:
        #   index +=1         pas necessaire

    return(t)


def ka3 (t):
    i=0

    for index in range(len(t)-1):
        if t[index] > t[index+1]:
            temp = t[index]
            t[index]=t[index+1]
            t[index+1]=temp
            index =-1
            #else:
            #    index +=1      pas necessaire
    return(t)

'''Test'''

def testka1():
    t=[8,5,9,2,3,1]
    i=0
    for index in range(len(t)-1):
        for index in range(len(t)-1):
            if t[index] > t[index+1]:
                temp = t[index]
                t[index]=t[index+1]
                t[index+1]=temp
                index =index-1
            #else:
            #    index +=1      pas necessaire
    return(t)


def testka2():
    t=[8,5,9,2,3,1]
    i=0

    for index in range(len(t)-1):

        if t[index] > t[index+1]:
            temp = t[index]
            t[index]=t[index+1]
            t[index+1]=temp
            ka2(t)



        #else:
        #   index +=1         pas necessaire

    return(t)


def testka3():

    t=[8,5,9,2,3,1]
    i=0
    for index in range(len(t)-1):
        if t[index] > t[index+1]:
            temp = t[index]
            t[index]=t[index+1]
            t[index+1]=temp
            index =-1
            #else:
            #    index +=1      pas necessaire
    return(t)

