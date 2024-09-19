import sys
import os
script_dir = os.path.dirname(__file__)
mymodule_path = os.path.join(script_dir,'..')
sys.path.insert(1, mymodule_path)
import Lab2.bounce
import Lab2.derivative

def display_menu():
    print("=== Main Menu ===")
    print("1. Option 1: Bounce function")
    print("2. Option 2: Do Something Else")
    print("3. Option 3: Another Task")
    print("4. Option 4: Yet Another Task")
    print("5. Option 5: Exit")

def handle_choice(choice):
    if choice == "1":
        print("You chose Option 1:")
        n = int(input("Input a number to bounce:"))
        Lab2.bounce.bounce(n)
        break
    elif choice == "2":
        print("You chose Option 2:")
    elif choice == "3":
        print("You chose Option 3:")
    elif choice == "4":
        print("You chose Option 4:")
    elif choice == "5":
        print("Exiting...")
    else:
        print("Invalid choice. Please select a valid option.")
        main()
    return

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1-5":
            handle_choice(choice)
            break

if __name__ == "__main__":
    main()
