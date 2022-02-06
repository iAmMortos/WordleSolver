
class Words (object):
  def __init__(self):
    self.common = []
    self.uncommon = []
    
    self.load_words()
    
  def load_words(self):
    with open('rsc/wordle_common_sorted.txt') as f:
      self.common = f.read().split('\n')
    with open('rsc/wordle_valid_uncommon.txt') as f:
      self.uncommon = f.read().split('\n')
      
  def is_word(self, word):
    return word in self.common or word in self.uncommon
  
  def get_common(self):
    return self.common[:]
    
  def get_uncommon(self):
    return self.uncommon[:]
    
  def get_all(self):
    return sorted(self.common + self.uncommon)
