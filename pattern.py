print("right angle triangle pattern \ n")


for i in range(1,6): # i = 1,2,3,4,5
    for j in range(i):
        print("*", end="")
    print('\n')




print("inverted right angle triangle pattern")

for i in range(6,1,-1):
    for j in range(i,1,-1):
        print("*", end="")
    print('\n')