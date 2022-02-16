
from words import Words
from clue_color import ClueColor


class WordBank (object):
  def __init__(self):
    w = Words()
    self.common = w.get_common()
    self.uncommon = w.get_uncommon()
    
  def guess(self, guess):
    self.common = self._reduce(self.common, guess)
    self.uncommon = self._reduce(self.uncommon, guess)
    
  @property
  def words(self):
    return self.common + self.uncommon
    
  @property
  def status(self):
    return f'{len(self.words)} words left.\n{self.words}'
        
  def _reduce(self, words, guess):
    ws = []
    for w in words:
      ls = list(w)
      valid = True
      for i,c in enumerate(guess.clues):
        if c.color == ClueColor.GREEN:
          if ls[i] != c.letter:
            valid = False
            break
          else:
            ls[i] = '_'
      if not valid:
        continue
            
      for i,c in enumerate(guess.clues):
        if c.color == ClueColor.YELLOW:
          if c.letter not in ls or ls[i] == c.letter:
            valid = False
            break
          else:
            ls[ls.index(c.letter)] = '_'
      if not valid:
        continue
      
      for i,c in enumerate(guess.clues):
        if c.color == ClueColor.BLACK:
          if c.letter in ls:
            valid = False
            break
        
      if valid:
        ws += [w]
    return ws

