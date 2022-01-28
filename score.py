
class Score:
  def __init__(self):
    self.f1 = []
    self.f2 = []
    self.f3 = []

    self.load_freq()

  def load_freq(self):
    with open('rsc/freq/freq1.txt') as f:
      self.f1 = [a.split('\t') for a in f.read().split('\n')]
    with open('rsc/freq/freq2.txt') as f:
      self.f2 = [a.split('\t') for a in f.read().split('\n')]
    with open('rsc/freq/freq3.txt') as f:
      self.f3 = [a.split('\t') for a in f.read().split('\n')]
    print("hello lol")

s = Score()