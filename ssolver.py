import time

puzzle = open("in1.txt", "r")
l = []
for line in puzzle:
    l.append(line)
puzzle.close()

#this function allows us to give coordinates of the number we want to print. (r,c) = (row, column)
def get_item(r,c):
    r -= 1
    c -= 1
    num = l[r].split()

    return num[c] 

#prints the numbers that we get when going across sudoku puzzle in a diagonal from top left --> bottom right
#row = 1
#while row <= 9:
#    #print(get_item(row,row))
##    row += 1
#    time.sleep(2)



#prints the numbers that we get when going across sudoku puzzle in a diagonal from top left --> bottom right
#ro = 1
#co = 9
#while 1 <= ro < 9 and 1 < co <= 9:
#    print(get_item(ro,co))
#    ro += 1
#    co -= 1

#print numbers row by row
#r = 1
#c = 1

#while c <= 9:
#    #print(get_item(r,c))
    #time.sleep(0)



#print numbers in boxes of 3*3
#print numbers column by column




#creating a list of lists using the in1.txt sudoku puzzle
sl = [[0,0,8,0,0,0,5,0,7],\
    [0,0,5,4,0,9,0,0,0],\
    [0,0,0,6,0,0,0,4,0],\
    [0,0,0,2,0,8,0,5,0],\
    [5,2,6,0,0,0,8,7,9],\
    [0,3,0,5,0,6,0,0,0],\
    [0,8,0,0,0,1,0,0,0],\
    [0,0,0,7,0,4,3,0,0],\
    [2,0,1,0,0,0,4,0,0]]

#print(sl[0])


#code to print periphery of sudoku puzzle
flag = 1
r = 0
c = 0
while flag == 1: 
    if c <=7 and r == 0:
        c += 1
    if c == 8 and r <= 7:
        r += 1
    if r == 8 and c >= 1:
        c -= 1
    if c == 0 and r >= 1:
        r -= 1
    if r == 1 and c <= 0:
        flag = 0 
    
#    print(sl[r][c]) 
             


#code to print periphery of sudoku puzzle in reverse
f = 1
row = 0
col = 0
while f == 1:
    if row <= 7 and col == 0:
        row += 1
    if row == 8 and col <= 7:
        col += 1 
    if row >= 1 and col == 8:
        row -= 1
    if row == 0 and col >= 1:
        col -= 1
    if row == 0 and col == 0:
        f = 0

   # print(sl[row][col])


#code to print in spiral
fl = 1
ro = 0
co = 0
mn = 0
mx = 8
while fl ==1:
    if ro == mn and co <= (mx - 1):
        print(sl[ro][co])
        co += 1
    if ro <= (mx - 1) and co == mx:
        print(sl[ro][co])
        ro += 1
    if ro == mx and co >= (mn + 1):
        print(sl[ro][co])
        co -= 1
    if ro >= (mn + 2) and co == mn:
        print(sl[ro][co])
        ro -= 1
    if ro == (mn + 1) and co == mn and mn <= 4 and mx >= 4:
        mn += 1
        mx -= 1
    if ro == 4 and co == 4:
        print(sl[ro][co])
        fl = 0 
