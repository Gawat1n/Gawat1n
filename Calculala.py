
def main():
    nmbrs()
    chsop()
    wish()

def nmbrs():
    global a
    global b
    a = None
    b = None

    try:
        a = float(input("Type a first number:"))
    except ValueError:
        while type(a) != float:
            try:
                a = float(input("Write only numbers:"))
            except ValueError:
                continue

    try:
        b = float(input("Type a second one:"))
    except ValueError:
        while type(b) != float:
            try:
                b = float(input("Write only numbers:"))
            except ValueError:
                continue

def chsop():
    op = input("Choose the one off operation(+;-;*;/):")
    if op == "+":
        calcop("+")
    elif op == "-":
        calcop("-")
    elif op == "*":
        calcop("*")
    elif op == "/":
        calcop("/")
    else:
        while op != "+" or "-" or "*" or "/":
            op = input("Choose the correct one(+;-;*;/):")
            if op == "+":
                calcop("+")
                break
            elif op == "-":
                calcop("-")
                break
            elif op == "*":
                calcop("*")
                break
            elif op == "/":
                calcop("/")
                break
            else:
                continue

def calcop(op):
    match op:
        case "+":
            c = a + b
            print(f"{a}+{b}={c}")
        case "-":
            c = a - b
            print(f"{a}-{b}={c}")
        case "*":
            c = a * b
            print(f"{a}*{b}={c}")
        case "/":
            c = a / b
            print(f"{a}/{b}={c}")

def wish():
    wish = str.upper(input("Would you like to continue?(Y/N):"))
    if wish == "Y":
        main()
    elif wish == "N":
        exit()
    else:
        while wish != "Y" or "N":
            wish = str.upper(input("Type correctly(Y/N):"))
            if wish == "Y":
                main()
            elif wish == "N":
                exit()

main()
