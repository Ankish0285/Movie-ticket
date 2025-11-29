age = int (input("enter your age:"))
ticket = input("enter 0 for true and 1 for false ")


if ticket =="0":
    ticket = True
else:
    ticket = False

if age > 18:
    print("you can watch the movie ")
    if ticket == True :
        print ("you can go inside")
    
    else:
        print("you cannot go inside withaout ticket")
elif age < 15:
        print("you can watch the movie with parents")
else:
        print("not allowed")