import string
import random

if __name__=="__main__":

    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation


Plen = int(input("Enter password length\n"))

S=[]

S.extend(list(s1))
S.extend(list(s2))
S.extend(list(s3))
S.extend(list(s4))

#print(s)
#random.shuffle(s)
#print(s)

print("yourv password is: ")
#print("".join(s[0:plen]))

print("".join(random.sample(S,Plen)))