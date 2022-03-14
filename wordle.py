
from words import Words
from clue_color import ClueColor
from guess import Guess
from wordbank import WordBank
import random
import clipboard

class Wordle (object):
  def __init__(self):
    self.words = Words()
    
    self.guesses = []
    self.found = []
    self.fuzzy = []
    self.abscent = []
    self.word = None
    self.cur_turn = 0
    self.total_turns = 6
  
  def new_game(self, word=None):
    if word:
      self.word = word
    else:
      self.word = random.choice(self.words.get_common())
    self.guesses = []
    self.found = []
    self.fuzzy = []
    self.abscent = []
    self.cur_turn = 0
    self.total_turns = 6
  
  def guess(self, word):
    cur = word
    self.guesses += [cur]
    self.cur_turn += 1
    return self.score(word)
    
  def score(self, guess):
    if guess == self.word:
      return Guess(guess, [ClueColor.GREEN]*len(self.word))
    
    gs = list(guess)
    ans = list(self.word)
    result = [None for _ in range(len(guess))]
    
    for i in range(len(gs)):
      c = gs[i]
      if c == ans[i]:
        ans[i] = '_'
        gs[i] = '_'
        result[i] = ClueColor.GREEN
        if c not in self.found:
          self.found.append(c)
        if c in self.fuzzy:
          self.fuzzy.remove(c)
        
    for i in range(len(gs)):
      c = gs[i]
      if c == '_': continue
      if c in ans:
        result[i] = ClueColor.YELLOW
        ans[ans.index(c)] = '_'
        if c not in self.fuzzy:
          self.fuzzy.append(c)
      else:
        result[i] = ClueColor.BLACK
        self.abscent.append(c)
      
    return Guess(guess, result)


def main():
  wordle = Wordle()
  wb = WordBank()
  wordle.new_game()
  debug = False
  helper = False
  print(wordle.word, end='\n'*50)
  while(True):
    if debug:
      guess = input(f'guess ({wordle.word}): ')
    else:
      guess = input(f'guess: ')
    g = wordle.guess(guess)
    clipboard.set(g.colorstr)
    print(g.colorstr)
    if helper:
      wb.guess(g)
      print(wb.status)
  
  
if __name__ == '__main__':
  main()

