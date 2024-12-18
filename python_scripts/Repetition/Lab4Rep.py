import os

class PhoneBook:
    def __init__(self):
        self.script_dir = os.path.dirname(__file__)
        self.book = {}
        self.reverse_book = {}
    
    def addEntry(self, name, number):
        if name in self.book:
            print(f"{name} already exists")
        elif number in self.book.values():
            print(f"{number} already exists")
        else:
            self.book[name] = number
            if number not in self.reverse_book:
                self.reverse_book[number] = [name]
            else:
                self.reverse_book[number].append(name)
    
    def lookupEntry(self, name):
        if name in self.book:
            print(f"{name}'s number: {self.book[name]}")
        else:
            print(f"Could not find {name} in phonebook.")
    
    def aliasEntry(self, name, newname):
        if name in self.book and newname not in self.book:
            self.book[newname] = self.book[name]
            self.reverse_book[self.book[name]].append(newname)
        else:
            print(f"{name} could not be found in phonebook,")
    
    def changeEntry(self, name, number):
        if name in self.book:
            current_number = self.book.get(name)
            for i in self.book:
                if current_number == self.book.get(i):
                    self.book[i] = number
            self.reverse_book[number] = self.reverse_book.pop(current_number)
        else:
            print(f"Could not find {name} in phonebook.")

    def deleteEntry(self, name):
        if name in self.book:
            self.reverse_book.pop(self.book[name])
            self.book.pop(name)
    
    def saveBook(self, filename):
        self.filepath = os.path.join(self.script_dir, filename)
        try:
            f = open(self.filepath, "x")
            for number, names in self.reverse_book.items():
                f.write(f"{number};{';'.join(names)}\n")
        except:
            overwrite = input("File exists. Overwrite? (Y/N): ")
            overwrite.strip(" .eEsS")
            if overwrite.upper() == "Y":
                with open(self.filepath, "w") as f:
                    for number, names in self.reverse_book.items():
                        f.write(f"{number};{';'.join(names)}\n")
            else:
                print("Saving cancelled.")
    
    def loadBook(self, filename):
        self.filepath = os.path.join(self.script_dir, filename)
        try:
            with open(self.filepath, "r") as f:
                for line in f:
                    parts = line.strip().split(';')
                    number = parts[0]
                    names = parts[1:]
                    for name in names:
                        self.book[name] = number
                    self.reverse_book[number] = names
        except:
            print(f"Phonebook {filename} not found.")
    
    def listEntries(self):
        print("List of all numbers in phonebook:")
        for number, names in self.reverse_book.items():
            names_str = ', '.join(names)
            print(f"{names_str} has number {number}")
    
    def quitBook(self):
        exit()

def main():
    phonebook = PhoneBook()
    while True:
        command = input("phoneBook> ").strip().split()
        choice = command[0].lower()
        if choice == "add" and len(command) == 3:
            name = command[1]
            number = command[2]
            phonebook.addEntry(name,number)
        elif choice == "lookup" and len(command) == 2:
            name = command[1]
            phonebook.lookupEntry(name)
        elif choice == "alias" and len(command) == 3:
            name = command[1]
            newname = command[2]
            phonebook.aliasEntry(name, newname)
        elif choice == "change" and len(command) == 3:
            name = command[1]
            number = command[2]
            phonebook.changeEntry(name, number)
        elif choice == "save" and len(command) == 2:
            filename = command[1]
            phonebook.saveBook(filename)
        elif choice == "load" and len(command) == 2:
            filename = command[1]
            phonebook.loadBook(filename)
        elif choice == "delete" and len(command) == 2:
            name = command[1]
            phonebook.deleteEntry(name)
        elif choice == "list" and len(command) == 1:
            phonebook.listEntries()
        elif choice == "quit" and len(command) == 1:
            phonebook.quitBook()
        else:
            print("Invalid command, try again.")

main()