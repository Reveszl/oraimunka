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
