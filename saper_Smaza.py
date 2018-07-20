import random
import numpy
import numpy as np

def get_number_of_mines(size):
    max_mines = int(size)*int(size) - 1
    answer = input("podaj ilosc min zakres od 1 do " + str(max_mines) + " ")
    return int(answer)

def random_mine(size):
    x = random.randint(0,size-1)
    y = random.randint(0,size-1)
    return (x,y)

def deploy_mines(number_of_mines,size):
    locations = []
    for i in range(number_of_mines):
        location_mine = random_mine(size)
        locations.append(location_mine)
        if locations.count(location_mine) == 0:
            locations.append(location_mine)
        else:
           random_mine(size)
    return locations

def create_board(list_mines, size): 
    big_board=[]
    line=[]
    for i in range(size+2):
        line.append(0)
        
    for i in range(size+2):
        big_board.append(line)

    big_board = numpy.array(big_board)
    
    for mine in list_mines:
        x = mine[0]+1
        y = mine[1]+1
        
        for a in range(x-1,x+2):
            for b in range(y-1,y+2):
                if (a,b) != (x,y):
                    big_board[a,b] += 1

        for mine in list_mines:
            x = mine[0] + 1
            y = mine[1] + 1
            big_board[x,y] = 9

    return big_board

def star_board(size):
    star_board=[]
    line=[]
    for i in range(size+2):
        line.append('*')    
    for i in range(size+2):
        star_board.append(line)

    star_board = numpy.array(star_board)    
    
    return star_board    

def win_board(board, star_board):
    copy_star_board = np.copy(star_board)
    
    for i in range(1,board.shape[0]-1):
        for j in range(1,board.shape[1]-1):
            if board[i,j] != 9:
                copy_star_board[i,j] = board[i,j]    

    return copy_star_board

def reveal_squears(x,y, board, star_board):
    dl = star_board.shape[0]-2
    if star_board[x,y] == '*':
        if x>=1 and x<=dl and y>=1 and y<=dl:
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):             
                    if board[x,y] == 0:
                        star_board[x,y] = board[x,y]                
                        reveal_squears(i,j, board, star_board)
                    if board[x,y] != 9:
                        star_board[x,y] = board[x,y]
        
    return star_board

def print_board(star_board, board, win):
    dl = star_board.shape[0]
    if str(star_board) == str(win):
        print(board[1:11,1:11])
        print ("Zwyciestwo")
    else:
        print(star_board[1:dl-1,1:dl-1])
        wspl_x = input("Podaj wspolrzedna x: ")
        wspl_y = input("Podaj wspolrzedna y: ")
      
        if board[int(wspl_x)+1, int(wspl_y)+1] == 9:
            star_board[int(wspl_x)+1, int(wspl_y)+1] = 9
            print(star_board[1:11,1:11])
            print ("Przegrana!!!")
        else:
            l = reveal_squears(int(wspl_y)+1, int(wspl_x)+1, board, star_board)
            print_board(star_board, board, win)

def game():
    pyt = input("Podaj rozmiar: ")
    size = int(pyt)

    number_of_mines = get_number_of_mines(size)
    list_mines = []
    list_mines = deploy_mines(number_of_mines,size)

    board = create_board(list_mines, size)
    stars_board = star_board(size)

    win = win_board(board, stars_board)
    print_board(stars_board, board, win)

game()
