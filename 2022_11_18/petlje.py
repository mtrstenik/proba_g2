pozicija_automobila = 0
pozicija_cilja = 10

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

for ime in ["marko", "milos", "marija", "ana", "sofija"]:
    print("Hello", ime)

print("Prva sledeca linija...")

for broj in [1, 2, 3, 4, 5, 6, 7]:
    print("Ovo je broj:", broj)

range(1, 21)
for broj in range(5, 10, 2):
    print("Stampanje broja:", broj)

for broj in range(100, 0, -1):
    print("Prikaz", broj)


pozicija_automobila = 0
pozicija_cilja = 10
for kretanje in range (5):
    pozicija_automobila +=2
    print(pozicija_automobila == pozicija_cilja)


print("***************Allowed years*********************")
startDate = 2010
endDate = 2020
for opseg in range(2010, 2020):
    print(opseg)
print("***************************************************")



print("1\t2\t3\t")
print("*****************")

print(1 * 1, end="\t")


# for brojac in range(1, 6):
#     print(brojac * 1, end="\t")
#     print(brojac * 2, end="\t")
#     print(brojac * 3, end="\t")


for x in range (5):
    for y in range(3):
        print("Ovo je x:", x, "Ovo je y:", y)

for x in range(6):
    for y in range(6):
        print("*", end=" ")
    print() 

for x in range(10):
    for y in range(10):
        print("*", end=" ")
        if x == y:
    print()


for x in range(10):
    for y in range(10)