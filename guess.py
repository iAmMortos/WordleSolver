
from clue import Clue
from clue_color import ClueColor


class Guess (object):
  def __init__(self, word, colors):
    if len(word) != len(colors):
      raise Exception('Must be same length')
    self.clues = []
    for i, c in enumerate(word):
      self.clues += [Clue(c, colors[i])]
      
  @property
  def word(self):
    return ''.join([c.letter for c in self.clues])
    
  @property
  def colors(self):
    return [c.color for c in self.clues]
    
  @property
  def colorstr(self):
    s = ''
    for c in self.clues:
      clr = c.color
      if clr == ClueColor.BLACK:
        s += '⬛️'
      elif clr == ClueColor.YELLOW:
        s += '🟨'
      elif clr == ClueColor.GREEN:
        s += '🟩'
    return s
    
  def __repr__(self):
    s = ''
    for c in self.clues:
      s += f'{c.color}{c.letter}'
    return s

if __name__ == '__main__':
  g = Guess('crane', [ClueColor.BLACK, ClueColor.BLACK, ClueColor.YELLOW, ClueColor.GREEN, ClueColor.BLACK])
  
  print(g.colorstr)
