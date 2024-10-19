n=int(input("unesi broj takmicara:"))
maks=0
for i in range(n):
    skok=float(input("unesi koliko je skacio"))
    if(skok>maks):
        maks=skok
print(maks)
