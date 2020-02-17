import random

def primary():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd0 = random.randint(0, last)
  rnd1 = random.randint(0, last)

  print(quotes[rnd0], end="")
  print(quotes[rnd1], end="")

if __name__== "__main__":
  primary()
