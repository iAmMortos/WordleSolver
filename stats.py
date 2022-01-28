
with open('rsc/wordle_common_sorted.txt') as f:
  ws = [l.strip() for l in f.readlines()]

data = [{} for _ in range(5)]
data2 = [{} for _ in range(4)]
data3 = [{} for _ in range(3)]

for word in ws:
  for i, c in enumerate(word):
    if c not in data[i]:
      data[i][c] = 0
    data[i][c] += 1
    if i < 4:
      w = word[i:i+2]
      if w not in data2[i]:
        data2[i][w] = 0
      data2[i][w] += 1
    if i < 3:
      w = word[i:i+3]
      if w not in data3[i]:
        data3[i][w] = 0
      data3[i][w] += 1

fr1 = [[] for _ in range(5)]
fr2 = [[] for _ in range(4)]
fr3 = [[] for _ in range(3)]

for i in range(5):
  fr1[i] = [b[0] for b in sorted(data[i].items(), key=lambda t: t[1], reverse=True)]
  if i < 4:
    fr2[i] = [b[0] for b in sorted(data2[i].items(), key=lambda t: t[1], reverse=True)]
  if i < 3:
    fr3[i] = [b[0] for b in sorted(data3[i].items(), key=lambda t: t[1], reverse=True)]

with open('rsc/freq/freq1.txt', 'w') as f:
  f.write('\n'.join(['\t'.join(f) for f in fr1]))
with open('rsc/freq/freq2.txt', 'w') as f:
  f.write('\n'.join(['\t'.join(f) for f in fr2]))
with open('rsc/freq/freq3.txt', 'w') as f:
  f.write('\n'.join(['\t'.join(f) for f in fr3]))
