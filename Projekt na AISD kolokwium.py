
class Tba_ros_g:
    zajetosc : int
    pojemnosc : int

    def __init__(self):
        self.dane = [None, None]
        self.zajetosc = 0
        self.pojemnosc = 2

    def lista_z_None(self):
        n = 2
        if len(self.dane)<=2 and self.dane[1] == None:
            self.dane2 =2*[None]
            self.dane2[0] = str(self.dane[0])
            self.zajetosc = 1
            return self.dane2

        if len(self.dane)<=2:
            self.dane2 = 2 * [None]

        else:
            while n < len(self.dane):
                n = n * 2
                self.pojemnosc = n
            self.dane2 = n * [None]

        for i in range(0, len(self.dane)):
            self.dane2[i] = str(self.dane[i])
        self.zajetosc = len(self.dane)

        return self.dane2

    def ustal(self, idx, wartosc):

        if  len(self.dane) == 2 and idx == 0:
            self.dane[0] = wartosc
            return self.lista_z_None()

        if len(self.dane) == 2 and idx != 0:
            for i in range(0, 2):
                if self.dane[i] == None:
                    self.dane[i] = ''

        dl_dane = len(self.dane)
        self.dane += ((idx+1)-dl_dane)*['']
        self.dane[idx] = wartosc

        return self.lista_z_None()

    def pobierz(self, idx):

        if idx > len(self.dane):
            return "[ ]"
        else:
            return f'indek:{idx} wartość:{self.dane[idx]}'

    def dodaj_za_koniec(self,wartosc):

        dl = len(self.dane)
        return  self.ustal(dl, wartosc)

    def dodaj_przed(self, idx, wartosc):

        if len(self.dane)<idx:
           return self.ustal(idx,wartosc)

        if self.zajetosc == 0 and idx < 2:
            self.dane[idx] = wartosc
            if idx == 1:
                return self.ustal(idx,wartosc)
            return self.lista_z_None()

        if self.zajetosc == 1 and idx == 0:
            self.dane.insert(idx,wartosc)
            self.dane = [i for i in self.dane if i is not None]
            return self.lista_z_None()

        if self.zajetosc == 1 and idx ==1:
            self.dane[idx] = wartosc
            return self.lista_z_None()

        self.dane.insert(idx, wartosc)

        return self.lista_z_None()

    def uprosc(self):

        while self.pojemnosc/2 < len(self.dane2):
            for i in range(int(self.pojemnosc - self.pojemnosc/2)):
                self.dane2.pop(-1)

    def print(self):

        if self.dane == [None,None]:
            print(';;')
            return 0
        for i in range(len(self.dane2)):
            if self.dane2[i] is not None:
                if self.dane2[i] == '':
                    print(';', end=' ')
                else:
                    print(self.dane2[i], end=' ')

    def sortuj(self):
        n = len(self.dane)
        for i in range(0, n - 1):
            miejsce = i
            for j in range(i + 1, n):
                if self.dane2[j] < self.dane2[miejsce] :
                    miejsce = j
            self.dane2[i], self.dane2[miejsce] = self.dane2[miejsce], self.dane2[i]


    def __str__(self):
        if self.dane == [None,None]:
            return str(self.dane)

        return  str(self.dane2)

tablica = Tba_ros_g()
#tablica.print()
#tablica.ustal( 1,8)
#tablica.ustal(0,8)
#tablica.ustal(5,8)
#tablica.sortuj()
#tablica.dodaj_przed(4,3)
#tablica.dodaj_przed(0,2)
#tablica.dodaj_przed(0,1)
#tablica.dodaj_przed(0,2)
#tablica.dodaj_przed(0,2)
#tablica.dodaj_przed(0,4)
#tablica.dodaj_przed(0,7)
#tablica.dodaj_przed(6,21)

#tablica.ustal(1,5)
#tablica.ustal(4, 3)
#tablica.ustal(0, 3)
#tablica.ustal(6, 67)
#tablica.ustal(5, 7)
#tablica.ustal(2, 7)
#tablica.dodaj_za_koniec(4)
#tablica.dodaj_przed(2, 4)
#tablica.dodaj_przed(1, 444)
#tablica.sortuj()
print(tablica)

#print(tablica.pobierz(1))
