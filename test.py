from words import Words
from score import Score

words = Words()
score = Score()

def find():
  for w in words.get_common():
    if 't' in w and w[4] != 't' and w[0] != 't' and 'r' in w and w[1] != 'r' and w[2] != 'r' and 'a' in w and w[2] != 'a' and w[1] != 'a':
      valid = True
      for c in 'cefghimnosdy':
        if c in w:
          valid = False
          break
      if valid:
        print(w)
        
def main():
  print(words.get_common().index('aroma'))
  print(words.get_common().index('caulk'))
  
main()
