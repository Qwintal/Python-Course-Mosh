# ">" arrow where user inputs, start-start they car, stop-stop the car, quit - quit game and help to display commands.
# if user put anything instead of these 3 tell "I don't understand"
Command = ""
Started = False
while True:
    Command = input(">").lower()
    if Command == "start":
        if Started:
            print("Car is already started!")
        else:
            Started = True
            print("Car started...")
    elif Command == "stop":
        if not Started:
            print("Car is already stopped!")
        else:
            Started = False
            print("Car stopped...")
    elif Command == "help":
        print('''
 start - to start car
 stop - to stop car
 quit - to quit    
        ''')
    elif Command == "quit":
        break

    else:
        print("I Don't understand.")

# Don't capitalize first words, it just creates confusion.
