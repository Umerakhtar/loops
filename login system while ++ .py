u = input("please set username:  ")
p = input("please set password:  ")
print (". . .  please use your username and password to login(in five attempts)  . . . ")
attempt = 0
while attempt < 5:
    u1 = input("username:  ")
    p1 = input("password:  ")
    if u1 == u:
        if p1 == p:
            print("login successful")
            break
        else:
            print("incorrect password")
    else:
        print("incorrect username")
    attempt += 1
    print("attempt" , attempt, "out of 5 used")
print("you have used wrong credentials 5 times")
print("\nprogram ended\n")