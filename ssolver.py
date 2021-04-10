puzzle = open("in1.txt", "r")

def get_item(r,c):

    l = []
    for line in puzzle:
        l.append(line)

    num = l[r].split()

    return num[c] 


print(get_item(7,4))
