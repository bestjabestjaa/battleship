from random import randint

grid = []

for i in range(5):
    grid.append(['O']*5)

#tworzenie planszy do gry
def print_grid(grid):
    for i in grid:
        print (str(" ".join(i)))

#definiowanie funkcji - generowanie losowego polozenia statku
def random_row(grid):
    return randint(0, len(grid)-1)

def random_col(grid):
    return randint(0, len(grid)-1)
def legend():
    print ("Legenda:\nX-odgadnięte, puste pola\nW-odgadnięte, zwycięskie pole")

#przypisanie zmiennych funkcjom
ship_row = random_row(grid)
ship_col = random_col(grid)

print ("Statek-wiersz: " + str(ship_row) + "\nStatek-kolumna: " + str(ship_col))

#dzialanie programu
print ("\nWitaj w grze STATKI\nTwoja plansza do gry: ")
print_grid(grid)

for turn in range(4):
    print("\nTura: " + str(turn + 1))

    try:
        guess_row = int(input("Zgadnij wiersz, pod którym kryje się statek "))
        guess_col = int(input("Zgadnij kolumnę, pod którym kryje się statek "))
        #print ("\n")
    except ValueError:
        print ("Nie podałeś liczby całkowitej")
        continue
    else:
        '''if not (1 <= guess_row <= 5) and not (1 <= guess_col <= 5):
            print ("Musisz podać cyfry z przedziału 1-5")'''

        if guess_row-1 == ship_row and guess_col-1 == ship_col:
            print ("Gratulacje! Udało ci się odgadnąć położenie statku")
            grid[guess_row-1][guess_col-1] = 'W'
            print_grid(grid)
            legend()
            break
        else:
            if (guess_row-1 < 0 or guess_row-1 > 4) or (guess_col-1 < 0 or guess_col-1 > 4):
                print ("Wygląda na to, że to nie jest już ocean! Spróbuj jeszcze raz!")
            elif grid[guess_row-1][guess_col-1] == 'X':
                print ("Już wskazałeś to pole, spróbuj wpisać inne dane")
            else:
                print ("Nie udało ci się podać współrzędnych statku!")
                grid[guess_row-1][guess_col-1] = 'X'
                print_grid(grid)
                legend()

if turn == 3:
    print ("Gra została zakończona")