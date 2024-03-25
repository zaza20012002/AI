 
def impot(situ,age) :
  if situ=="homme" and age>20 :
    print("il faut paient l'impot")
  elif situ=="femme" and age>18 and age<35 :
    print("il faut paient l'impot")
  else :
    print("il ne paient pas d'impot")


situ=str(input("enter la situation homme/femme :"))
age=int(input("enter l'age :"))
impot(situ,age)
