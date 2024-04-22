#In python Covert_balls_to_overs
# coverting the ball's to the overs in cricket

#Enter the no.of Balls from user input
x = int(input("Enter the Balls:"))
y = 6

a = x // y
b = x % y

print("{} overs".format(a))
print("{} Ball".format(b))


result = str(a) + "."+ str(b)
print("Converting Balls to Overs:",result)
