import random 
import string 

def generete_password(length):

    characters =  string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = 8 
password = generete_password(length)
print ("parol: ", password)
