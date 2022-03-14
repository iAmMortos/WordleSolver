import ui
#from clue_color import ClueColor

class GuessView (ui.View):
  def did_load(self):
    self.lbls = [
      self['lbl0'],
      self['lbl1'],
      self['lbl2'],
      self['lbl3'],
      self['lbl4']]
    self.flex = 'WTB'
    
  def init(self, guess):
    return
    for i,c in enumerate(guess.clues):
      lbl = self.lbls[i]
      lbl.text = c.letter
      lbl.border_width = 0
      if c.color == ClueColor.GREEN:
        lbl.background_color = '#608b54'
      elif c.color == ClueColor.YELLOW:
        lbl.background_color = '#b19f4c'
      elif c.color == ClueColor.BLACK:
        lbl.background_color = '#3a3a3b'
    
  @staticmethod
  def load_view(guess):
    v = ui.load_view()
    v.init(guess)
    return v
    
    
if __name__ == '__main__':
  v = ui.View()
  fw = v.width
  v.background_color = '#121213'
  gv = GuessView.load_view(None)
  gv.width = fw
  v.add_subview(gv)
  v.present()
