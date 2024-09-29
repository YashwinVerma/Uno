import sys
import random
import os
import time

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

def turn_manager(action_type):
    pass

class Card:
    def __init__(self, card_type, card_color, card_number, card_state, current_draw_total):
        self.card_type = card_type
        self.card_color = card_color
        self.card_number = card_number
        self.card_state = card_state
        self.current_draw_total = current_draw_total

    def match_cards(self, matching_object, current_player, current_running_color, request_color):
        color_sensitive_cards = ["SKIP_TURN", "REVERSE_TURN", "DRAW_TWO"]
        if self.card_type != "GENERIC_CARD":
            if self.card_type in color_sensitive_cards:
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
        elif (self.card_color == current_running_color) or (self.card_number == matching_object.card_number):
            current_running_color = self.card_color
            turn_manager("TICK_TURN")
            return True

class Player:
    def __init__(self, player_card_number, draw_total):
        self.player_card_number = player_card_number
        self.draw_total = draw_total

def clear_screen():
    os.system('cls')
