class PhoneBook:        # Klass för telefonbok
    def __init__(self):
        self.book = {}  # Definiera "book"

    def add(self, name, number):
        # Se till att namn -och- nummer inte finns
        if name in self.book:
            print(f"{name} already exists")
        elif any(num == number for num in self.book.values()):
            print(f"{number} already exists")
        else:
            self.book[name] = number

    def lookup(self, name):
        # Se till att namn finns
        if name in self.book:
            print(self.book[name])
        else:
            print(f"{name} not found")

    def alias(self, name, newname):
        # Se till att namn finns men inte Alias
        if name in self.book and newname not in self.book:
            self.book[newname] = self.book[name]
        else:
            print("name not found or duplicate name")

    def change(self, name, new_number):
        if name in self.book:
            old_number = self.book[name]
            for key in self.book:
                # Ändra numret hos alla namn som har samma nummer (Alias)
                if self.book[key] == old_number:
                    self.book[key] = new_number
        else:
            print(f"{name} not found")

    def save(self, filename):
        try:  # try-except om det inte skulle gå att skriva filen
            with open(filename, 'w') as f:
                for name, number in self.book.items():
                    f.write(f"{number};{name};\n")  # Formattering i filen som sparas
            print(f"Phonebook saved to {filename}")
        except IOError:
            print(f"Error saving to {filename}")

    def load(self, filename):
        try:
            with open(filename, 'r') as f:
                self.book.clear() # Töm nuvarande bok
                for line in f:
                    # Ladda namnen till minnet, ignorera 3:e valutan
                    number, name, _ = line.strip().split(';')
                    self.book[name] = number
            print(f"Phonebook loaded from {filename}")
        except IOError:
            print(f"'{filename}' doesn't exist.")
    
    def remove(self, name):
        if name in self.book:
            # Spara numret associerat till namnet
            number = self.book[name]
            # Använd lista för att undvika RuntimeError
            for key in list(self.book.keys()):
                if self.book[key] == number:
                    del self.book[key]
            print(f"Removed entries and aliases for {name}.")
        else:
            print(f"{name} not found in the phone book.")

def main():
    phonebook = PhoneBook()

    while True:
        command = input("telebok> ").strip().split() # Splittra kommandon
        if len(command) == 0:
            continue
        # Lowercase konvertering för enklare hantering
        action = command[0].lower()
        # Hantering av de olika kommandon
        if action == "add" and len(command) == 3:
            name, number = command[1], command[2]
            phonebook.add(name, number)
        elif action == "lookup" and len(command) == 2:
            name = command[1]
            phonebook.lookup(name)
        elif action == "alias" and len(command) == 3:
            name, newname = command[1], command[2]
            phonebook.alias(name, newname)
        elif action == "change" and len(command) == 3:
            name, number = command[1], command[2]
            phonebook.change(name, number)
        elif action == "save" and len(command) == 2:
            filename = command[1]
            phonebook.save(filename)
        elif action == "load" and len(command) == 2:
            filename = command[1]
            phonebook.load(filename)
        elif action == "remove" and len(command) == 2:
            name = command[1]
            phonebook.remove(name)
        elif action == "quit":
            break
        else:
            print("Unknown command or invalid arguments")

# Starta programmet
while True:
    main()
