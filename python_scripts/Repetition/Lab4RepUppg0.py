# Uppg. 0, Bulletin Board
class Board:
    def __init__(self, msg):
        self.msg = [msg]
    
    def post_msg(self, new_msg):
        if "No messages" in self.msg:
            self.msg = [new_msg]
        else:
            self.msg.append(new_msg)
    
    def display_msg(self):
        return "\n".join(self.msg)

def main():
    msg = "No messages"
    Kim = Board(msg)
    Chris = Board(msg)
    current_board = None

    while True:
        print("=== Bulletin Board System ===")
        if current_board == Kim:
            print("Kim's Bulletin Board Messages:")
            print(Kim.display_msg())
        elif current_board == Chris:
            print("Chris's Bulletin Board Messages:")
            print(Chris.display_msg())
        print("1: Write a message to the board")
        print("2: Tell the other to post a message")
        print("3: Choose board")
        print("0: Exit")
        choice = input("Enter choice: ")
        choice = choice.strip(" .:,")
        if choice == "1":
            if current_board == None:
                boardchoice = input("Choose board to post to (Kim or Chris): ")
                if boardchoice == "Kim":
                    current_board = Kim
                elif boardchoice == "Chris":
                    current_board = Chris
            msg = input("Enter your message: ")
            current_board.post_msg(msg) #pyright: ignore
            print("Message posted on the board: ", msg, "\n")
        elif choice == "2":
            print("Chris, please post a message on the board.")
            msg = input("Enter your message: ")
            Chris.post_msg(msg)
            print("Message posted on the board: ", msg)
        elif choice == "3":
            board = input("Choose board (Kim or Chris): ")
            board = board.strip(" .:,")
            if board == "Kim":
                current_board = Kim
                print("Current board: Kim")
            elif board == "Chris":
                current_board = Chris
                print("Current board: Chris")
            else:
                print("Invalid board")
        elif choice == "0":
            print("Goodbye!")
            exit()

main()