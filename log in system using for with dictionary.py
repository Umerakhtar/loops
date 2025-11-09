#log in system with nested loops and storing them in dictionary
u_dict = {}
p_dict = {}
user_key = ""
pass_value = ""
print("please set your username and password\n")
u = input("Set your username: ")
p = input("Set your password: ")
print("\nNow, please log in.\n")
for attempt in range(5):
    u1 = input("Enter username: ")
    p1 = input("Enter password: ")
    u_dict[attempt] = u1
    p_dict[attempt] = p1
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

print( u_dict,"\n" ,p_dict )