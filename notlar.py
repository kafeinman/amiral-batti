# prepare to exit the program
def quit():
    global exitProgram
    exitProgram=True

# set hotkey
keyboard.add_hotkey('q', lambda: quit())