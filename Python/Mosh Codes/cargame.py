a = "0"
b = "0"
print("Welcome to car game! \nType 'help' for help")
while True:
            control = input(">>")
            if control.lower() == "help":
                print("start - to start the car \nstop - to stop the car \nquit - to exit")
            elif control.lower() == "start" and a == "0":
                print("Car started...Ready to go")
                a = "1"
            elif control.lower() == "stop" and b == "0":
                print("Car stopped")
                a = "0"
                b = "1"
            elif control.lower() == "quit":
                break
            elif control.lower() == "start" and a == "1":
                print("Car already started dummy")
            elif control.lower() == "stop" and b == "1":
                print("Car already parked")
            else:
                print("I don't understand shit")

