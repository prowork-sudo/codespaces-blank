import art
import menu
contains = {'water': 2000, 'milk': 1500, 'coffee': 240}

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}


def check_available(drink):
    global contains
    a = menu.MENU[drink]["ingredients"]
    for key in a:
        contains[key] = contains[key]- a[key]
    print(contains)
    for key in contains:
        if contains[key] < 0:
            print("Sorry not able to process this")
            exit()

    print(f"Insert {menu.MENU[drink]["cost"]}")
    if coin_inserted() > menu.MENU[drink]["cost"]:
        print("hire is your drink sir")
    else:print("more cash buddy")

def coin_inserted():
    print("Insert coin")
    penny_multple = int(input("How many penny"))
    dime_multple = int(input("How many dime"))
    nickle_multple = int(input("How many nickle"))
    quater_multple = int(input("How many quater"))
    return (COIN_VALUES["penny"] * penny_multple) + (COIN_VALUES["dime"] * dime_multple) + (COIN_VALUES["nickel"] * nickle_multple) + (COIN_VALUES["quarter"] * quater_multple)




            

print(art.logo)
print("Available drinks: ")
for key in menu.MENU:
    print(key)
choice = input("Pick a drink: \n")

if choice == "espresso":
    check_available(choice)
elif choice == "latte":
    check_available(choice)
elif choice == "cappuccino":
    check_available(choice)
elif choice == "off":
    print("OFF")
elif choice == "report":
    for key in contains:
        print(f"{key} : {contains[key]}")
