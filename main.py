from random import randint
from time import sleep
import tkinter


class screen:
  def __init__(self):
    self.MULS = 50
    self.window = tkinter.Tk()
    self.window.title('Bogus-Sort')

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

def gen_unsorted(len):
  list = []
  for _i in range(len):
    list.append(randint(1, len))
  return list

# your bogo sort is fake
def bogo_sort(list, visualized=False, visualizer=''):
  sorted = False
  while not sorted:
    for i in range(len(list)-1):
      if randint(0, 1) == 1:
        x = list[i]
        list[i] = list[i+1]
        list[i+1] = x
    if visualized:
      visualizer.visualize_list(list)
    y = list.copy()
    y.sort()
    if list == y:
      sorted = True
  return list

lescreen = screen()
lescreen.init_canvas(5)
lescreen.visualize_list([1,2,3,4,5,6,7,8,9,10])


myList = gen_unsorted(7)
print(myList)
myList = bogo_sort(myList, True, lescreen)
print(myList)
input()
