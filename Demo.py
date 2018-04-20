
# login(input("Enter the User ID"),input("Enter the password"))

class xyz:

        def login(_self_,limit):
            for x in range(0, limit):
                username = input("Enter the username")
                password = int(input("enter the password"))
                if x <= 2:
                    if username == "prem" and password == 123:
                        print("Login fine")
                        break
                    else:
                        print(" Login failed")
                else:
                    print("Account locked. Contact admin")
# from Demo import xyz
# a = xyz()
# a.login(5)

