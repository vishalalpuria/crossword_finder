import numpy as np

R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

matrix = []  

print("Enter the entries rowwise:")
# For user input 
for i in range(R):		 # A for loop for row entries 
	a =[] 
	for j in range(C):	 # A for loop for column entries 
		a.append(input()) 
	matrix.append(a) 

print("The given input is as follows")

for i in range(R): 
	for j in range(C): 
		print(matrix[i][j], end = " ") 
	print() 


Tmatrix = np.array(matrix)

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  


def finder(word):
    for i in range(R):
        # for horizontal strings making
        tempstr = listToString(matrix[i])
        if(tempstr.find(word) != -1):
            print(f"{word} is finded in line", i+1 )

    for i in range(R):
        # for REVERSE_horizontal strings making
        tempstr = listToString(matrix[i])[::-1]
        if(tempstr.find(word) != -1):
            print(f"{word} is finded in line", i+1 )





    for i in range(C):
        # for vertical strings making
        tempstr = ""
        for k in range(C):
            tempstr += (matrix[k][i])
        if(tempstr.find(word) != -1):
            print(f"{word} is finded in Column", i+1 )

    for i in range(C):
        # for REVERSE_vertical strings making
        tempstr = ""
        for k in range(C):
            tempstr += (matrix[k][i])
        tempstr = tempstr[::-1]
        if(tempstr.find(word) != -1):
            print(f"{word} is finded in Column", i+1 )

    #---------------------FOR DIAGONALS-----------------
    diags = [Tmatrix[::-1,:].diagonal(i) for i in range((-R+1),C)]
    diags.extend(Tmatrix.diagonal(i) for i in range(R-1,-C,-1))
    z1 = 0 
    for n in diags:
        z1 += 1
        tempstr = listToString(n)
        if(tempstr.find(word) != -1):
            if z1 <= (R+C-1):
                print(f"{word} is finded in DIAGONAL {z1} (top left to bottom right)")
            else:
                print(f"{word} is finded in DIAGONAL {z1} (top right to bottom left)")

    #---------------------FOR REVERSE DIAGONALS-------------
    diags = [Tmatrix[::-1,:].diagonal(i) for i in range((-R+1),C)]
    diags.extend(Tmatrix.diagonal(i) for i in range(R-1,-C,-1))
    z2 = 0
    for n in diags:
        z2 += 1
        tempstr = listToString(n)[::-1]
        if(tempstr.find(word) != -1):
            if z2 <= (R+C-1):
                print(f"{word} is finded in REV_DIAGONAL {z2} (top left to bottom right)")
            else:
                print(f"{word} is finded in REV_DIAGONAL {z2} (top right to bottom left)" )



print("Enter the words u want to find")
n=0
tlist=[]
while n != 1:
    inp = input("ENTER WORD\n")
    tlist.append(inp)
    n = int(input("press 0 - for more input \npress 1 - for continue search\n"))

for items in tlist:
    finder(items)










