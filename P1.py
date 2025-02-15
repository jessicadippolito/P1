import p1_random as p1
rng = p1.P1Random()
# import the module (do this on the first line of code)
# create a P1Random variable

game=0
hand = 0
option='1'
p_wins=0
d_wins=0
ties=0

def print_menu():
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. EXIT")


while option!='4':
    if option=='1' or option=='2':
        game+=1
        print(f'START GAME #{game}')
    hand=0
    if option == '3':
        game-=1
        print('')
        print(f'Number of Player wins: {p_wins}')
        print(f'Number of Dealer wins: {d_wins}')
        print(f'Number of tie games: {ties}')
        print(f'Total # of games played is: {game}')
        percent = (p_wins / game) * 100.0
        print(f'Percentage of Player wins: {percent:.1f}%')
        print('')
        print_menu()
        print('')
        option = (input('Choose an option: '))
    elif option!='1' and option!='2':
        print('Invalid input!')
        print('Please enter an integer value between 1 and 4!')
        print('')
        print_menu()
        print('')
        option = (input('Choose an option: '))
    while option!='3' and option!='4':
        print('')
        value = rng.next_int(13) + 1
        hand = hand + value
        if value == 11:
            print('Your card is a JACK!')
            hand-=1
        elif value == 12:
            print('Your card is a QUEEN!')
            hand-=2
        elif value == 13:
            print('Your card is a KING!')
            hand-=3
        elif value == 1:
            print('Your card is a ACE!')
        else:
            print(f'Your card is a {value}!')
        print(f'Your hand is: {hand}')
        print('')
        if hand==21:
            print('BLACKJACK! You win!')
            p_wins+=1
            print('')
            break
        if hand>21:
            print('You exceeded 21! You lose.')
            d_wins+=1
            print('')
            break
        print_menu()
        print('')
        option = (input('Choose an option: '))
        if option=='1':
            continue
        if option=='2':
            print('')
            dealer_hand = rng.next_int(11)+16
            print(f"Dealer's hand: {dealer_hand}")
            print(f'Your hand is: {hand}')
            print('')
            if dealer_hand>21:
                print('You win!')
                p_wins+=1
            elif dealer_hand==hand:
                print("It's a tie! No one wins!")
                ties+=1
            elif dealer_hand>hand:
                print('Dealer wins!')
                d_wins+=1
            else:
                print('You win!')
                p_wins += 1
            print('')
            break
        else:
            break
