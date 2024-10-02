def runMain():
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

def runMainLists():
  wordList = []
  descriptionList = []
  while True:
    print_menu()
    try:
      choice = int(input("Input menu choice: "))
      if choice in range(1,4):
        handle_choiceLists(choice, wordList, descriptionList)
      else:
        raise ValueError
    except ValueError:
      print("Invalid input, try again.")

def print_menu(): # GUI meny
  print("=== Main Menu ===")
  print("1: Insert word")
  print("2: Lookup word")
  print("3: Exit")

def handle_choiceLists(choice, wordList, descriptionList):
  if choice == 1:
    word = str(input("Write the word you want to add: "))
    desc = str(input("\nWrite the description of the word: "))
    insertWordLists(word, desc, wordList, descriptionList)
    return
  elif choice == 2:
    word = str(input("Write the word you want to lookup: "))
    lookupWordLists(word, wordList, descriptionList)
  elif choice == 3:
    print("Exiting...")
    exit()

def insertWordLists(word, description, wordList, descriptionList):
  wordList.append(word)
  descriptionList.append(description)
  print(f"Added '{word}' with description '{description}' to the dictionary.")
  return

def lookupWordLists(word, wordList, descriptionList):
  if word in wordList:
    index = wordList.index(word)
    print(f"Description of '{word}': {descriptionList[index]}")
  else:
    print(f"'{word}' was not found in dictionary.")
  return

def runMainTupel():
  tupel = ()
  while True:
    print_menu()
    try:
      choice = int(input("Input menu choice: "))
      if choice in range(1,4):
        tupel = handle_choiceTupel(choice, tupel)
      else:
        raise ValueError
    except ValueError:
      print("Invalid input, try again.")

def handle_choiceTupel(choice, tupel):
  if choice == 1:
    word = str(input("Write the word you want to add: "))
    desc = str(input("Write the description of the word: "))
    tupel = insertWordTupel(tupel, word, desc)
  elif choice == 2:
    word = str(input("Write word you want to lookup: "))
    lookupWordTupel(tupel, word)
  elif choice == 3:
    print("Exiting...") 
    exit()
  return tupel

def insertWordTupel(tupel, word, desc):
  print(f"Added '{word}' with description '{desc}' to the dictionary.")
  return tupel + (word,desc)

def lookupWordTupel(tupel, word):
  if word in tupel:
    index = tupel.index(word)
    print(f"Description of '{word}': {tupel[(index+1)]}")
  else:
    print(f"'{word}' was not found in dictionary.")
  return

def runMainDictionary():
  dictionary = {}
  while True:
    print(dictionary)
    print_menu()
    try:
      choice = int(input("Input menu choice: "))
      if choice in range(1,4):
        handle_choiceDictionary(choice, dictionary)
      else:
        raise ValueError
    except ValueError:
      print("Invalid input, try again.")

def handle_choiceDictionary(choice, dictionary):
  if choice == 1:
    word = input("Write the word you want to add: ")
    desc = input("Write the description of the word: ")
    insertWordDictionary(dictionary, word, desc)  # Insert word into the dictionary
  elif choice == 2:
    word = input("Write the word you want to lookup: ")
    lookupWordDictionary(dictionary, word)  # Lookup the word in the dictionary
  elif choice == 3:
    print("Exiting...")
    exit()

def insertWordDictionary(dictionary, word, desc):
  dictionary[word] = desc
  print(f"Added '{word}' with description '{desc}' to the dictionary.")

def lookupWordDictionary(dictionary, word):
  if word in dictionary:
    print(f"Description of '{word}': {dictionary[word]}.")
  else:
    print(f"'{word}' was not found in the dictionary.")

runMain()