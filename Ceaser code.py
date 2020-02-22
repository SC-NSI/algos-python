import string
import collections





def caesar():
    #lettre+cle=crypt
    code=[]
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    message=input("saisir votre message a coder : ")

    cle=int(input("saisir votre cle: "))
    for lettre in message:

        #print(alphabet.index(lettre))
        #print(alphabet.index(lettre)+cle)
        i=alphabet.index(lettre)
        if(i+cle>25):
            i=i-25
        print(alphabet[i+cle])


def newcaesar(text,cle):

        upper = collections.deque(string.ascii_uppercase)
        lower = collections.deque(string.ascii_lowercase)

        upper.rotate(cle)
        lower.rotate(cle)

        upper = ''.join(list(upper))
        lower = ''.join(list(lower))

        return text.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))





