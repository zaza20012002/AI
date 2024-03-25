import math 
def delta(a,b,c):
    delt=b**2 - (4*a*c)
    return delt

def condi(dele,a,b,c) :
    if dele<0 :
     print("pas de solution")
    elif dele==0 :
     sol=-(b/2*a)
     print("la solution est :" ,sol)
    else :
     sol1=(-b+math.sqrt(dele)/2*a)
     sol2=(b+math.sqrt(dele)/2*a)
     print("les solution de l'équation est",sol1,"et",sol2)

print("enter l'equation")
a=int(input("enter a d'équation"))
b=int(input("enter b d'équation"))
c=int(input("enter c d'équation"))

dele = delta(a,b,c)
condi(dele,a,b,c)


