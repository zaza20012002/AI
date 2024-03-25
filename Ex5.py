nombre1=int(input("enter le nombre entier 1: "))
nombre2=int(input("enter le nombre entier 2: "))
operation=str(input("enter l'operation choisie: "))
if operation=="+"  :
 resultat=nombre1 + nombre2 
elif operation=="-":
 resultat=nombre1 - nombre2 
elif operation=="*":
 resultat=nombre1 * nombre2  
elif operation=="/":
 resultat=nombre1 / nombre2 
else :
 resultat=0 

print("------------------------------")

if resultat==0 :
 print("operation non trouvable")
else :
 print(nombre1,operation,nombre2,"=",resultat)
