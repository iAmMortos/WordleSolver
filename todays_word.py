import datetime


start = datetime.date(2021, 6, 19)
today = datetime.date.today()
# today = datetime.date(2022, 2, 11)
delta = today - start

with open('rsc/wordle_common.txt') as f:
  ws = f.read().split('\n')
  
print(f'Today\'s word: "{ws[delta.days]}"')
