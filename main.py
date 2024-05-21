import random, os
hand = []
bothand = []
table = []
cards = ['1:🔵', '1:🔵', '1:🟢', '1:🟢', '1:🟡', '1:🟡', '1:🔴', '1:🔴', 
         '2:🔵', '2:🔵', '2:🟢', '2:🟢', '2:🟡', '2:🟡', '2:🔴', '2:🔴', 
         '3:🔵', '3:🔵', '3:🟢', '3:🟢', '3:🟡', '3:🟡', '3:🔴', '3:🔴', 
         '4:🔵', '4:🔵', '4:🟢', '4:🟢', '4:🟡', '4:🟡', '4:🔴', '4:🔴', 
         '5:🔵', '5:🔵', '5:🟢', '5:🟢', '5:🟡', '5:🟡', '5:🔴', '5:🔴', 
         '6:🔵', '6:🔵', '6:🟢', '6:🟢', '6:🟡', '6:🟡', '6:🔴', '6:🔴', 
         '7:🔵', '7:🔵', '7:🟢', '7:🟢', '7:🟡', '7:🟡', '7:🔴', '7:🔴', 
         '8:🔵', '8:🔵', '8:🟢', '8:🟢', '8:🟡', '8:🟡', '8:🔴', '8:🔴', 
         '9:🔵', '9:🔵', '9:🟢', '9:🟢', '9:🟡', '9:🟡', '9:🔴', '9:🔴', 
         '0:🔵', '0:🟢', '0:🟡', '0:🔴', 
         'block:🔵', 'block:🔵', 'block:🟢', 'block:🟢', 'block:🟡', 'block:🟡', 'block:🔴', 'block:🔴', 
         'twist:🔵', 'twist:🔵', 'twist:🟢', 'twist:🟢', 'twist:🟡', 'twist:🟡', 'twist:🔴', 'twist:🔴', 
         '+2:🔵', '+2:🔵', '+2:🟢', '+2:🟢', '+2:🟡', '+2:🟡', '+2:🔴', '+2:🔴', 
         'CHANGE:🔵🟢🟡🔴', 'CHANGE:🔵🟢🟡🔴', 'CHANGE:🔵🟢🟡🔴', 'CHANGE:🔵🟢🟡🔴', 
         '+4:🔵🟢🟡🔴', '+4:🔵🟢🟡🔴', '+4:🔵🟢🟡🔴', '+4:🔵🟢🟡🔴']
def cls():
    os.system("cls")
def show_hands():
        print(f"Your hand: {hand}")
        print(f"Bot hand: {bothand}")
def change_color():
    global color
    while True:
        try:
            colorchoice = int(input("1 🔵| 2 🟢| 3 🟡| 4 🔴")) 
            break
        except ValueError:
            print("ERROR")
    match colorchoice:
        case 1:
            color = "🔵"
        case 2:
            color = "🟢"
        case 3:
            color = "🟡"
        case 4:
            color = "🔴"
def getcard(user):
    if user == "bot":
        card_index = random.choice(range(len(cards)))
        bothand.append(cards.pop(card_index))
    elif user == "user":
        card_index = random.choice(range(len(cards)))
        hand.append(cards.pop(card_index))
def get_hands():
    for i in range(0, 7):
        getcard("user")
    for i in range(0, 7):
        getcard("bot")
    show_hands()
def play():
    while True:
            choice = input("Index da carta (QUALQUER LETRA PARA COMPRAR): ")
            if choice.isalpha():
                getcard("user")
            else:
                try:
                    choice = int(choice) - 1
                
                    temp = hand[choice].split(":")
                    value = temp[0]
                    color = temp[1]
                    
                    if len(table) > 0:
                        temp = table[-1].split(":")
                        tvalue = temp[0]
                        tcolor = temp[1]
                    else:
                        tvalue = value
                        tcolor = color
                        
                    if value == "CHANGE":
                        change_color()
                        
                    if value == "+4":
                        change_color()
                        for i in range(1, 4):
                            getcard("bot")
                            
                    if value == tvalue or tcolor in color:
                        table.append(hand.pop(choice))
                        cls()
                        print(f"Table : {table}")
                        show_hands()
                except IndexError:
                    pass
def main():
    get_hands()
    play()
main()