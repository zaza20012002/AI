T=int(input("enter T:"))
heure=T//3600
reste=T%3600
minute=reste//60
secende=reste%60
print("pour T les heurs est",heure,"h",minute,"min",secende,"s")
