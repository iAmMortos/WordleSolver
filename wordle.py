
class Wordle:
  pass

ws = []
with open('rsc/wordle_list.txt') as f:
  for w in [l.strip() for l in f.readlines()]:
    if len(w) == 5:
      ws += [w]
with open('rsc/wordle_list_2.txt') as f:
  for w in [l.strip() for l in f.readlines()]:
    if len(w) == 5:
      ws += [w]

with open('rsc/wordle_combined.txt', 'w') as f:
  f.write('\n'.join(sorted(ws)))
