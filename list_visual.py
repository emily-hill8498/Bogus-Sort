from time import sleep
import tkinter

class screen:
  def __init__(self, title, MULS=50):
    self.MULS = MULS
    self.window = tkinter.Tk()
    self.window.title(title)

  def init_canvas(self, listSize):
    self.width = listSize*self.MULS
    self.height = listSize*self.MULS
    self.canvas = tkinter.Canvas(self.window, width=self.width, height=self.height, bg='black')
    self.canvas.pack()
    self.window.update()
    
  def visualize_list(self, list):
    self.canvas.delete('all')
    for i in range(len(list)):
      self.canvas.create_rectangle(i*self.MULS, self.height, (i+1)*self.MULS, self.height-list[i]*self.MULS, outline='', fill='white')
    self.canvas.pack()
    self.window.update()
    # sleep(1)

# print('test')