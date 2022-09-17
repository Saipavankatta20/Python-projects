"""
[" ", " ", " "] - r0
[" ", " ", " "] - r1
[" ", " ", " "] - r2

"""

# Check for win
def checkforwin():
    # Row
    if(r0 == ["O", "O", "O"] or r1 == ["O", "O", "O"] or r2 == ["O", "O", "O"]):
        print("O win")
        return True
    if(r0 == ["X", "X", "X"] or r1 == ["X", "X", "X"] or r2 == ["X", "X", "X"]):
        print("X win")
        return True
    
    # Column
    for i in range(3):
        if(r0[i] == r1[i] == r2[i] == "O"):
            print("O wins")
            return True
        if(r0[i] == r1[i] == r2[i] == "X"):
            print("X wins")
            return True
            
    # Diagonal
    if(r0[0] == r1[1] == r2[2] == "O" or r0[2] == r1[1] == r2[0] == "O"):
        print("O wins")
        return True
    if(r0[0] == r1[1] == r2[2] == "X" or r0[2] == r1[1] == r2[0] == "X"):
        print("X wins")
        return True

    if(" " not in r0 and " " not in r1 and " " not in r2):
        print("DRAW")
        return True
        
    return False

# Input
def take_input(k):
    r, c = map(int, input("Enter row and column numbers:").split())
    if(r in [0, 1, 2] and c in [0, 1, 2]):

        if(r == 0):
            if(r0[c] == " "):
                r0[c] = k
            else:
                print("INVALID")
                take_input(k)
        elif(r == 1):
            if(r1[c] == " "):
                r1[c] = k
            else:
                print("INVALID")
                take_input(k)

        else:
            if(r2[c] == " "):
                r2[c] = k
            else:
                print("INVALID")
                take_input(k)
    #checkforwin()
    else:
        print("INVALID RANGE")
        take_input(k)


r0 = [" ", " ", " "]
r1 = [" ", " ", " "]
r2 = [" ", " ", " "]
count = 0
while(checkforwin() == False):
    if(count % 2 == 0):
        take_input("X")
    else:
        take_input("O")
    print(r0)
    print(r1)
    print(r2)
    count = count + 1     