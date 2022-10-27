from p1_random import P1Random

rng = P1Random()

game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
both_wins = 0
no_winners = 0
while game_continue:
    # 1. Set up initial message
    game_num = game_num + 1
    print("START GAME #", game_num)
    player_hand = 0

    # 2. Deal the player a card and assign that card a value
    card = rng.next_int(13) + 1
    player_hand = card
    if card == 1:
        print("")
        print("Your card is a ACE!")
        print("Your hand is:" ,player_hand)

    elif 2 <= card <= 10:
        print("")
        print(f"Your card is a {card}!")
        print("Your hand is:" ,player_hand)

    elif card == 11:
        card = 10
        player_hand = player_hand - 11
        player_hand = player_hand + 10
        print("")
        print("Your card is a JACK!")
        print("Your hand is:" ,player_hand)

    elif card == 12:
        card = 10
        player_hand = player_hand - 12
        player_hand = player_hand + 10
        print("")
        print("Your card is a QUEEN!")
        print("Your hand is:" ,player_hand)


    elif card == 13:
        card = 10
        player_hand = player_hand - 13
        player_hand = player_hand + 10
        print("")
        print("Your card is a KING!")
        print("Your hand is:" ,player_hand)


    # 3. Keep asking users to choose the menu options

    no_winners = True

    while no_winners:

        print("")
        print('1. Get another card')
        print('2. Hold hand')
        print('3. Print statistics')
        print('4. Exit')
        print("")

    #4. ask player to make a choice
        choice = (input("Choose an option:" ))

    #5. Define choice 1
        if choice == '1':
            card = rng.next_int(13) + 1
            player_hand = player_hand + card  # Why is this way correct but player_hand = card + player_hand not correct???
            if card == 1:
                print("")
                print("Your card is a ACE!")
                print("Your hand is:" ,player_hand)
            elif 2 <= card <= 10:
                print("")
                print(f"Your card is a {card}!")
                print("Your hand is:" ,player_hand)
            elif card == 11:
                card = 10
                player_hand = player_hand - 11
                player_hand = player_hand + 10
                print("")
                print("Your card is a JACK!")
                print("Your hand is:" ,player_hand)
            elif card == 12:
                card = 10
                player_hand = player_hand - 12
                player_hand = player_hand + 10
                print("")
                print("Your card is a QUEEN!")
                print("Your hand is:" ,player_hand)
            elif card == 13:
                card = 10
                player_hand = player_hand - 13
                player_hand = player_hand + 10
                print("")
                print("Your card is a KING!")
                print("Your hand is:" ,player_hand)

            if player_hand == 21:
                no_winners = False
                player_wins = player_wins + 1
                print("")
                print("BLACKJACK! You win!")
                print("")
            if player_hand > 21:
                no_winners = False
                dealer_wins = dealer_wins + 1
                print("")
                print("You exceeded 21! You lose.")
                print("")

    # Define choice 2
        elif choice == '2':

            card = rng.next_int(11) + 16
            dealers_hand = card

            if card > 21:
                no_winners = False
                player_wins = player_wins + 1
                print("")
                print("Dealer's hand:",dealers_hand)
                print("Your hand is:" ,player_hand)
                print("")
                print("You win!")
                print("")
            elif card == player_hand:
                no_winners = False
                both_wins = both_wins + 1
                print("")
                print("Dealer's hand:", dealers_hand)
                print("Your hand is:" ,player_hand)
                print("")
                print("It's a tie! No one wins!")
                print("")
            elif card < player_hand:
                no_winners = False
                player_wins = player_wins + 1
                print("")
                print("Dealer's hand:", dealers_hand)
                print("Your hand is:" ,player_hand)
                print("")
                print("You win!")
                print("")
            elif card > player_hand:
                no_winners = False
                dealer_wins = dealer_wins + 1 # THERE MAY BE AN ERROR HERE
                print("")
                print("Dealer's hand:", dealers_hand)
                print("Your hand is:" ,player_hand)
                print("")
                print("Dealer wins!")
                print("")

    #Define choice 3
        elif choice == '3':
            print("")
            print('Number of Player wins:' , player_wins)
            print('Number of Dealer wins:' , dealer_wins)
            print('Number of tie games:' , both_wins)
            print('Total # of games played is: ' , game_num - 1)
            percent_wins = (player_wins / (player_wins + dealer_wins + both_wins))
            percent_wins = percent_wins * 100
            print(f'Percentage of Player wins: {round(percent_wins , 1)}%')

    #Define choice 4
        elif choice == '4':
            no_winners = False
            game_continue = False

        else:
            print('')
            print('Invalid input!\nPlease enter an integer value between 1 and 4.')








                # we have to set up a varaible to count the number of times the player wins
                # if the hand is greater than 21, then we lose... code for that... these are all if statements














