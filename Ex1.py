def saisie() :
  a=float(input("enter la note :"))
  if a<0 or a>20 :
   print("cette note inacseptable")
   saisie()
  else :
   return a
   
    

def moyen(a,b,c):
  somme=a+b+c
  m=somme/3
  if m>=16 :
   print("tres bien")
  elif m>=14 :
   print("bien")
  elif m>=12 :
   print("assez bien")
  elif m>=10 :
   print("Passable")
  else  :
   print("Insuffisant")
 
 
print("saisie les note")

for i in range(3) :
 ai=float(input("enter la note "+str(i+1)+":"))
 if ai<0 or ai>20 :
  print("cette note inacseptable")
  a=saisie()
 else :
  a=ai
 
 

moyen(a,a,a)
 