def getdate():
    import datetime
    return datetime.datetime.now()

print('''Welcome Welcome Welcome 
            to our highly rated 
   
   
   Health Management Program''')
print("Please Register or login")
def management_AI():
    i = 0
    for i in range(0, 3):
        a = int(input("Enter 0 for registeration or 1 for login : "))
        if a == 0:
            print("         Registeration Center        ")
            n = input("Enter your name : ")
            h = f"{n}.txt"
            h_1 = f"{n}_1.txt"
            # print(h)
            with open(h, 'w') as f:
                f.write(f"{n} exercise management window")
            with open(h_1, 'w') as f:
                f.write(f"{n} diet management window")
            print("Thank you, for registering")
        elif a == 1:
            print("         User Conrtrol Center        ")
            p = input("Enter your name : ")
            u = f"{p}.txt"
            u_1 = f"{p}_1.txt"
            m = input('''please enter r for reading your data or w for adding your data : ''')
            if m == "r":
                k = int(input("Enter 2 to view exercise management window or 3 to view diet management window : "))
                if k == 2:
                    with open(u) as f:
                        con = f.read()
                        print(con)
                elif k == 3:
                    with open(u_1) as f:
                        con = f.read()
                        print(con)
                else:
                    None
            elif m == "w":
                l = int(input("Enter 4 for updating exercise management window or 5 for updating diet management window : "))
                if l == 4:
                    with open(u, 'a') as f:
                        con = input("Enter what you have to write : ")
                        f.write(f"{con}\n{getdate()}\n")
                        print("Thank you, your data has been successfully saved")
                elif l == 5:
                    with open(u_1, 'a') as f:
                        con = input("Enter what you have to write : ")
                        f.write(f"{con}\n{getdate()}\n")
                        print("Thank you, your data has been successfully saved")
                else:
                    None
            else:
                None
        else:
            None
        i = i + 1

management_AI()