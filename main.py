# this code creates an imitation of a chat in the console.
# this code is written in python 3.11.
# this code does not make sense and was created as a demonstration.
# this code does not support databases and it has no network functions.
# creation date 15/11/2022 by Krayfor.

import os
import time
import ctypes


chat_password = "12345"
colorList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
damnWordsList = ["fuck", "bitch", "blyat", "нахуй", "сука", "syka"]



def sendMessageInChat(message, user_name):
    unix_time = time.time()
    message_time = time.ctime(unix_time)
    print(f"({message_time}) {user_name}: {message}")


def changeConsoleColor(colorId):
    os.system(f"color {colorId}")


def authorization():
    os.system("cls")
    print(f"Hello {user_login}!\nDo you want to enter the chat? y/n")
    user_choice = input("choice: ")

    if user_choice == "y":
        os.system("cls")
        print("Welcome to the chat!")

        # chat logic
        while True:
            # time.sleep(0.5)
            user_input_message = input("Say: ")
            if user_input_message == "/q" or user_input_message == "/quit":
                break
            elif "/c" in user_input_message:
                for i in user_input_message:
                    if i in colorList:
                        changeConsoleColor(i)
                        user_input_message = None
                        continue
            if user_input_message is not None and user_input_message != " " and user_input_message != "":
                sendMessageInChat(user_input_message, user_login)
                if user_input_message in damnWordsList:
                    system = "System"
                    system_message = f"{user_login} don't swear!"
                    print(f"{system}: {system_message}")
                    del system
                    del system_message
        print("Good bye!")
    else:
        print("Good bye!")



os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleA(b"Python chat")
user_login = input("What is your name?: ")

if len(user_login) > 20 or len(user_login) < 3:
    print("Username invalid!")
else:
    user_input_password = input("Enter the chat password: ")
    if user_input_password == chat_password:
        authorization()
    else:
        print("Password invalid!")