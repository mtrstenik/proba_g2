# for x in range(6):
#     for y in range(5):
#         print("#", end="")
#     print("za")


for x in range(10):
    for y in range(10):
        if y > x:
            print("#", end="")
        else:
            print(" ", end="")
    print()


automobil = 0
cilj = 100

brzina = 10
while automobil < cilj:
    print("Voznja je u toku.")
    automobil += brzina
else:
    print("Stigli ste.")