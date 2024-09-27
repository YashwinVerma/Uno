import sys
import random
import os
import time

def input_func(choices):
  while True:
    for index, choice in enumerate(choices):
      if (index == selected_index):
        print(f"> {choice} <")
          else:
            print(f"  {choice}")
        user_input = input("Press 'w' for Up, 's' for Down, or 'Enter' to select: ")
    if (user_input == 'w'):
      selected_index = (selected_index - 1) % len(choices)
    elif (user_input == 's'):
      selected_index = (selected_index + 1) % len(choices)
    elif (user_input == ''):
      return choice
    else:
      print("Invalid response")
      time.sleep(0.5)
    clear_screen()

class Card:
  def __init__(self, card_type, card_color, card_number, card_state):
    self.card_type = card_type
    self.card_color = card_color
    self.card_number = card_number
    self.card_state = card_state
  def match_cards(self, matching_object, current_color):
    turn_manager_triggers = ["SKIP_TURN", "REVERSE_TURN", ""]
    if (self.card_type != "GENERIC_CARD"):
      turn_manager(self.card_type)
    elif (self.card_color == current_running_color) or (self.card_number == matching_object.card_number):
      turn_manager("TICK_TURN")
      return True

class Player:
  def __init__(self)

def clear_screen():
  print("\033[2J\033[H", end='')
