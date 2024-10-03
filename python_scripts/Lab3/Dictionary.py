def runMain(): # Vilken typ av Ordlista att kalla
  print("=== Choose type ===")
  print("1: Listor")
  print("2: Tupel")
  print("3: Dictionary")
  try:
    val = int(input("Val: \n"))
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
    #print(wordList)
    #print(descriptionList)
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
  wordList.append(word)               # Lägg till i Ordlista
  descriptionList.append(description) # Lägg till i definitions lista
  print(f"Added '{word}' with description '{description}' to the dictionary.")
  return

def lookupWordLists(word, wordList, descriptionList):
  try:            # Kollar om ordet finns
    index = wordList.index(word)  # Samma index på ordet som definition
    print(f"Description of '{word}': {descriptionList[index]}")
  except ValueError:
    print(f"'{word}' was not found in dictionary.")
    return

def removeWordLists(word, wordList, descriptionList):
  try:
    index = wordList.index(word) # Index av samma anledning som lookup
    wordList.pop(index) # Pop tar bort ordet
    descriptionList.pop(index) # Och definitionen 
    print(f"Removed '{word}' with description {descriptionList[index]}")
  except ValueError:
    print(f"'{word}' was not found in dictionary.")
    return
  
def runMainTupel(): # Samma upplägg men med tupel
  tupel = ()        # Tilldela tupel till variabel
  while True:
    print_menu()
    print(tupel)
    try:
      choice = int(input("Input menu choice: "))
      if choice in range(1,5):
        tupel = handle_choiceTupel(choice, tupel) # Måste tilldela till tupel
      else:
        raise ValueError
    except ValueError:
      print("Invalid input, try again.")

def handle_choiceTupel(choice, tupel):  # Hantera val
  if choice == 1:
    word = str(input("Write the word you want to add: "))
    desc = str(input("Write the description of the word: "))
    tupel = insertWordTupel(tupel, word, desc)  # Samma här, tilldela till tupel
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
  print(f"Added '{word}' with description '{desc}' to the dictionary.")
  return tupel + (word,desc) # Returnera ord och definition

def lookupWordTupel(tupel, word):
  try:                          # Kolla att ordet finns
    index = tupel.index(word)   # Index av ordet
    print(f"Description of '{word}': {tupel[(index+1)]}") # Skriver index+1 för att få definition
  except ValueError:
    print(f"'{word}' was not found in dictionary.")
    return

def removeWordTupel(tupel, word):
  if word in tupel:
    index = tupel.index(word)
    if index % 2:
      print(f"'{word}' was not found in dictionary.")
    else:
      tupel = tupel[:index] + tupel[index+2:]
  else:
    print(f"'{word}' was not found in dictionary.")
  return tupel
  #try:
  #  index = tupel.index(word)
  #  listCnvt = list(tupel)  # Konvertera till lista
  #  listCnvt.pop(index)     # Pop tar bort ordet
  #  listCnvt.pop(index)     # Igen för beskrivningen tar ordets plats
  #  tupel = tuple(listCnvt) # Tillbaka till tupel
  #  return tupel
  #except ValueError:        # Fångar om ordet inte finns
  #  print(f"'{word}' was not found in dictionary.")
  #  return

def runMainDictionary():
  dictionary = {} # Tilldela variabel med dictionary
  while True:
    print_menu()
    # print(dictionary)
    try:
      choice = int(input("Input menu choice: "))
      if choice in range(1,5):
        handle_choiceDictionary(choice, dictionary)
      else:
        raise ValueError
    except ValueError:
      print("Invalid input, try again.\n")

def handle_choiceDictionary(choice, dictionary):
  if choice == 1:
    word = str(input("Write the word you want to add: "))
    desc = str(input("Write the description of the word: "))
    insertWordDictionary(dictionary, word, desc)
  elif choice == 2:
    word = str(input("Write the word you want to lookup: "))
    lookupWordDictionary(dictionary, word)
  elif choice == 3:
    word = str(input("Write the word you want to remove: "))
    removeWordDictionary(dictionary, word)
  elif choice == 4:
    print("Exiting...\n")
    exit()

def insertWordDictionary(dictionary, word, desc):
  dictionary[word] = desc # Lägg till ord och definition till Ordlista
  print(f"Added '{word}' with description '{desc}' to the dictionary.\n")

def lookupWordDictionary(dictionary, word):
  if word in dictionary:  # Kolla om ordet finns
    print(f"Description of '{word}': {dictionary[word]}.")
  else:
    print(f"'{word}' was not found in the dictionary.\n")

def removeWordDictionary(dictionary, word):
  try:
    dictionary.pop(word)
  except KeyError:
    print(f"'{word}' was not found in the dictionary.\n")
    return

runMain()
