def znak_do_liczby (znak):
    znaki = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    return znaki[znak]

def rzymska_do_arabskiej(liczba_rzymska):
    liczba_arabska = 0
    for i in range(len(liczba_rzymska)):
        if i > 0:
            if znak_do_liczby(liczba_rzymska[i]) > znak_do_liczby(liczba_rzymska[i - 1]):
                liczba_arabska += znak_do_liczby(liczba_rzymska[i]) 
                liczba_arabska -= 2 * znak_do_liczby(liczba_rzymska[i - 1])
            else:
                liczba_arabska += znak_do_liczby(liczba_rzymska[i])
        else:
            liczba_arabska += znak_do_liczby(liczba_rzymska[i])
    return liczba_arabska


def arabska_do_rzymskiej (liczba_arabska):
    liczby = {
        1 : "I",
        4: "IV",
        5 : "V",
        9 : "IX",
        10 : "X",
        40: "XL",
        50 : "L",
        90: "XC",
        100 : "C",
        400 : "CD",
        500 : "D",
        900 : "CM",
        1000 : "M"
    }
    liczba_rzymska = ""

    while liczba_arabska != 0:
        ile_odjac = 0
        for i in liczby:
            if i > ile_odjac and i <= liczba_arabska:
                ile_odjac = i
        liczba_arabska -= ile_odjac
        liczba_rzymska += liczby[ile_odjac]
    return liczba_rzymska