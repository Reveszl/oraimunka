szamok=[3,4,2,7,8,1,9,7,3]

#összegzés tétele

osszeg=0
for x in szamok:
    osszeg=osszeg+x
print(osszeg)
print (sum(szamok))

#eldöntés tétele

vane=False
for x in szamok:
    if (x==1):
        vane=True
print(vane)

#megszámlálás

db=0
for x in szamok:
    if x==3:
        db=db+1;
print("Ez a hármasok darabszáma")
print(db)

#feltételes összegzés csak a páros számokat összegzem
print("A páros számok összege: ")
osszeg=0
for x in szamok:
    if x%2==0:
        osszeg=osszeg+x
print(osszeg)

#minimum kiválasztás tétele
print("minimum kiválasztás tétele")
min1=1000
for x in szamok:
    if x<min1:
        min1=x
print(min1)
print(min(szamok))

#maximum kiválasztás tétele

print("maximum kiválasztás tétele")

max1=-1000
for x in szamok:
    if x>max1:
        max1=x
print(max1)
print(max(szamok))

#Feladat:
#számok átlaga
szamok=[9,36,27,31,75,63,41,69,24,45]
db=0
for x in szamok:
   db=db+1
print(sum(szamok)/db)
print(sum(szamok))

#Legkisebb
min1=1000
for x in szamok:
    if x<min1:
        min1=x
print(min1)

#Legnagyobb
max1=-1000
for x in szamok:
    if x>max1:
        max1=x
print(max1)
#van páros?
paros=False
for x in szamok:
    if x%2==0:
        paros=True
        print(x)
print(paros)
#50-nél nagyobbak összege
nagyobb=0
for x in szamok:
   if x>50:
       nagyobb=nagyobb+x
print(nagyobb)
#9-esek száma
szam=0
for x in szamok:
    if x==9:
        szam=szam+1
print(szam)