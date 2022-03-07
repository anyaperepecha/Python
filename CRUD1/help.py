def help_info():
    with open("help.txt", 'r') as rf:
        reader = rf.read()
        print(reader.lstrip())
