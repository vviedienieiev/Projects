
import random
import art
from replit import clear

def initiate_account():
    print(art.logo)
    print("Welcome in blackjack casino!")
    while True:
        balance = input("Please select your initial balance: 500, 1000, 5000, 10000\n")
        if balance not in ["500", "1000", "5000", "10000"]:
            print("You selected the wrong balance. Please try again.")
        else:
            return int(balance)

def make_a_bet(balance):
    while True:
        bet = int(input("Please select your bet: \n"))
        if bet > balance:
            print("You don't have enough money")
        else:
            print(f"You made a ${bet} bet and your remaining balance is ${balance - bet}")
            return balance - bet, bet

def get_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def select_first_cards():
    gamer_cards = [get_a_card(), get_a_card()]
    dealer_cards = [get_a_card()]
    print(f"Your cards are {gamer_cards}")
    print(f"Dealer`s card is {dealer_cards}")
    return gamer_cards, dealer_cards

def ask_for_split(balance, bet, gamer_cards):
    if (gamer_cards[0] == gamer_cards[1]):
        if bet <= balance:
            is_split = input("Do you want to split your cards?(Y/N)\n").lower()
            if is_split == "y":
                print(f"New balance is: {balance - bet}")
                new_hand = {"First hand": {"cards": [gamer_cards[0], get_a_card()],
                                           "bet": bet},
                            "Second hand": {"cards": [gamer_cards[1], get_a_card()],
                                            "bet": bet}}
                for hand in new_hand:
                    print(f"{hand} is {new_hand[hand]['cards']}")
                return balance - bet, new_hand
        else:
            print("You don't have enough money to make a split")
    return balance, {"First hand": {"cards": [gamer_cards[0], gamer_cards[1]],
                                    "bet": bet}}

def deal_with_ace(any_cards):
    if (calculate_score(any_cards) > 21) & (11 in any_cards):
        for i in range(len(any_cards)):
            if any_cards[i] == 11:
                any_cards[i] = 1
                break
    return any_cards

def calculate_score(any_cards):
    return sum(any_cards)

def calculate_dealers_score(dealers_cards):
    dealer_turn = True
    while dealer_turn:
        if calculate_score(dealers_cards) < 17:
            dealers_cards.append(get_a_card())
            dealers_cards = deal_with_ace(dealers_cards)
        else:
            dealer_turn = False
    dealers_score = calculate_score(dealers_cards)
    is_blackjack = False
    if (len(dealers_cards) == 2) & (dealers_score == 21):
        print("Dealer got Blackjack!")
        is_blackjack = True
    print(f"Final dealer`s cards are {dealers_cards}")
    return {"Dealer_cards": dealers_cards, "Dealer_scores": dealers_score, "Blackjack": is_blackjack}

def play(gamer_cards):
    game_result = {}
    for hand in gamer_cards:
        user_turn_in_progress = True
        while user_turn_in_progress:
            is_blackjack = False
            print(f"Your current hand is {gamer_cards[hand]['cards']}")
            if calculate_score(gamer_cards[hand]['cards']) == 21:
                if len(gamer_cards[hand]['cards']) == 2:
                    is_blackjack = True
                    game_result.update({hand: {"Cards": gamer_cards[hand]['cards'],
                                               "Score": calculate_score(gamer_cards[hand]['cards']),
                                               "Bet": gamer_cards[hand]['bet'],
                                               "Blackjack": is_blackjack}})
                else:
                    game_result.update({hand: {"Cards": gamer_cards[hand]['cards'],
                                               "Score": calculate_score(gamer_cards[hand]['cards']),
                                               "Bet": gamer_cards[hand]['bet'],
                                               "Blackjack": is_blackjack}})
                user_turn_in_progress = False
            else:
                choice = input("Do you want Hit or Stand? (H\S)\n").lower()
                if choice != "h":
                    game_result.update({hand: {"Cards": gamer_cards[hand]['cards'],
                                                "Score": calculate_score(gamer_cards[hand]['cards']),
                                                "Bet": gamer_cards[hand]['bet'],
                                                "Blackjack": is_blackjack}})
                    user_turn_in_progress = False
                else:
                    gamer_cards[hand]['cards'].append(get_a_card())
                    gamer_cards[hand]['cards'] = deal_with_ace(gamer_cards[hand]["cards"])
                    if sum(gamer_cards[hand]['cards']) > 21:
                        game_result.update({hand: {"Cards": gamer_cards[hand]['cards'],
                                                    "Score": calculate_score(gamer_cards[hand]['cards']),
                                                    "Bet": gamer_cards[hand]['bet'],
                                                    "Blackjack": is_blackjack}})
                        user_turn_in_progress = False
        print(f"Your final result for this hand is {game_result[hand]['Cards']}")
    return game_result

def calculate_game_result(user_result, dealer_result):
    income = 0
    for hand in user_result:
        if (user_result[hand]["Blackjack"] == True) & (dealer_result["Blackjack"] == True):
            result = 0
        elif (user_result[hand]["Blackjack"] == True) & (dealer_result["Blackjack"] != True):
            result = 1
        elif (user_result[hand]["Blackjack"] != True) & (dealer_result["Blackjack"] == True):
            result = -1
        elif user_result[hand]["Score"] > 21:
            result = -1
        elif dealer_result["Dealer_scores"] > 21:
            result = 1
        elif user_result[hand]["Score"] == dealer_result["Dealer_scores"]:
            result = 0
        elif user_result[hand]["Score"] > dealer_result["Dealer_scores"]:
            result = 1
        elif user_result[hand]["Score"] < dealer_result["Dealer_scores"]:
            result = -1
        if result == 0:
            print("Draw!")
            income += user_result[hand]["Bet"]
        elif result == 1:
            print("You win!!!")
            income += user_result[hand]["Bet"]*2
        elif result == -1:
            print("You lose!!!")
    return income



balance = initiate_account()
play_again = True
while play_again:
    clear()
    print(f"Your current balance is ${balance}")
    initial_balance, bet = make_a_bet(balance)
    gamer_cards, dealer_cards = select_first_cards()
    new_balance, gamer_cards = ask_for_split(initial_balance, bet, gamer_cards)
    for hand in gamer_cards:
        gamer_cards[hand]["cards"] = deal_with_ace(gamer_cards[hand]["cards"])
    user_result = play(gamer_cards)
    dealer_result = calculate_dealers_score(dealer_cards)
    income = calculate_game_result(user_result, dealer_result)
    if income > 0:
        new_balance += income
    print(f"In this round you balanced changed by ${new_balance-balance}. The current balance is ${new_balance}")
    balance = new_balance
    choice_play_again = input("Do you want to play 1 more round?(Y/N)\n").lower()
    if choice_play_again != "y":
        play_again = False
        print(f"You left the casino with ${balance}")
