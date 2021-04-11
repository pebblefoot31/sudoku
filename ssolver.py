import time

puzzle = open("in1.txt", "r")
l = []
for line in puzzle:
    l.append(line)
puzzle.close()

def get_item(r,c):
    r -= 1
    c -= 1
    num = l[r].split()

    return num[c] 

row = 1
while row <= 9:
    print(get_item(row,row))
    row += 1
