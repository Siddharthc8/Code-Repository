import os
import keyboard

def front_slash(string):
    str(string)
    for i in range(0, len(string)):
        if string[i] == '\\':
            string = string[0:i] + '/' + string[i + 1:]
    return string


def back_slash(string):
    str(string)
    for i in range(0, len(string)):
        if string[i] == '/':
            string = string[0:i] + '\\' + string[i + 1:]
    return string


def get_valid_dir():
    while True:
        try:
            directory = input("Enter the directory: ")
            if not directory.strip():
                print("Directory cannot be empty. Please try again.")
                continue
            directory = front_slash(directory)
            os.chdir(directory)
            print(f"Current directory = {os.getcwd()}\n")
            break  # Exits loop on success

        except FileNotFoundError:
            print("Directory does not exist. \nTry again")

        except PermissionError:
            print("Permission denied. You don't have access to this directory.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}. \nTry again")


def get_valid_files():
    while True:
        try:
            file_name = input("Enter the name of the file without extension: ")
            if file_name.upper() in ["EXIT", "N", "NO"]:
                print("Session Terminated")
                break

            if not file_name.strip():
                print("File name cannot be empty. \nPlease try again.")
                continue
            elif not file_name[0].isalpha():
                print("File name must start with an alphabet. \nTry again")
                continue
            file_name = file_name + ".sv"
            files_in_dir = os.listdir()
            files = [item for item in files_in_dir if os.path.isfile(os.path.join(os.getcwd(), item))] # To filter only the files
            names = [f.split()[0] for f in files]
            file, ext = file_name.split(".")

            if file_name in files:
                print(f"File {file_name} already exists")
                continue

            with open(file_name, "w") as f:
                # file, extension = os.path.splitext(file_name)
                f.write("`timescale 1ns / 1ps\n\n\n\n\n")
                f.write(f"module {file}();\n\n\nendmodule")

        except FileExistsError:
            print(f"{file_name} already exists. Try a different name")
            continue
        except ValueError:
            print("File name must contain an extension. \nTry again")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}. \nTry again")
            continue

        # while True:
        #     response = input("Do you want to create another file? Y/N : ")
        #     response = response.upper()
        #     exit_command = False
        #     if response in ["Y" or "YES"]:
        #         print("Next file execution")
        #         break
        #     elif response in ["N" or "No"]:
        #         print("Session Terminated")
        #         exit_command = True
        #         break
        #     else:
        #         print("ENTER A VALID RESPONSE. MAKE SURE YOU DID NOT ENTER THE FILE NAME")
        # if exit_command:
        #     break

