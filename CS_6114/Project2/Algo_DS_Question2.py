# Function for rook's possible positions
def getRookMoves(pos, chessBoard,explored_positions):
    row, column = list(pos.strip().lower())
    #print(row, column)
    row = int(row)
    column = chess_map_from_alpha_to_index[column]
    solutionMoves = []
    filled_pos = []

    if explored_positions is not None:
        for i in explored_positions:
            r, c = list(i.strip().lower())
            r = int(r)
            c = chess_map_from_alpha_to_index[c]
            filled_pos.append((r, c))

    # To move above
    if row < 8:
        for i in range((row+1),9):
            new_pos = (i,column)
            if new_pos not in filled_pos:
                solutionMoves.append(new_pos)
            else:
                break

    # To move below
    if row > 1:
        for i in range((row-1),0,-1):
            new_pos = (i,column)
            if new_pos not in filled_pos:
                solutionMoves.append(new_pos)
            else:
                break

    # To move left
    if column > 1:
        for i in range((column-1),0,-1):
            new_pos = (row,i)
            if new_pos not in filled_pos:
                solutionMoves.append(new_pos)
            else:
                break

    # To move right
    if column <8:
        for i in range((column+1),9):
            new_pos = (row,i)
            if new_pos not in filled_pos:
                solutionMoves.append(new_pos)
            else:
                break
    # Representing in chess moves
    solutionMoves = ["".join([str(i[0]),chess_map_from_index_to_alpha[i[1]]]) for i in solutionMoves]
    solutionMoves.sort()
    return solutionMoves

