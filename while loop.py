i=0
while(i<45):
    print(i+1, end=" ")
    i=i+1

while(True):
    inp=int(input("enter a no\n"))
    if inp>100:
        print("you have entered no gtrater 100\n")
        break
    else:
        print("try again\n")
        continue


