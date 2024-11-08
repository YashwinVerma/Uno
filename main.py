import sys
import random
import os
import time

#TODO : .
#Condense card_color into card_type in the card class.
#Fix first card = color changing card issue.
#Finish select_card() function.
colors = {
    "RED" : '\033[91m',
    "GREEN" : '\033[92m',
    "YELLOW" : '\033[93m',
    "BLUE" : '\033[94m',
    "MAGENTA" : '\033[95m',
    "CYAN" : '\033[96m',
    "RESET" : '\033[0m'
}
class CardTypeLists:
    not_generic_card = ["SKIP TURN", "REVERSE TURN", "DRAW TWO", "DRAW_FOUR", "WILD"]
    card_colors = ["RED", "GREEN", "YELLOW", "BLUE"]
    special_color_cards = ["SKIP TURN", "REVERSE TURN", "DRAW TWO"]
    special_color_change_cards = ["DRAW_FOUR", "WILD"]
    all_card_types = ["SKIP TURN", "REVERSE TURN", "DRAW TWO", "DRAW_FOUR", "WILD", "RED", "GREEN", "YELLOW", "BLUE"]

def main():
    global player_order_list
    global running_card_deck
    global special_card_appearence_dict
    main_game_loop = True
    total_players = 0
    player_order_list = []
    current_player = None
    current_card_compare = None
    turn_number = 0
    previous_cards = []
    reject_flag_1 = False
    reject_flag_2 = False
    current_running_color = None
    special_card_appearence_dict = {"SKIP_TURN", f"{self.card_color = }"}
    print("You can type 'exit' at eny statement to exit. Except on integer inputs!")
    time.sleep(1)
    while True:
        clear_screen()
        try:
            total_players = int(input("How many player would you like to have in this game of classic uno as a number (minimum 2 maximum 8): "))
        except ValueError:
            print("Please type a number. Try again!")
        if ((total_players < 2) or (total_players > 8)):
            print("Invalid number of players selected!")
        else:
            break
        clear_screen()
    for i in range(total_players):
        while True:
            player_name = input("Enter a good name for the player(no spaces): ").replace(" ", "").upper()
            clear_screen()
            if ((len(player_name) < 2) or (len(player_name) > 20) or any(player.player_name == player_name for player in player_order_list)):
                print("Invalid name for player! Please try again.")
            else:
                player_order_list.append(Player(player_name))
                break
    running_card_deck = create_deck()
    for i in range(4):
        random.shuffle(running_card_deck)
    full_card_deck = running_card_deck
    while True:
        clear_screen()
        reject_flag_2 = False
        try:
            card_number = int(input("Enter the number of cards you would like to start with for each player in integer form eg(5). Maximum 11 and minimum 4: "))
            if ((card_number > 12) or (card_number < 4)):
                reject_flag_2 = True
        except ValueError:
            print("Your input is either of the wrong datatype or is too large or small.")
            continue
        for i in player_order_list:
            for _ in range(card_number):
                running_card_deck = i.add_card(random.choice(running_card_deck))
        break
    print("This game of uno is about to begin.")
    current_running_card = random.choice(running_card_deck)
    previous_cards.append(current_running_card)
    while main_game_loop:
        input("Press enter to begin turn: ")
        clear_screen()
        current_running_card = current_player.select_card(current_card_compare)
        previous_cards.append(current_running_card)
        print("Player card numbers: ")
        for i in player_order_list:
            for i in range(i.player_card_number):
                running_card_deck = i.add_card(random.choice(running_card_deck))
            print(f"{i.player_name.capitalize()} has {i.player_card_number} cards left.")
        input("Press enter to finish turn: ")
        clear_screen()

def input_func(choices, header):
    selected_index = 0
    while True:
        print(header)
        for index, choice in enumerate(choices):
            if (index == selected_index):
                print(f"> {choice} <")
            else:
                print(f"  {choice}")
        user_input = input("Press 'w' for Up, 's' for Down, or 'Enter' to select: ")
        if (user_input == 'w'):
            selected_index = ((selected_index - 1) % len(choices))
        elif (user_input == 's'):
            selected_index = ((selected_index + 1) % len(choices))
        elif (user_input == ''):
            return choices[selected_index]
        else:
            print("Invalid response")
            time.sleep(0.5)
        clear_screen()

def create_deck():
    card_numbers = list(range(10)) + list(range(1, 10))
    wild_card_appearance = f"{colors['RED']}W{colors['YELLOW']}I{colors['GREEN']}L{colors['BLUE']}D{colors['RESET']}"
    draw_four_appearance = f"{colors['RED']}D{colors['YELLOW']}R{colors['GREEN']}A{colors['BLUE']}W FOUR{colors['RESET']}"
    card_deck = []
    for card_color in CardTypeLists.card_colors:
        for number in card_numbers:
            card_deck.append(Card(card_color, number))
        for special_card in CardTypeLists.special_color_cards:
            card_deck.extend([Card(special_card, None)] * 2)
    for _ in range(4):
        card_deck.append(Card("WILD", None))
        card_deck.append(Card("DRAW FOUR", None))
    return card_deck

def turn_manager(action_type, player_list, current_player):
    if action_type == "TICK_TURN":
        player_list.remove(current_player)
        player_list.append(current_player)
    elif action_type == "REVERSE_TURN":
        player_list.reverse()
    elif action_type == "SKIP_TURN":
        second_player = player_list[1]
        player_list.remove(current_player)
        player_list.remove(second_player)
        player_list.append(current_player)
        player_list.append(second_player)

class Card:
    def __init__(self, card_color, card_number=None):
        self.card_color = card_color
        self.card_number = 10 if card_number is None else card_number

    def calculate_card_appearence(self) -> str:
        if self.card_number != 10:
            return f"{colors[self.card_color]}{self.card_color.capitalize()} {self.card_number}"
        else:
            asdf

    def match_cards(self, matching_object) -> bool:
        if ((self.card_number != 10) or (self.card_color in CardTypeLists.special_color_cards)):
            if ((self.card_color == matching_object.card_color) or (self.card_color == matching_object.card_color)):
                return True
        else:
            pass


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_cards = []
        self.player_card_number = len(self.player_cards)
        self.draw_total = 0

    def add_card(self, new_card_add) -> list:
        self.player_cards.append(new_card_add)
        running_card_deck.remove(new_card_add)
        return running_card_deck

    def select_card(self, compare_card) -> None:
        colors_request = [f"{colors['BLUE']}/tBlue", f"{colors['RED']}/tRed", f"{colors['GREEN']}/tGreen", f"{colors['YELLOW']}/tYellow"]
        display_header = compare_card.calculate_card_appearence() + "\nThe current color is: " + current_running_color_input.capitalize()
        player_cards_dict = {}
        for i in player_cards:
            player_cards_dict[i] = i.card_appearence
        cards_display = ["\t" + x for x in player_cards_dict.values()]
        while True:
            selected_card_appearence = input_func(cards_display, display_header)
            exit_statement(selected_card_appearence)
            selected_card = next((k for k, v in player_cards_dicts.items() if v == selected_card_appearence), None)
            if selected_card.card_type in CardTypeLists.special_color_change_cards:
                current_running_color_input = input_func("Please choose the color that you want to change to as you have chosen a card that allows you do such: ", colors_request)
               
def clear_screen():
    print("\033c")

def exit_statement(statement_check):
    if (statement_check.upper().replace(" ", "") == "EXIT"):
        exit()

main()
