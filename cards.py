# class Card
class Card:
  def __init__(self, word, location):
    self.card = word
    # location
    self.location = location
    self.matched = False

  # __eq__
  def __eq__(self, other):
    return self.card == other.card

  # __str__
  def __str__(self):
    return self.card
  
# __dunder main___
if __name__ == "__main__":
  card1 = Card("egg", "A1")
  card2 = Card("egg", "B1")
  card3 = Card("spider", "A2")
  
  print(card1 == card2)
  print(card1 == card3)
  print(card3)
  