

def boter_kaas_eieren():
    print ()
    print ('TechGrounds TIC TAC TOE')
    print ()
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]#De posities op het bord
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) #Er zijn slechts een aantal combinaties die winnen

    def draw(): # Dit zijn de morgelijkheden om te verliezen
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nDat mag niet, nog een keer")
            p1()
        else:
            board[n] = "X"

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nDat mag niet, nog een keer")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nDat mag niet, nog een keer")#Omdat de positie al gekozen is
                        continue
                except ValueError:
                   print("\nDat mag niet, nog een keer")#ook hieromdat de positie al gekozen is 
                   continue

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Speler1 wint!\n")
                print("Gefeliciteerd!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Speler 2 wint!\n")
                print("Gefelictieerd!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("Het is gelijkspel\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Speler 1 mag kiezen")
        p1()
        draw()
        end = check_board()
        if end == True:
            break
        print("Speler 2 mag kiezen")
        p2()

    if input("Nog een keer? (j/n)\n") == "j":
        print()
        boter_kaas_eieren()

boter_kaas_eieren()