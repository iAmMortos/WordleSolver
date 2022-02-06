
class Score:
  def __init__(self):
    self.f1 = []
    self.f2 = []
    self.f3 = []
    self.av1 = 0
    self.av2 = 0
    self.av3 = 0

    self.load_freq()

  def load_freq(self):
    with open('rsc/freq/freq1.txt') as f:
      self.f1 = [a.split('\t') for a in f.read().split('\n')]
    with open('rsc/freq/freq2.txt') as f:
      self.f2 = [a.split('\t') for a in f.read().split('\n')]
    with open('rsc/freq/freq3.txt') as f:
      self.f3 = [a.split('\t') for a in f.read().split('\n')]
  
  def score(self, word):
    sc1 = 0
    sc2 = 0
    sc3 = 0
    
    w1 = 1
    w2 = 0
    w3 = 0
    
    for i in range(5):
      w = word[i]
      if w not in self.f1[i]:
        sc1 += len(self.f1[i]) ** 2
      else:
        sc1 += self.f1[i].index(w) ** 2
      
    for i in range(4):
      w = word[i:i+2]
      if w not in self.f2[i]:
        sc2 += len(self.f2[i]) ** 2
      else:
        sc2 += self.f2[i].index(w) ** 2
      
    for i in range(3):
      w = word[i:i+3]
      if w not in self.f3[i]:
        sc3 += len(self.f3[i]) ** 2
      else:
        sc3 += self.f3[i].index(w) ** 2
    # print(sc1, sc2, sc3)
    
    return w1 * sc1 + w2 * sc2 + w3 * sc3
    
    
def main():
  s = Score()
  while True:
    word = input()
    print(s.score(word))


if __name__ == '__main__':
  main()

