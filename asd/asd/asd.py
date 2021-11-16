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