import random

def choice(Symbols):
    return[random.choice(Symbols) for symbol in range(3)] #return a list

#for orinting rows in well format we use another function
def print_row(row):
    print("Spinning.....")
    print("|".join(row))  #EXAMPLE - 😂 | 🤣| 😒

def payout_profit(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="😂":
           return bet*3
        elif row[0]=="😊" :
          return  bet*2
        elif row[0]=="🤣":
           return bet*2.5
        elif row[0]=="😒":
          return  bet*6
        else: bet*7
     #if  no matching no profit
    return 0

def main():
    balance = int(input("Enter amount :"))
    is_running = True

    while is_running:
        print(f"Your Current Balance:{balance}")
        bet = input("Enter bet amount:")
        #bet should only be digit
        if not bet.isdigit():
            print("Invalid !Enter a valid number")
            continue
        # bet should not be greater than balance
        #first convert it to int
        bet = int(bet)
        if bet>balance:
            print("Insufficent Balance")
            continue
        #bet can not be less than or = 0
        if bet<=0:
            print("bet can not be less than or equal to zero")
            continue

        balance -= bet
        Symbols = ["😂", "😊", "🤣", "😒", "😁"]
        print(f"Emojis:{Symbols}")
            #generating random emoji
        row = choice(Symbols)
        #printing in proper format random emoji
        print("**********")
        print_row(row)
        #how much profit earn
        payout = payout_profit(row,bet)
        if payout>0:
            print("You Won!")
            print(f"Your Payout is :${payout}")
            balance += payout
        elif payout<=0:
            print("you LOSE!")
        if not  input("want to play again?(Y/N):").upper()=="Y":
            is_running = False

    print(f"Your Total Balance:${balance}")
    print("Thanks for playing !")

  



if __name__ == main():
    main()
