import random


x = 10

if x > 0:
    print("broj x je pozitivan")

print("Izvrsava se u svakom slucaju")

vozilo_u_pokretu = True
brzina = 60

if vozilo_u_pokretu == True:
    print("Vozilo se krece...")
    print("Proverite i brzinu...")
    if brzina > 50:
        print("Prekoracena brzina")
    print("Ovo izvrsavam kolika god da je brzina")
    if brzina <= 50:
        print("Brzina je OK.")

if vozilo_u_pokretu == False:
    print("Vozilo nije u pokretu")






proizvod = "duks"
cena = 3000

# komanda = int(input("Unesite komandu: "))


# if komanda == 1:
#     print("Prikazi proizvode")
#     print("Proizvod:", proizvod, "Cena:", cena)
# if komanda == 2:
#     print("Kupovina...")
#     stanje = int(input("Unesite stanje na racunu: "))
#     if stanje >= cena:
#         print("Uspesna kupovina!")
#     if stanje < cena:
#         print("Neuspesna kupovina...")
# if komanda == 3:
#     print("Izlaz")

# broj = 5
# if broj > 0:
#     print("Broj je veci od 0.")
# else:
#     print("Broj je 0 ili manji od 0.")

# marija = 
# ksenija = True


# devojka_na_dejtu = ""
# if marija:
#     devojka_na_dejtu = "marija"
# elif katarina:
#     devojka_na_dejtu
# elif ksenija:
#     devojka_na_dejtu = "ksenija"
# else:
#     devojka_na_dejtu = "sofija"

# print("Izlazi sa mnom:", devojka_na_dejtu)


# automobil_polovan = True
# godiste = 2021
# boja = "crna"


# if (automobil_polovan == True or godiste > 2017) and boja == "crna":
#     print("Kupujem")

# if not automobil_polovan:
#     print("Automobil je nov.")
# prisutan = False
# if prisutan:
#     print("Na casu je")
# if not prisutan:
#     print("Nije na casu")


#     trenutni_rezultat = random.randint(1, 100)
#     novi_rezultat = int(input("Unesite novi broj (od 1 do 100): "))

#     if novi_rezultat > 100 or novi_rezultat < 1:
#         print("Proverite broj, dozvoljeno od 1 do 100")
#     else:
#         print("Trenutni broj:", trenutni_rezultat, "Novi:", novi_rezultat)
#         if trenutni_rezultat < novi_rezultat:
#             print("Pobedili ste!")
#         elif trenutni_rezultat == novi_rezultat:
#             print("Identicne vrednosti!!!")
#         else:
#             print("Izgubili ste")

pol = input("Unesite pol: ")
poruka = ""
if pol == "m":
    poruka = "Hey mister!"
else:
    poruka = "Hey miss!"

poruka = "Hey mister!" if pol == "m" else "Hey miss!"
print(poruka)


popularan_proizvod = ""
jesen = False
if jesen:
    print("Popularan proizvod: ajvar")
else:
    print("Popularan proizvodsladoled")


    