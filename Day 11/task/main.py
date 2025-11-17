from art import logo
import random
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def calculate_score(hand):
    score = sum(hand)
    while score > 21 and 11 in hand:
        hand[hand.index(11)] = 1   # convert Ace from 11 to 1
        score = sum(hand)
    return score


def play_game():

    continue_with_another_card=True
    your_cards = [random.choice(cards), random.choice(cards)]
    current_score = calculate_score(your_cards)

    computer_cards = [random.choice(cards)]
    computer_score = calculate_score(computer_cards)

    while continue_with_another_card:
        print(f"your_card: {your_cards} current score:{current_score}")
        print(f"computer's first card: {computer_cards}, computer's first score:{computer_score}")

        another_card_or_not = input("Type Y to get another card, Type n to pass:").upper()
        print (another_card_or_not)

        if another_card_or_not=="Y":
            your_cards.append(random.choice(cards))
            current_score = calculate_score(your_cards)

            computer_cards.append(random.choice(cards))
            computer_score = calculate_score(computer_cards)

        else:
            continue_with_another_card = False
            while computer_score < 17:
                computer_cards.append(random.choice(cards))
                computer_score = calculate_score(computer_cards)

        player_score = calculate_score(your_cards)
        final_computer_score = calculate_score(computer_cards)

        print(f"\nYour final cards: {your_cards}, final score: {player_score}")
        print(f"Dealer's final cards: {computer_cards}, final score: {final_computer_score}")

        if player_score > 21:
            print("You bust! Dealer wins.")
        elif final_computer_score > 21:
            print("Dealer busts! You win!")
        elif player_score > final_computer_score:
            print("You win!")
        elif player_score < final_computer_score:
            print("Dealer wins!")
        else:
            print("Draw!")


play_game()
