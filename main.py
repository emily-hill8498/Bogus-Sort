from random import randint
import list_visual as lv


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
listLen = 256
lescreen = lv.screen('Bogus-sort', 720/listLen)
lescreen.init_canvas(listLen)
# lescreen.visualize_list([1,2,3,4,5,6,7,8,9,10])


myList = gen_unsorted(listLen)
print(myList)
myList = bogo_sort(myList, True, lescreen)
print(myList)
input()
