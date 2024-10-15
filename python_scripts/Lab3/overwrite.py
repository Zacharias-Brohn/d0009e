def save(self, filename):
    try:
        with open(filename, 'r') as f:
          overwrite = input(f"'{filename}' already exists. Do you want to overwrite? [y/n]> ")
          if overwrite.lower() == 'no' and overwrite.lower() == 'n':
            print("Save operation canceled.")
            return
          elif overwrite.lower() == 'yes' and overwrite.lower() == 'y':
            raise IOError
    except IOError:
        with open(filename, 'w') as f:
            for name, number in self.book.items():
                f.write(f"{number};{name};\n")
        print(f"Phonebook saved to {filename}")