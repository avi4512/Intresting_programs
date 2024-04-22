#in python Converting_overs_to_balls

#Converting Overs to Balls
#Enter the overs from user input
overs = float(input("Enter the overs:"))

num = int(overs * 10)

n1 = num % 10
if(n1 < 7):
    n2 = int(overs)

    balls = n1 + (n2 * 6)

    print("Converting overs to Balls:",balls)

else:
    print("ERROR.....Enter the Corret Over")
