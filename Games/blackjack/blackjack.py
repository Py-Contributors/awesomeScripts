import random
from time import sleep

try:
    # Variables (7)
    player_hand = []
    dealer_hand = []
    player_hand2 = []
    dealer_hand2 = []
    player_hand_value = 0
    dealer_hand_value = 0
    first_draw = 0

    # Set Values (2)
    deck = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    # Defined Functions (8)
    def deal_hand():
        global first_draw
        first_draw = 0
        player_hand.clear()
        dealer_hand.clear()
        player_hand2.clear()
        dealer_hand2.clear()
        player_hand.append(random.sample(deck, 2))
        dealer_hand.append(random.sample(deck, 2))
        for x in player_hand[0]:
            player_hand2.append(str(x) + " of " + random.choice(suits))
        for x in dealer_hand[0]:
            dealer_hand2.append(str(x) + " of " + random.choice(suits))
        print(
            "---------------------------------------------------------"
        )
        print("Dealing out cards.....\n")
        sleep(1)
        print(
            f"Your hand contains '{str(player_hand2[0])}' and " +
            "'{str(player_hand2[1])}'.\n"
        )
        hand_value()

    def hand_value():
        global player_hand_value
        player_hand_value = 0
        # Player Hand
        for x in player_hand[0]:
            if x == "Ace":
                player_hand_value += 11
        for x in deck[0:9]:
            for j in player_hand[0]:
                if j == x:
                    player_hand_value += int(x)
        for x in deck[9:12]:
            for j in player_hand[0]:
                if j == x:
                    player_hand_value += 10
        if player_hand_value > 21:
            if "Ace" in player_hand[0]:
                player_hand_value -= 10
        print(f"Your hand value is {player_hand_value}.\n")
        hit_stay()

    def hit_stay():
        global first_draw
        if first_draw == 0:
            print("The dealer draws two cards and reveals " +
                  f"'{str(dealer_hand2[0])}'.\n")
            first_draw += 1
        if player_hand_value <= 21:
            hit_stay_choice = ""
            while hit_stay_choice != "hit" or "stand":
                hit_stay_choice = input("Do you want to hit or stand? ")
                sleep(1.2)
                if hit_stay_choice == "hit":
                    player_hand[0].append(random.choice(deck))
                    player_hand2.append(
                        str(player_hand[0][-1]) + " of " + random.choice(suits)
                    )
                    print(player_hand2)
                    print(f"You were dealt '{str(player_hand2[-1])}'.\n")
                    hand_value()
                if hit_stay_choice == "stand":
                    sleep(2)
                    reveal_dealer_hand()
        elif player_hand_value > 21:
            print("Your hand went over 21! You busted! \n")
            ask_game()

    def reveal_dealer_hand():
        global dealer_hand_value
        dealer_hand_value = 0
        # Dealer Hand
        for x in dealer_hand[0]:
            if x == "Ace":
                dealer_hand_value += 11
        for x in deck[0:9]:
            for j in dealer_hand[0]:
                if j == x:
                    dealer_hand_value += int(x)
        for x in deck[9:12]:
            for j in dealer_hand[0]:
                if j == x:
                    dealer_hand_value += 10
        if dealer_hand_value > 21:
            if "Ace" in dealer_hand[0]:
                dealer_hand_value -= 10
        print(
            f"\nThe dealer's hand is {str(dealer_hand2)} " +
            "with a value of {dealer_hand_value}. "
        )
        if dealer_hand_value <= 16:
            dealer_hit()
        if dealer_hand_value > 16:
            dealer_stay()

    def dealer_hit():
        global dealer_hand
        global dealer_hand_value
        dealer_hand[0].append(random.choice(deck))
        dealer_hand2.append(str(dealer_hand[0][-1]) + " of " +
                            random.choice(suits))
        print(f"The dealer hits and draws '{dealer_hand2[-1]}'.")
        reveal_dealer_hand()

    def dealer_stay():
        if player_hand_value > dealer_hand_value:
            if player_hand_value <= 21:
                win_game()
            if player_hand_value > 21:
                print("Your hand went over 21! You busted! \n")
                sleep(1)
                ask_game()
        if player_hand_value < dealer_hand_value:
            if dealer_hand_value <= 21:
                print(
                    "The dealer has a greater hand value than yours at " +
                    f"{dealer_hand_value} opposed to your {player_hand_value}!"
                    "\nYou lose the game! \n",
                    sep="\n",
                )
                sleep(0.5)
                ask_game()
            if player_hand_value > 21:
                print("Your hand went over 21! You busted! \n")
                ask_game()
            if dealer_hand_value > 21 and player_hand_value <= 21:
                win_game()
        if dealer_hand_value == 21 == player_hand_value:
            print("You both have tied at 21!!")
            sleep(0.5)
            ask_game()
        if int(dealer_hand_value) == int(player_hand_value):
            print(f"You both have tied at {player_hand_value}!!")
            sleep(0.5)
            ask_game()

    def win_game():
        print(
            "\nYour hand value was " +
            f"{player_hand_value} while the dealer's hand " +
            f"value was {dealer_hand_value}."
        )
        sleep(1)
        if dealer_hand_value > 21:
            print("The dealer's hand went over 21! You win!! \n")
        print("You win! Congrats!! \n")
        if player_hand_value == 21:
            print(
                "You have a perfect score of 21! You scored a BlackJack! " +
                "Congrats!! \n"
            )
        ask_game()

    def ask_game():
        new_game = input("Do you want to play a new game? 'Yes' or 'No' ")
        if (new_game == "Yes" or new_game == "yes" or new_game == "y"
                or new_game == "Y"):
            print(
                "------------------------------------------------------------"
            )
            deal_hand()
        elif (new_game == "No" or new_game == "no" or new_game == "n" or
                new_game == "N"):
            print("\nGoodbye! Nice playing with you! ")
            sleep(4)
            quit()

    # The Game
    print(
            "\t\t\t\t\t    B.L.A.C.K.J.A.C.K",
            "\n",
            "\n                                               THE RULES",
            "\n",
            "\nThe rules of the game are simple:",
            "\n",
            "\nObjective: To have a higher score(hand value) than the " +
            "dealer but at the same time to not go over 21.",
            "\n",
            "\n1. You get a pre-dealt pair of cards from the dealer. " +
            "These two cards' value will be calculated as your score.",
            "\n2. The values of the cards King, Queen, Jack have 10 points " +
            "each and the rest of the cards (2-10) have their unit values.",
            '\n3. "Hit" means to draw another card (the value will be added ' +
            'to your hand) and if you feel your hand value is capable of' +
            ' having another card, you may "hit" to get another card',
            '\n4. "Stand" means that you are currently not drawing any card ' +
            'and thus the hand value will not change and if you are' +
            'satisfied with your hand, you may "stand" with it.',
            '\n5. If anyone\'s hand value goes over 21, they automatically ' +
            'lose or "bust".',
            '\n6. The Ace card value can change between 11 or 1 depending ' +
            'on the overall value of the hand.',
            "\n",
            '\nALL THE BEST AND HAVE FUN! \n', end="\n"
    )

    input("Press Enter to start the game ")
    deal_hand()
except Exception:
    print()
