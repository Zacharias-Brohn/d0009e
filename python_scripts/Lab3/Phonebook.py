class PhoneBook:        # Klass för telefonbok
    def __init__(self):
        self.book = {}  # Definiera "book"

    def add(self, name, number):
        # Se till att namn -och- nummer inte finns
        if name in self.book:
            print(f"{name} already exists")
        elif number in self.book.values():
            print(f"{number} already exists")
            # Annars skriv...
        else:
            self.book[name] = number

    def lookup(self, name):
        # Se till att namn finns, sedan skriv numret med namn som nyckel
        if name in self.book:
            print(self.book[name])

        else:
            print(f"{name} not found")

    def alias(self, name, newname):
        # Se till att namn finns och att Alias namn inte finns, sedan skriv alias
        if name in self.book and newname not in self.book:
            self.book[newname] = self.book[name]

        else:
            print("name not found or duplicate name")

    def change(self, name, new_number):
        # Kolla om namn finns och att nya numret inte finns
        if name in self.book and new_number not in self.book.values():
            old_number = self.book[name]
            for key in self.book:
                # Ändra numret hos alla namn som har samma nummer (Alias)
                if self.book[key] == old_number:
                    self.book[key] = new_number
        # Om numret redan finns, skriv felmeddelande
        elif new_number in self.book.values():
            print(f"{new_number} is a duplicate number")

        else:
            print(f"{name} not found")

    def save(self, filename):
        # try-except om det inte skulle gå att skriva till filnamnet
        try:
            # with open() så f.close blir onödig
            with open(filename, 'w') as f:
                # Mata in name,number och skriv till {filename}
                for name, number in self.book.items():
                    # Formattering i filen som sparas
                    f.write(f"{number};{name};\n")  
            print(f"Phonebook saved to {filename}")

        except IOError:
            print(f"Error saving to {filename}")

    def load(self, filename):
        # try-except om filnamnet som laddas inte finns
        try:
            # with open() så f.close blir onödig
            with open(filename, 'r') as f:
                # Töm nuvarande bok
                self.book.clear() 
                for line in f:
                    # Ladda namnen till minnet, ignorera 3:e "valutan"
                    number, name, _ = line.strip().split(';')
                    self.book[name] = number
            print(f"Phonebook loaded from {filename}")
        
        except IOError:
            print(f"'{filename}' doesn't exist.")

    def remove(self, name):
        # Kolla om namn finns
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
    # Initiera klassen PhoneBook
    phonebook = PhoneBook()

    while True:
        # Strip ledande och följande whitespace, splittra till kommando per ord
        command = input("telebok> ").strip().split() 
        # Reset om input utan kommandon
        if len(command) == 0:
            continue
        # Lowercase konvertering för enklare hantering
        action = command[0].lower()
        # Hantering av val - len(command) för att kasta vid fel kommando args
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
            quit()
        else:
            print("Unknown command or invalid arguments")


# Starta programmet
while True:
    main()
