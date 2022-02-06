from words import Words
from score import Score

words = Words()
score = Score()

for w in words.get_common():
  d = {}
  for c in w:
    d[c] = 0
  if len(d.keys()) < 5:
    print(w)
    
print(word)
print(lowest)
