
from words import Words
import random

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
  
  def new_game(self):
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
    
  def get_colorful_score(self, score):
    out = ''
    for c in score:
      if c == '0':
        out += '⬛️'
      elif c == '1':
        out += '🟨'
      elif c == '2':
        out += '🟩'
    return out
    
  def score(self, guess):
    if guess == self.word:
      return '2'*len(self.word)
    
    gs = list(guess)
    ans = list(self.word)
    result = ['' for _ in range(len(guess))]
    
    for i in range(len(gs)):
      c = gs[i]
      if c == ans[i]:
        ans[i] = '_'
        gs[i] = '_'
        result[i] = '2'
        if c not in self.found:
          self.found.append(c)
        if c in self.fuzzy:
          self.fuzzy.remove(c)
        
    for i in range(len(gs)):
      c = gs[i]
      if c == '_': continue
      if c in ans:
        result[i] = '1'
        ans[ans.index(c)] = '_'
        if c not in self.fuzzy:
          self.fuzzy.append(c)
      else:
        result[i] = '0'
        self.abscent.append(c)
      
    return ''.join(result)


def main():
  wordle = Wordle()
  wordle.new_game()
  while(True):
    guess = input('guess: ')
    print(f'answr: {wordle.word}')
    print(wordle.get_colorful_score(wordle.guess(guess)))
  
  
if __name__ == '__main__':
  main()

