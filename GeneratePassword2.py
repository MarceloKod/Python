
'''
Gerador de senhas, o usauario vai digitar quantas letras, numeros e caracteres especiais ele quer em sua senha.
O gerador, pode gerar a senha em uma ordem, sendo essa letra, numeroe caracteres especiais.
Ex: Ab12*(
Ou a senha pode ser gerada de uma forma randomica.
Ex: 1A*b(5

Cabe ao usuario  final escolher entre as duas formas de senha

pesquisei sobre o shuffle na list, como usar o randint, como adicionar as coisas na ordem em uma list
'''
import random
from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q' ,'R', 'S', 'T', 'U', 'V', 'W', 'X' ,'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("PASSWORD GENERATOR WITH PYTHON")
print('''Wellcome!\nWhere we gonna generate a password for.''')

#=================================================================================
quantityLetters = input("How many letters do you want in your password?\n")

if(quantityLetters.isnumeric()):#verify if the answer is numeric
    quantityLetters = int(quantityLetters)#transform str to int
    if(int(quantityLetters)>=0):
        while(quantityLetters > 0):
            password.append(letters[randint(0,len(letters)-1)])
            quantityLetters -= 1 

else:
    print("Error. I considered your answer as 0(zero). Next time try putting just natural numbers in the answer")
    exit()
#=================================================================================
quantityNumbers = input("How many nunbers do you want in your password?\n")

if(quantityNumbers.isnumeric()):
    quantityNumbers = int(quantityNumbers)
    if(int(quantityNumbers)>=0):
        while(quantityNumbers > 0):
            password.append(numbers[randint(0,len(numbers)-1)])
            quantityNumbers -= 1 

else:
    print("Error. I considered your answer as 0(zero). Next time try putting just natural numbers in the answer")
    exit()
#=================================================================================
quantitySymbols = input("How many symbols do you want in your password?\n")

if(quantitySymbols.isnumeric()):
    quantitySymbols = int(quantitySymbols)
    if(int(quantitySymbols)>=0):
        while(quantitySymbols > 0):
            password.append(symbols[randint(0,len(symbols)-1)])
            quantitySymbols -= 1 

else:
    print("Error. I considered your answer as 0(zero). Next time try putting just natural numbers in the answer")
    exit()


print('''


OK, almost there!
The last step select if you want your password as:
1 - in order, maybe easier to remember 
-> exemple: Abc123(*$
2 - random order more difficult to remember
-> exemple: DE4*5f$6/''')  
option = input("with type do you want 1 or 2?\n")
if(option == "1"):
    print("Your generate password is:\n" + "".join(password))
elif(option == '2'):
    random.shuffle(password)
    print("Your generate password is:\n" + "".join(password))
else:
    print("Error. Try putting just natural numbers in the answer")
