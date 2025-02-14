import p1_random as p1
rng = p1.P1Random()
# import the module (do this on the first line of code)
# create a P1Random variable

game=1
hand = 0
value = rng.next_int(13)+1

def print_menu():
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print Statistics")
    print("4. EXIT")

def another_card():
    if value == 11:
        print('Your card is a JACK!')
    elif value == 12:
        print('Your card is a QUEEN!')
    elif value == 13:
        print('Your card is a KING!')
    elif value == 1:
        print('Your card is a ACE!')
    else:
        print(f'Your card is a {value}!')

print(f'START GAME #{game}')
print('')
hand= hand+value
another_card()
print(f'Your hand is: {hand}')
print('')
print_menu()
print('')
option = (input('Choose an option: '))

while option!=4:
    if option==1:
        value = rng.next_int(13) + 1
        another_card()
        hand+=value
        continue
    elif option==2:
        dealer_hand = rng.next_int(11)+16
        print(f"Dealer's hand: {dealer_hand}")
        print(f'Your hand is: {hand}')
        print('')
        if dealer_hand>21:
            print('You win!')
        elif dealer_hand==hand:
            print("It's a tie! No one wins!")
        elif dealer_hand>hand:
            print('Dealer wins!')
        else:
            print('You win!')
    elif option==3:
        print("3")
    elif option==4:
        break
    game+=1

