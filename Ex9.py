nombre=int(input("enter un nombre :"))
resultat=0
for i in range(1,nombre):
    if nombre%i==0 :
        temp=i
        resultat+=temp
    else :
        continue

if resultat==nombre :
 print("le nombre est parfait")
else :
   print("le nombre est non parfait")
        