while True:
    try:
        number = int(input("Enter an integer but 0: "))
        print(18/number)
        break

    except ValueError:
        print("Enter only a number")

    except ZeroDivisionError:
        print("Do not enter '0'")

    except:
        break

    finally:
        print("Loop complete")             # Prints at the end of the program
