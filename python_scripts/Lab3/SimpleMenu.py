import sys
import os
script_dir = os.path.dirname(__file__)
mymodule_path = os.path.join(script_dir,'..')
sys.path.insert(1, mymodule_path)
import Lab2.bounce
import Lab2.derivative

def display_menu(): # GUI meny
  print("=== Main Menu ===")
  print("1: Bounce function")
  print("2: Tvärsumma function")
  print("3: Newton-Raphson function")
  print("4: Exit")

def handle_choice(choice): # Hantera val, exekvera funktioner
  if choice == 1:
    try:
      n = int(input("Input a number to bounce: "))
      Lab2.bounce.bounce(n) # Använd funktion bounce från Lab2
    except ValueError:
      print("Invalid input, try again.\n")
      handle_choice(choice)
  elif choice == 2:
    try:
      n = int(input("Input a number to calculate: "))
      o = Lab2.bounce.tvarsumman(n) # Använd funktion tvarsumman från Lab2
      print(f"Sum of numbers is: {o}\n")
    except ValueError:
      print("Invalid input, try again.\n")
      handle_choice(choice)
  elif choice == 3:
    try:
      n = int(input("Input starting guess: "))
      root = Lab2.derivative.solve(Lab2.derivative.exempel1,n,1e-5)
      print(f"Root of x^2-1 with guess {n} is {root}\n")
    except ValueError:
      print("Invalid input, try again.\n")
      handle_choice(choice)
  elif choice == 4:
    print("Exiting...")
    exit()
  a = None # Definiera variabel a
  while a not in ("Y","N","y","n"): 
    a = str(input("Would you like to run that function again? (Y/N): "))
    if a in ("Y", "y"):
      handle_choice(choice) # Kör om samma funktion igen
    elif a in ("N", "n"):
      break # Bryt ut ur loopen
    else:
      print("Invalid input, try again.\n")
  return

def main(): # Visa meny och kalla hanterare
  display_menu() 
  try:
    choice = int(input("Enter your choice (1-4): "))
    if choice in range(1,5): # Se till att val är mellan 1 och 4
      print(f"You chose option {choice}\n")
      handle_choice(choice)
    raise ValueError
  except ValueError:
    print("Invalid input, try again.\n")
  return


while True: # Visa meny vid start och vid return
  main()
