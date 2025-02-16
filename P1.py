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
in_progress=True

def print_menu():
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")


while in_progress:
    game+=1
    hand=0
    print(f'START GAME #{game}')
    if option=='4':
        break
    while in_progress:
        if option=='2':
            option='1'
            break
        if hand>=21:
            break
        if hand==0:
            print('')
            value = rng.next_int(13) + 1
            if value >= 11:
                if value == 11:
                    print('Your card is a JACK!')
                    hand += 10
                    print(f'Your hand is: {hand}')
                elif value == 12:
                    print('Your card is a QUEEN!')
                    hand += 10
                    print(f'Your hand is: {hand}')
                elif value == 13:
                    print('Your card is a KING!')
                    hand += 10
                    print(f'Your hand is: {hand}')
            elif value == 1:
                print('Your card is a ACE!')
                hand += 1
                print(f'Your hand is: {hand}')
            else:
                print(f'Your card is a {value}!')
                hand += value
                print(f'Your hand is: {hand}')
        print('')
        print_menu()
        print('')
        option = (input('Choose an option: '))
        while True:
            if option=='1':
                print('')
                value = rng.next_int(13) + 1
                if value>=11:
                    if value == 11:
                        print('Your card is a JACK!')
                        hand +=10
                        print(f'Your hand is: {hand}')
                    elif value == 12:
                        print('Your card is a QUEEN!')
                        hand +=10
                        print(f'Your hand is: {hand}')
                    elif value == 13:
                        print('Your card is a KING!')
                        hand +=10
                        print(f'Your hand is: {hand}')
                elif value==1:
                    print('Your card is a ACE!')
                    hand+=1
                    print(f'Your hand is: {hand}')
                else:
                    print(f'Your card is a {value}!')
                    hand+=value
                    print(f'Your hand is: {hand}')
                if hand == 21:
                    print('')
                    print('BLACKJACK! You win!')
                    p_wins += 1
                    print('')
                    break
                elif hand > 21:
                    print('')
                    print('You exceeded 21! You lose.')
                    d_wins += 1
                    print('')
                    break
                break
            elif option=='2':
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
            elif option == '3':
                game-=1
                print('')
                print(f'Number of Player wins: {p_wins}')
                print(f'Number of Dealer wins: {d_wins}')
                print(f'Number of tie games: {ties}')
                print(f'Total # of games played is: {game}')
                percent = (p_wins / game) * 100.0
                print(f'Percentage of Player wins: {percent:.1f}%')
                break
            elif option=='4':
                in_progress=False
                break
            else:
                print('')
                print('Invalid input!')
                print('Please enter an integer value between 1 and 4.')
                print('')
                print_menu()
                print('')
                option = (input('Choose an option: '))

