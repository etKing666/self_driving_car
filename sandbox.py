from abc import ABC, abstractmethod
from time import sleep
from sys import exit


def main_menu():
    print(30 * "=", "SMART CAR INFORMATION SYSTEM (SCIS)", 30 * "=")
    print("""
    1. Get information about the car
    2. Interact with the car
    3. Exit
    """)
    print(97 * "=")

    choice = int(input("Please make your choice [1-3]"))
    while True:
        if choice == 1:
            inf_menu()
        elif choice == 2:
            interact_menu()
        elif choice == 3:
            print("Thank you for using SCIS!")
            sleep(2)
            exit()
        else:
            print("You have entered an invalid choice. Please try again.")
            sleep(2)
            main_menu()

def inf_menu():
    print("I am the information menu")
    exit()
    pass

def interact_menu():
    print("I am the interaction menu")
    exit()
    pass

main_menu()