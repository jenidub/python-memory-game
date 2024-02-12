from cards import Card
import random

# class Game
class Game:
  def __init__(self):
    # grid size
    self.size = 4
    
    # list of card options
    self.card_options = ["time", "bank", "book", "hope", 
                         "cash", "farm", "sign", "game"]
    # columns for the top row
    self.columns = ["A", "B", "C", "D"]
    self.cards = []
    
    # list of locations in grid
    self.locations = []
    for column in self.columns:
      for number in range(1,5):
        self.locations.append(f"{column}{number}")

# method: create the Card instance with words and location
  def set_cards(self):
    used_locations = []
    for word in self.card_options:
      for i in range(2):
         available_locations = set(self.locations) - set(used_locations)
         random_location = random.choice(list(available_locations))
         used_locations.append(random_location)
         card = Card(word, random_location)
         self.cards.append(card)
    for card in self.cards:
      print(card.card, card.location)
    
# method: create a grid row
  def create_row(self, num):
    row = []
    for column in self.columns:
      for card in self.cards:
        if card.location == f"{column}{num}":
          if card.matched:
            row.append(f" {str(card)}")
          else:
            row.append("     ")
    return row
  
# method: create a grid row
  def create_grid(self):
    header = "  |   "
    header += ("   |    ").join(self.columns)
    header += "   |"
    print(header)
    for row_num in range(1,self.size + 1):
      print_row = f" {row_num}|"
      get_row = self.create_row(row_num)
      print_row += "  | ".join(get_row) + "  |"
      print(print_row)
      
# method: check for matches
  def check_match(self, location1, location2):
    if location1 == "exit" or location2 == "exit":
      return False
    match_check = []
    for card in self.cards:
      if card.location == location1 or card.location == location2:
        match_check.append(card)
    if match_check[0].card == match_check[1].card:
        match_check[0].matched = True
        match_check[1].matched = True
        return True
    else:
        return False

# method: check if game is won
  def check_win(self):
    for card in self.cards:
      if card.matched == False:
        return False
    return True
  
# method: check location entry
  def check_location(self, time):
    while True:
      guess = input(f"What's the location of your {time} card?  ")
      if guess == "exit":
        break
      if guess.upper() in self.locations:
        return guess.upper()
        break
      else:
        print("Your guess is not valid. It should look like this: A1")
    
# method: run the game
  def start_game(self):
      game_running = True
      print("Welcome to the Memory Game by JeniDub")
      self.set_cards()
      while game_running == True:
        self.create_grid()
        guess1 = self.check_location('first')
        guess2 = self.check_location('second')
        if self.check_match(guess1, guess2):
          if self.check_win():
            print("Congrats! You have guessed them all!")
            self.create_grid()
            game_running = False
        else:
          input("Those cards are not a match. Press enter to continue.")
      print("GAME OVER. Have a nice day!")

#dunder main testing protocols
if __name__ == "__main__":
  new_game = Game()
  new_game.start_game()
  