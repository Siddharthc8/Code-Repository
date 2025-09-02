control = ""
started = False
stopped = False
while control.lower() != "quit":
            control = input(">>")
            if control.lower() == "help":
                print("start - to start the car \nstop - to stop the car \nquit - to exit")
            elif control.lower() == "start" and started == False:
                print("Car started...Ready to go")
                started = True
            elif control.lower() == "stop" and stopped == False:
                print("Car stopped")
                stopped = True
            elif control.lower() == "quit":
                break
            elif control.lower() == "start" and started == True:
                print("Car already started")
            elif control.lower() == "stop" and stopped == True:
                print("Car already parked")
            else:
                print("I don't understand shit")
