import sys

def runMain(): # Vilken typ av Ordlista att kalla
  print("=== Choose type ===")
  print("1: Listor")
  print("2: Tupel")
  print("3: Dictionary")
  try:
    val = int(input("Val: "))
    if val == 1:
      runMainLists()
    elif val == 2:
      runMainTupel()
    elif val == 3:
      runMainDictionary()
    elif val not in range(1,4):
      raise ValueError
  except ValueError:
    print("Invalid input")
    runMain()

def print_menu(): # GUI meny
  print("\n=== Main Menu ===")
  print("1: Insert word")
  print("2: Lookup word")
  print("3: Delete word")
  print("4: Exit")

def runMainLists():     # Ordlista med listor
  wordList = []         # Beskriva listorna
  descriptionList = []
  while True:           # Kör programmet oändligt så listor inte återställs
    print_menu()
    try:
      choice = int(input("Input menu choice: "))
      if choice in range(1,5):
        handle_choiceLists(choice, wordList, descriptionList)
      else:
        raise ValueError  # För att fånga input utanför 1-3 med nedan
    except ValueError:    # För att fånga input som inte är integer
      print("Invalid input, try again.")

def handle_choiceLists(choice, wordList, descriptionList):
  if choice == 1:
    word = str(input("Write the word you want to add: "))
    desc = str(input("\nWrite the description of the word: "))
    insertWordLists(word, desc, wordList, descriptionList)
  elif choice == 2:
    word = str(input("Write the word you want to lookup: "))
    lookupWordLists(word, wordList, descriptionList)
  elif choice == 3:
    word = str(input("Write the word you want to remove: "))
    removeWordLists(word, wordList, descriptionList)
  elif choice == 4:
    print("Exiting...")
    exit()
  return

def insertWordLists(word, description, wordList, descriptionList):
  if word in wordList:
    print(f"'{word}' is already defined, you can only insert new words.")
  else:
    wordList.append(word)               # Lägg till i Ordlista
    descriptionList.append(description) # Lägg till i definitions lista
    print(f"Added '{word}' with description '{description}' to the dictionary.")
  return

def lookupWordLists(word, wordList, descriptionList):
  try:                            # Kollar om ordet finns
    index = wordList.index(word)  # Samma index på ordet som definition
    print(f"Description of '{word}': {descriptionList[index]}")
  except ValueError:              # Fångar om ordet inte finns i Ordlistan
    print(f"'{word}' was not found in dictionary.")
    return

def removeWordLists(word, wordList, descriptionList):
  try:
    index = wordList.index(word)  # Index av samma anledning som lookup
    print(f"Removed '{word}' with description {descriptionList[index]}")
    wordList.pop(index)           # Pop tar bort ordet
    descriptionList.pop(index)    # Och definitionen 
  except ValueError:              # Fångar om order inte finns i Ordlistan
    print(f"'{word}' was not found in dictionary.")
    return
  
def runMainTupel(): # Samma upplägg men med tupel
  tupel = []        # Tilldela tupel till variabel
  while True:
    print_menu()
    try:
      choice = int(input("Input menu choice: "))
      if choice in range(1,5):
        handle_choiceTupel(choice, tupel) # Måste tilldela till tupel
      else:
        raise ValueError
    except ValueError:
      print("Invalid input, try again.")

def handle_choiceTupel(choice, tupel):  # Hantera val
  if choice == 1:
    word = str(input("Write the word you want to add: "))
    desc = str(input("Write the description of the word: "))
    insertWordTupel(tupel, word, desc)
  elif choice == 2:
    word = str(input("Write word you want to lookup: "))
    lookupWordTupel(tupel, word)
  elif choice == 3:
    word = str(input("Write word you want to remove: "))
    tupel = removeWordTupel(tupel, word)
  elif choice == 4:
    print("Exiting...") 
    exit()
  return tupel

def insertWordTupel(tupel, word, desc):
  if word in tupel:
    print(f"'{word}' is already defined, you can only insert new words.")
    return
  else:
    print(f"Added '{word}' with description '{desc}' to the dictionary.")
  return tupel.append((word,desc)) # Returnera ord och definition

def lookupWordTupel(tupel, word):
  for i in tupel:
    if word in i:   # Index av ordet
      print(f"Description of '{word}': {i[1]}") # Skriver index+1 för att ta fram definition
      return
  print(f"'{word}' was not found in dictionary.")
  return

def removeWordTupel(tupel, word):
  if word in tupel:
    index = tupel.index(word)
    if index % 2: # Index på definitioner i tupeln är alltid udda
      print(f"'{word}' was not found in dictionary.")
    else:
      tupel = tupel[:index] + tupel[index+2:] # Slice/sk��r tupeln
  else:
    print(f"'{word}' was not found in dictionary.")
  return tupel

def runMainDictionary():
    """Main function to run the dictionary program."""
    dictionary = {}  # Initialize dictionary
    while True:
        print_menu()
        print(dictionary)
        try:
            choice = int(input("Input menu choice: "))
            if choice in range(1, 5):
                handle_choiceDictionary(choice, dictionary)
            else:
                raise ValueError
        except ValueError:
            print("Invalid input, try again.\n")

def handle_choiceDictionary(choice, dictionary):
    """Handle menu choices for the dictionary."""
    if choice == 1:
        word = input("Write the word you want to add: ")
        desc = input("Write the description of the word: ")
        insertWordDictionary(dictionary, word, desc)
    elif choice == 2:
        word = input("Write the word you want to lookup: ")
        lookupWordDictionary(dictionary, word)
    elif choice == 3:
        word = input("Write the word you want to remove: ")
        removeWordDictionary(dictionary, word)
    elif choice == 4:
        print("Exiting...\n")
        sys.exit()

def insertWordDictionary(dictionary, word, desc):
    """Insert a word and its description into the dictionary."""
    if word in dictionary:
        print(f"'{word}' is already defined, you can only insert new words.")
    else:
        dictionary[word] = desc  # Add word and definition to dictionary
        print(f"Added '{word}' with description '{desc}' to the dictionary.\n")

def lookupWordDictionary(dictionary, word):
    """Lookup a word in the dictionary."""
    if word in dictionary:  # Check if the word exists
        print(f"Description of '{word}': {dictionary[word]}.")
    else:
        print(f"'{word}' was not found in the dictionary.\n")

def removeWordDictionary(dictionary, word):
    """Remove a word from the dictionary."""
    if word in dictionary:
        del dictionary[word]
        print(f"Removed '{word}' from the dictionary.\n")
    else:
        print(f"'{word}' was not found in the dictionary.\n")

runMain()
