from question_asker import *
from deck import *
from dealer import *
from player import *

qa = QuestionAsker()

def clear_screen():
  print('\n' * 59)

class Table:
############################
  def __init__(self):
    self.m_dealer = Dealer()

############################
  def setup(self):
    self.set_deck()
    self.set_limits()
    self.set_players()

############################
  def simultaion(self):
    while(True):
      self.play_an_entire_hand()
      play_again = self.ask_play_again()

      if(play_again == 1):
        continue
      elif(play_again == 2):
        break

    self.player_money_print()

############################
  def set_deck(self):
    clear_screen()
    while(True):
      num_decks = qa.aquire_int("How many decks are we going to use? ")
      if(num_decks < 1):
        print("We must play with a positive number of decks.")
      else:
        break
    self.m_deck = Deck(num_decks)

############################
  def set_limits(self):
    clear_screen()
    #minimum bet setting
    while(True):
      self.min_bet = qa.aquire_int("What is the minimum bet? ")
      if(self.min_bet < 1):
        print("Minimum bet must be greater than 0.")
      else:
        break

    #maximum bet setting
    while(True):
      self.max_bet = qa.aquire_int("And the maximum bet? ")
      if(self.max_bet < 5 * self.min_bet):
        print("Maximum bet must be at least 5 times the minimum bet.")
      else:
        break

############################
  def set_players(self):
    clear_screen()
    num_players = 0
    while(num_players < 1):
      num_players = qa.aquire_int("How many players are playing? ")
    
    self.players = []
    for i in range(0, num_players):
      name = input("Player " + str(i + 1) + "'s name: ")
      tmp = Player(name)
      self.players.append(tmp)

############################
#########THE BEEF###########
############################
  def play_an_entire_hand(self):
      self.set_hands_for_players()
      clear_screen()
      print("Playing Blackjack with " \
            + str(len(self.players)) \
            + " players.")
      for player in self.players:
        print(player.name + " is playing " + str(len(player.hands)))
        for hand in player.hands:
          print(hand)
      #self.starting_deal()

############################
  def ask_play_again(self):
    while(True):
      play_again = input("Play again? (y/n) ")
      if(play_again == 'y' or play_again == 'Y'):
        return 1
      if(play_again == 'n' or play_again == 'n'):
        return 2

############################
  def set_hands_for_players(self):
    clear_screen()
    for player in self.players:
      while(True):
        while(True):
          num_hands = qa.aquire_int("How many hands does "\
                              + player.name + " want to play? ")
          if(num_hands < 1):
            print(player.name + " must play a positive number of hands")
          else:
            break
        while(True):
          bet = qa.aquire_int("And the bet? ("\
                              + str(self.min_bet) + "-"\
                              + str(self.max_bet) + ") ")
          if(bet < self.min_bet):
            print(player.name + " must bet more than " + str(self.min_bet))
          elif(bet > self.max_bet):
            print(player.name + " must bet less than " + str(self.max_bet))
          else:
            break

        total_bet = num_hands * bet

        if(not player.can_afford(total_bet)):
          print(player.name + " can not afford this bet of " + str(total_bet))
          continue
        else:
          for i in range(0, num_hands):
            tmp = Hand(bet)
            player.hands.append(tmp)
          break

############################
  def player_money_print(self):
    for i in self.players:
      print(i)
