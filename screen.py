def clear():
    print("\033[2J")

def locate(line, column):
    print("\033[{};{}H".format(line, column), end="")

def clearLine():
    print("\033[K", end="")
