import sys
import random
import os
import time

def main():
    main_game_loop = True
    total_players = 0
    player_order_list = []
    reject_flag_1 = False
    while True:
        try:
            total_players = int(input("How many player would you like to have in this game of classic uno as a number(eg. 2) maximum 8: "))
        except ValueError:
            print("Wrong datatype. Try again!")
        if (total_players < 2) or (total_players > 8):
            print("Invalid number of players selected!")
        clear_screen()
    for i in range(total_players):
        while True:
            new_player = input("Enter a good name for the player: ").replace(" ", "")
            if len(new_player) < 20 or len(new_player) > 1:
                if new_player in player_order_list:
                    reject_flag_1 = True
                else:
                    player_order_list.append(new_player)
                    break
            else:
                reject_flag = True
            if reject_flag == True:
                print("Invalid player name! Please Try again.")
    running_card_deck = create_deck()
    
    
def input_func(choices):
    selected_index = 0  # Initialize selected_index
    while True:
        for index, choice in enumerate(choices):
            if index == selected_index:
                print(f"> {choice} <")
            else:
                print(f"  {choice}")
        user_input = input("Press 'w' for Up, 's' for Down, or 'Enter' to select: ")
        if user_input == 'w':
            selected_index = (selected_index - 1) % len(choices)
        elif user_input == 's':
            selected_index = (selected_index + 1) % len(choices)
        elif user_input == '':
            return choices[selected_index]  # Return the selected choice
        else:
            print("Invalid response")
            time.sleep(0.5)
        clear_screen()

def create_deck():
    card_colors = ["RED", "YELLOW", "GREEN", "BLUE"]
    card_numbers = list(range(10)) + list(range(1, 10))
    special_cards = ["SKIP_TURN", "REVERSE_TURN", "DRAW_TWO"]
    wild_cards = ["WILD", "DRAW_FOUR"]
    card_deck = []
    for color in card_color:
        for number in card_numbers:
            card_deck.append(Card("GENERIC_CARD", color, number, None))
        for special_card in special_cards:
            card_deck.extend([Card(special_card, color, None, None)] * 2)
    for _ in range(4):
        for i in wild_cards:
            card_deck.append(Card(i, None, None, None))
    return card_deck

def turn_manager(action_type):
    pass

class Card:
    def __init__(self, card_type, card_color, card_number, card_possession):
        self.card_type = card_type
        self.card_color = card_color
        self.card_number = card_number
        self.card_possession = card_possession

    def match_cards(self, matching_object, current_player, current_running_color, request_color):
        color_sensitive_cards = ["SKIP_TURN", "REVERSE_TURN", "DRAW_TWO"]
        if (self.card_type != "GENERIC_CARD"):
            if (self.card_type in color_sensitive_cards):
                if self.card_color == current_running_color:
                    if self.card_type == "DRAW_TWO":
                        current_player.draw_total += 2
                        return True
                    else:
                        turn_manager(self.card_type)
                        return True
                else:
                    return False
            else:
                current_running_color = request_color
                if self.card_type == "DRAW_FOUR":
                    current_player.draw_total += 4
        elif ((self.card_color == current_running_color) or (self.card_number == matching_object.card_number)):
            current_running_color = self.card_color
            turn_manager("TICK_TURN")
            return True

class Player:
    def __init__(self, player_card_number, draw_total):
        self.player_card_number = player_card_number
        self.draw_total = draw_total

def clear_screen():
    os.system('cls')
