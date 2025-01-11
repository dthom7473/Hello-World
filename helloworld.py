def menu():
    while True:
        print("\n1 - About Me\n2 - Repository Info \n3 - Exit\n")
        try:
            x = int(input("Select a Number: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if x == 1:
            print("\nHello! My name is Walter Thomas and I am an aspiring computer engineer. "
                  "I study at Brigham Young University - Idaho and I have a profound love for computers and their systems. "
                  "I love music, movies, and board games, and I particularly enjoy problem-solving tasks. "
                  "Welcome to my portfolio!")
        elif x == 2:
            print("\nThe purpose of this repository is to contain projects created by myself to share and educate other people. "
                  "It will contain several passion projects of my own as I aspire to expand my knowledge in new programming languages, "
                  "learn their uses, and develop a deeper understanding.")
        elif x == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Start the program
print("Hello World!")
menu()
