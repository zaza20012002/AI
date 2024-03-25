nombre=int(input("entre un nombre :"))
print("les dix nombres suivie de se nombre est : ")
x=10
f=nombre+x
for i in range(nombre,f,1) :
    print(i," ; ")

print(" ,fin")

 #on utilisant while
"""
i=0
tmp=nombre
while i<10 :
    tmp=nombre+1
    print(tmp," ; ")
    nombre=tmp
    i=i+1

print("-------fin")
"""
