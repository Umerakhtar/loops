#log in system with nested loops
print("please set your username and password\n")
u = input("Set your username: ")
p = input("Set your password: ")
print("\nNow, please log in.\n")
for attempt in range(5):
    u1 = input("Enter username: ")
    p1 = input("Enter password: ")
    if u1 == u:
        if p1 == p: 
            print("Login successful")
            break
        else:
            print("wrong password " , attempt + 1 , " attempt")
    else:
        print("wrong username " , attempt + 1 , " attempt\n")
else:
     print("you have used wrong credentials 5 times")

print("program is ended")
