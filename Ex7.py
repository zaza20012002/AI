import math
nombre=int(input("entrer un nombre entier nom null : "))
resultat=0
if nombre==0 :
    print("le nombre et null")
else :
    for i in range(1,nombre+1):
     temp=i**2
     print(temp)
     resultat+=temp
print("le resultat est :",resultat)

