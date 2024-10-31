dziennik = {}

def dodaj_studenta ():
    imie = input("podaj imie: ")
    nazwisko = input("podaj nazwisko: ")
    indeks = int(input("Podaj numer indeksu: "))

    if indeks in dziennik:
        print("student już istneije!!!")
    else:
        dziennik[indeks] = (imie, nazwisko)

def wyszukaj_studenta ():
    indeks = int(input("Podaj numer indeksu studenta do wyszukania: "))
    
    if indeks in dziennik:
        imie, nazwisko = dziennik[indeks]
        print("student o numerze:", indeks, "nazywa się:",imie, nazwisko)
    else:
        print("student nie istnieje!!!")
def usun_studenta ():
    indeks = int(input("Podaj numer indeksu studenta do usunięcia: "))
    if indeks in dziennik:
        del dziennik[indeks]
    else:
        print("student nie istnieje!!!")
def wypisz_studentow ():
    if not dziennik:
        print("dziennik jest pusty!!!")
    for i in dziennik:
        imie, nazwisko = dziennik[i]
        print("student o numerze:", i, "nazywa się:",imie, nazwisko)

dziennik[1]=("jan", "kowalski")
dziennik[2]=("ala", "kowalczyk")

def main():
    while True:
        print(" 1=dodaj studenta \n 2=usun studenta \n 3=wyszukaj studenta \n 4=wyswietl studentów \n 5=koniec")
        wybor=int(input("numer: "))

        if wybor == 1:
            dodaj_studenta ()
        elif wybor ==2:
            usun_studenta ()
        elif wybor ==3:
            wyszukaj_studenta ()
        elif wybor ==4:
            wypisz_studentow ()
        elif wybor ==5:
            break


if __name__ == "__main__":
    main ()
