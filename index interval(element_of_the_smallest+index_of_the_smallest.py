def element_of_the_smallest(list,start,stop):
    if start >= stop:
        fin=start
        debut=stop
    else:
        fin=stop
        debut=start
    for element in list:

        if element >= debut and element <= fin:
            print (element)

def index_of_the_smallest(list,start,stop):
    index=0


    if start >= stop:
        fin=start
        debut=stop
    else:
        fin=stop
        debut=start

#important
    for  element in list:
        if element >= debut and element <= fin:
            print (index)
            index +=1
        else:
            index +=1


