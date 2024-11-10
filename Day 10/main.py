import art

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b


methods = {"+":add,
            "-":sub,
            "*":multiply,
             "/":divide
}
def calc():
    cont = True
    cont_new = True

    print(art.logo)

    while cont_new == True:
        first = int(input("what is your first number? \n"))
        cont_new = False
    while cont == True:
        operation = input("Pick an operation \n")

        second = int(input("what is nest number \n"))
        new_first = methods[operation](first,second)
        print(new_first)

        a = input(f"type y to continue with {new_first} or type n to go with new number ")
        if a =="y":
            cont_new = False
            first = new_first
        else:
            cont_new = True
            calc()

calc()