# Function for knight's possible positions
def getKnightMoves(pos, chessBoard,explored_positions):
    """ A function that returns the all possible moves
        of a knight stood on a given position
    """
    row, column= list(pos.strip().lower())
    row = int(row)
    column = chess_map_from_alpha_to_index[column]
    i, j = row, column
    solutionMoves = []

    try:
        temp = chessBoard[i + 1][j - 2]
        solutionMoves.append([i + 1, j - 2])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j - 1]
        solutionMoves.append([i + 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i + 2][j + 1]
        solutionMoves.append([i + 2, j + 1])
    except:
        pass
    try:
        temp = chessBoard[i + 1][j + 2]
        solutionMoves.append([i + 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j + 2]
        solutionMoves.append([i - 1, j + 2])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j + 1]
        solutionMoves.append([i - 2, j + 1])
    except:
        pass
    try:
        temp = chessBoard[i - 2][j - 1]
        solutionMoves.append([i - 2, j - 1])
    except:
        pass
    try:
        temp = chessBoard[i - 1][j - 2]
        solutionMoves.append([i - 1, j - 2])
    except:
        pass

    # Filter all negative values
    temp = [i for i in solutionMoves if i[0] >= 1 and i[1] >= 1]
    #print(temp)

    # Represneting in chess moves
    allPossibleMoves = ["".join([str(i[0]),chess_map_from_index_to_alpha[i[1]]]) for i in temp]
    allPossibleMoves.sort()
    #remove already filled positions
    for i in explored_positions:
        for j in allPossibleMoves:
            if i ==j:
                allPossibleMoves.remove(j)

    return allPossibleMoves

# Function for Bishop's possible positions
def getBishopMoves(pos, chessBoard,explored_positions):
    row,column = list(pos.strip().lower())
    row = int(row)
    column = chess_map_from_alpha_to_index[column]
    possibleMoves = []
    filled_pos = []

    if explored_positions is not None:
        for i in explored_positions:
            r, c = list(i.strip().lower())
            r = int(r)
            c = chess_map_from_alpha_to_index[c]
            filled_pos.append((r, c))

    x, y = row, column

    # Move diagonally downwards
    x1 = x - 1
    y1 = y - 1
    while (x1 > 0 and y1 > 0):
        if (x1,y1) not in filled_pos:
            possibleMoves.append((x1, y1))
            y1 -= 1
            x1 -= 1
        else:
            break

    # Move diagonally downward
    x1 = x + 1
    y1 = y - 1
    while (x1 <= 8 and y1 > 0):
        if (x1, y1) not in filled_pos:
            possibleMoves.append((x1, y1))
            x1 = x1 + 1
            y1 = y1 - 1
        else:
            break

    # Move diagonally upwards
    x1 = x + 1
    y1 = y + 1
    while (x1 <= 8 and y1 <= 8):
        if (x1, y1) not in filled_pos:
            possibleMoves.append((x1, y1))
            x1 = x1 + 1
            y1 = y1 + 1
        else:
            break

    # Move diagonally upwards
    x1 = x - 1
    y1 = y + 1
    while (x1 > 0 and y1 <= 8):
        if (x1, y1) not in filled_pos:
            possibleMoves.append((x1, y1))
            x1 = x1 - 1
            y1 = y1 + 1
        else:
            break
    # Representing in chess moves
    possibleMoves = ["".join([str(i[0]),chess_map_from_index_to_alpha[i[1]]]) for i in possibleMoves]

    possibleMoves.sort()

    return possibleMoves

# Function for Queen's possible positions
def getQueenMoves(pos, chessBoard, explored_positions):
    # i, j = row, column
    row, column = list(pos.strip().lower())
    row = int(row)
    column = chess_map_from_alpha_to_index[column]
    possibleMoves = []
    filled_pos = []

    if explored_positions is not None:
        for i in explored_positions:
            r, c = list(i.strip().lower())
            r = int(r)
            c = chess_map_from_alpha_to_index[c]
            filled_pos.append((r, c))

    # Top

    if row < 8:
        for i in range((row + 1), 9):
            new_pos = (i, column)
            if new_pos not in filled_pos:
                possibleMoves.append(new_pos)
            else:
                break

    # Move below
    if row > 1:
        for i in range((row - 1), 0, -1):
            new_pos = (i, column)
            if new_pos not in filled_pos:
                possibleMoves.append(new_pos)
            else:
                break

    # Move to left
    if column > 1:
        for i in range((column - 1), 0, -1):
            new_pos = (row, i)
            if new_pos not in filled_pos:
                possibleMoves.append(new_pos)
            else:
                break

    # Move to right
    if column < 8:
        for i in range((column + 1), 9):
            new_pos = (row, i)
            if new_pos not in filled_pos:
                possibleMoves.append(new_pos)
            else:
                break

    x, y = row, column

    # Move diagonally downward
    x1 = x - 1
    y1 = y - 1
    while (x1 > 0 and y1 > 0):
        if (x1, y1) not in filled_pos:
            possibleMoves.append((x1, y1))
            y1 -= 1
            x1 -= 1
        else:
            break

        # Move diagonally downward
    x1 = x + 1
    y1 = y - 1
    while (x1 <= 8 and y1 > 0):
        if (x1, y1) not in filled_pos:
            possibleMoves.append((x1, y1))
            x1 = x1 + 1
            y1 = y1 - 1
        else:
            break

    # Move diagonally upwards
    x1 = x + 1
    y1 = y + 1
    while (x1 <= 8 and y1 <= 8):
        if (x1, y1) not in filled_pos:
            possibleMoves.append((x1, y1))
            x1 = x1 + 1
            y1 = y1 + 1
        else:
            break

    # Move diagonally upwards
    x1 = x - 1
    y1 = y + 1
    while (x1 > 0 and y1 <= 8):
        if (x1, y1) not in filled_pos:
            possibleMoves.append((x1, y1))
            x1 = x1 - 1
            y1 = y1 + 1
        else:
            break

    possibleMoves = ["".join([str(i[0]),chess_map_from_index_to_alpha[i[1]]] ) for i in possibleMoves]
    possibleMoves.sort()
    return possibleMoves

# Function for King's possible positions
def getkingMoves(pos, chessBoard,explored_positions):
    row, column = list(pos.strip().lower())
    #print(row, column)
    row = int(row)
    column = chess_map_from_alpha_to_index[column]
    solutionMoves = []
    filled_pos = []
    x, y = row, column

    if explored_positions is not None:
        for i in explored_positions:
            r, c = list(i.strip().lower())
            r = int(r)
            c = chess_map_from_alpha_to_index[c]
            filled_pos.append((r, c))

    # Move upwards

    if row < 8:
        new_pos = ((row+1),column)
        if new_pos not in filled_pos:
            solutionMoves.append(new_pos)

    #below
    if row > 1:
        new_pos = ((row-1),column)
        if new_pos not in filled_pos:
            solutionMoves.append(new_pos)

    # Move to left
    if column > 1:
#        for i in range((column-1),0,-1):
        new_pos = (row,(column-1))
        if new_pos not in filled_pos:
            solutionMoves.append(new_pos)

    # Move to right
    if column <8:
#        for i in range((column+1),9):
        new_pos = (row,(column+1))
        if new_pos not in filled_pos:
            solutionMoves.append(new_pos)

    # Move diagonally downward
    x1 = x - 1
    y1 = y - 1
    if (x1, y1) not in filled_pos:
        solutionMoves.append((x1, y1))
        y1 -= 1
        x1 -= 1

    # Move diagonally downward
    x1 = x + 1
    y1 = y - 1

    if (x1, y1) not in filled_pos:
        solutionMoves.append((x1, y1))
        x1 = x1 + 1
        y1 = y1 - 1

    # Move diagonally upwards
    x1 = x + 1
    y1 = y + 1
    if (x1, y1) not in filled_pos:
        solutionMoves.append((x1, y1))
        x1 = x1 + 1
        y1 = y1 + 1

        # Move diagonally upwards
    x1 = x - 1
    y1 = y + 1
    if (x1, y1) not in filled_pos:
        solutionMoves.append((x1, y1))
        x1 = x1 - 1
        y1 = y1 + 1

    solutionMoves = ["".join([str(i[0]),chess_map_from_index_to_alpha[i[1]]]) for i in solutionMoves]
    solutionMoves.sort()
    return solutionMoves


# Function for pawn's possible positions
def getpawnMoves(pos, chessBoard,explored_positions):
    row, column = list(pos.strip().lower())
    #print(row, column)
    row = int(row)
    column = chess_map_from_alpha_to_index[column]
    possibleMoves = []
    filled_pos = []
    x, y = row, column

    if explored_positions is not None:
        for i in explored_positions:
            r, c = list(i.strip().lower())
            r = int(r)
            c = chess_map_from_alpha_to_index[c]
            filled_pos.append((r, c))

    # Move upwards

    if row < 8:
        new_pos = ((row+1),column)
        if new_pos not in filled_pos:
            possibleMoves.append(new_pos)

    x, y = row, column

    # Upward diagonal direction
    x1 = x + 1
    y1 = y - 1
    if (x1, y1) not in filled_pos:
        possibleMoves.append((x1, y1))

    # Upward diagonal direction
    x1 = x + 1
    y1 = y + 1
    if (x1, y1) not in filled_pos:
        possibleMoves.append((x1, y1))

    temp = [i for i in possibleMoves if i[0] >= 1 and i[1] >= 1]

    possibleMoves = ["".join([str(i[0]),chess_map_from_index_to_alpha[i[1]]]) for i in temp]
    possibleMoves.sort()
    return possibleMoves


print('The chess board in the program is assumed to be names as follows\nAll the 8 rows are named using number [1-8]\nAll the 8 columns are named using albhabets [a-h]'
          '\nThe positions are named as 1a,1b,1c,1d,1e,1f,1g,1h\nThe positions are named as 2a,2b,2c,2d,2e,2f,2g,2h')
print('********************* Lets start the game now ***********************')

explored_positions = []
while True:
    chessBoard = [[1, 1, 1, 1, 1, 1, 1, 1] for i in range(8)]

# Dictionries to map alphabets to index and vice versa
    chess_map_from_alpha_to_index = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8
    }

    chess_map_from_index_to_alpha = {
        1: "a",
        2: "b",
        3: "c",
        4: "d",
        5: "e",
        6: "f",
        7: "g",
        8: "h"
    }
    print('You can select one chess piece from the following 1.Rook 2.Knight 3.Bishop 4.Queen 5.King 6.Pawn')
    choice = input("Enter the Piece Name > ")

    if choice == 'exit':
        print("Hope you enjoyed playing the game")
        print("Thank you")
        break
    else:
        if choice == 'Rook':
            print('Enter the position of rook')
            rook_position = input()
            print(rook_position)
            if rook_position not in explored_positions:
                pos = getRookMoves(rook_position, chessBoard,explored_positions)
                for idx, val in enumerate(pos):
                    print('Possible position: ', idx)
                    print(val)
                print('Select the position number ( 0 -', len(pos) - 1, ') you want the pawn to move to')
                piece_choice = input("> ")
                print('Finally selected row details row: ', pos[int(piece_choice)][0], 'column: ',
                      pos[int(piece_choice)][1])
                tmp = pos[int(piece_choice)]
                explored_positions.append(tmp)
                #print('Explored positions',explored_positions)
                print('Do you want to continue [yes/no]')
                user_input = input('> ')
                if user_input =='no':
                    print("Hope you enjoyed playing the game")
                    print("Thank you")
                    break
                elif user_input == 'yes':
                    continue
                else:
                    print('Enter Valid input')
            else:
                print('This position is filled. Please select a different position')
        elif choice == 'Knight':
            print('Enter the position of Knight')
            knight_position = input()
            #print(knight_position)
            if knight_position not in explored_positions:
                pos= getKnightMoves(knight_position, chessBoard,explored_positions)
                for idx, val in enumerate(pos):
                    print('Possible position: ', idx)
                    print(val)
                print('Select the position number ( 0 -', len(pos) - 1, ') you want the pawn to move to')
                piece_choice = input("> ")
                print('Finally selected row details row: ', pos[int(piece_choice)][0], 'column: ',
                      pos[int(piece_choice)][1])
                tmp = pos[int(piece_choice)]
                explored_positions.append(tmp)
                #print('Explored positions', explored_positions)
                print('Do you want to continue [yes/no]')
                user_input = input('> ')
                if user_input =='no':
                    print("Hope you enjoyed playing the game")
                    print("Thank you")
                    break
                elif user_input == 'yes':
                    continue
                else:
                    print('Enter Valid input')
            else:
                print('This position is filled. Please select a different position')
        elif choice == 'Bishop':
            print('Enter the position of Bishop')
            bishop_position = input()
            #print(bishop_position)
            if bishop_position not in explored_positions:
                pos= getBishopMoves(bishop_position, chessBoard,explored_positions)
                for idx, val in enumerate(pos):
                    print('Possible position: ', idx)
                    print(val)
                print('Select the position number ( 0 -', len(pos) - 1, ') you want the pawn to move to')
                piece_choice = input("> ")
                print('Finally selected row details row: ', pos[int(piece_choice)][0], 'column: ',
                      pos[int(piece_choice)][1])
                tmp = pos[int(piece_choice)]
                explored_positions.append(tmp)
                #print('Explored positions', explored_positions)
                print('Do you want to continue [yes/no]')
                user_input = input('> ')
                if user_input =='no':
                    print("Hope you enjoyed playing the game")
                    print("Thank you")
                    break
                elif user_input == 'yes':
                    continue
                else:
                    print('Enter Valid input')
            else:
                print('This position is filled. Please select a different position')
        elif choice == 'Queen':
            print('Enter the position of Queen')
            queen_position = input()
            #print(queen_position)
            if queen_position not in explored_positions:
                pos= getQueenMoves(queen_position, chessBoard,explored_positions)
                for idx, val in enumerate(pos):
                    print('Possible position: ', idx)
                    print(val)
                print('Select the position number ( 0 -', len(pos) - 1, ') you want the pawn to move to')
                piece_choice = input("> ")
                print('Finally selected row details row: ', pos[int(piece_choice)][0], 'column: ',
                      pos[int(piece_choice)][1])
                tmp = pos[int(piece_choice)]
                explored_positions.append(tmp)
                #print('Explored positions', explored_positions)
                print('Do you want to continue [yes/no]')
                user_input = input('> ')
                if user_input =='no':
                    print("Hope you enjoyed playing the game")
                    print("Thank you")
                    break
                elif user_input == 'yes':
                    continue
                else:
                    print('Enter Valid input')
            else:
                print('This position is filled. Please select a different position')
        elif choice == 'King':
            print('Enter the position of King')
            king_position = input()
            #print(queen_position)
            if king_position not in explored_positions:
                pos= getkingMoves(king_position, chessBoard,explored_positions)
                for idx, val in enumerate(pos):
                    print('Possible position: ', idx)
                    print(val)
                print('Select the position number ( 0 -', len(pos) - 1, ') you want the pawn to move to')
                piece_choice = input("> ")
                print('Finally selected row details row: ', pos[int(piece_choice)][0], 'column: ',
                      pos[int(piece_choice)][1])
                tmp = pos[int(piece_choice)]
                explored_positions.append(tmp)
                #print('Explored positions', explored_positions)
                print('Do you want to continue [yes/no]')
                user_input = input('> ')
                if user_input =='no':
                    print("Hope you enjoyed playing the game")
                    print("Thank you")
                    break
                elif user_input == 'yes':
                    continue
                else:
                    print('Enter Valid input')
            else:
                print('This position is filled. Please select a different position')
        elif choice == 'Pawn':
            print('Enter the position of Pawn')
            pawn_position = input()
            #print(queen_position)
            if pawn_position not in explored_positions:
                pos = getpawnMoves(pawn_position, chessBoard,explored_positions)
                for idx, val in enumerate(pos):
                    print('Possible position: ', idx)
                    print(val)
                print('Select the position number ( 0 -', len(pos) - 1, ') you want the pawn to move to')
                piece_choice = input("> ")
                print('Finally selected row details row: ', pos[int(piece_choice)][0], 'column: ',
                      pos[int(piece_choice)][1])
                tmp = pos[int(piece_choice)]
                explored_positions.append(tmp)
                print('Explored positions', explored_positions)
                print('Do you want to continue [yes/no]')
                user_input = input('> ')
                if user_input =='no':
                    print("Hope you enjoyed playing the game")
                    print("Thank you")
                    break
                elif user_input == 'yes':
                    continue
                else:
                    print('Enter Valid input')
            else:
                print('This position is filled. Please select a different position')
        else:
            print('Please enter name of the piece correctly')