def plotRect(rect1,rect2):
  import matplotlib.pyplot as plt
  plt.axes()
  line00  = plt.Line2D((rect1[2], rect1[0]), (rect1[1], rect1[1]), lw=1.5)
  line01  = plt.Line2D((rect1[2], rect1[0]), (rect1[3], rect1[3]), lw=1.5)
  line02  = plt.Line2D((rect1[2], rect1[2]), (rect1[1], rect1[3]), lw=1.5)
  line03  = plt.Line2D((rect1[0], rect1[0]), (rect1[1], rect1[3]), lw=1.5)

  
  line10  = plt.Line2D((rect2[2], rect2[0]), (rect2[1], rect2[1]), lw=1.5, c="red", ls ="--")
  line11  = plt.Line2D((rect2[2], rect2[0]), (rect2[3], rect2[3]), lw=1.5, c="red", ls ="--")
  line12  = plt.Line2D((rect2[2], rect2[2]), (rect2[1], rect2[3]), lw=1.5, c="red", ls ="--")
  line13  = plt.Line2D((rect2[0], rect2[0]), (rect2[1], rect2[3]), lw=1.5, c="red", ls ="--")


  #line1 = plt.Line2D((rect1[2], rect1[0]), (1, 1), lw=1.5)
  plt.gca().add_line(line00)
  plt.gca().add_line(line01)
  plt.gca().add_line(line02)
  plt.gca().add_line(line03)
  
  plt.gca().add_line(line10)
  plt.gca().add_line(line11)
  plt.gca().add_line(line12)
  plt.gca().add_line(line13)

  plt.axis('scaled')
  plt.show()

#plotRect([0,0,4,4], [0,0,4,5])

def convertRectToCoOrdinates(rect):
  x1=rect[0]
  x2=rect[0]+rect[2]
  y1=rect[1]-rect[3]
  y2=rect[1]
  return [x1,y1,x2,y2]

rec_list=[[0,3,4,9],[2,0,6,4]]
plotRect(rec_list[0], rec_list[1])

def overlap1(rec1, rec2):
  if (rec1[2]<=rec2[0] or rec2[2]<=rec1[0]):
    return False

  if (rec1[3]<=rec2[1] or rec2[3]<=rec1[1]):
    return False
  return True

overlap1(rec_list[0],rec_list[1])

rec_list=[[0,3,4,9],[2,0,6,-6]]

plotRect(rec_list[0], rec_list[1])


def overlap2(rec1, rec2):
  if (max(rec1[0],rec2[0]) - min(rec1[2],rec2[2])>=0):
    return False

  if (max(rec1[1],rec2[1]) - min(rec1[3],rec2[3])>=0):
    return False
  return True

overlap2(rec_list[0],rec_list[1])

#rect = top left corner coordinate + w+h

#rectangle=[x,y,w,h]

rec_list=[[0,3,4,9],[2,-3,4,9]]

rect1=convertRectToCoOrdinates(rec_list[0])
rect2=convertRectToCoOrdinates(rec_list[1])
plotRect(rect1,rect2)
# same rect with  bottom left corordinate and top right coordinate

def overlap3(rec1, rec2):
  if (rec1[0]+rec1[2]<=rec2[0] or rec2[0]+rec2[2]<=rec1[0]):
    return False

  if (rec1[1]-rec1[3]>=rec2[1] or rec2[1]-rec2[3]>=rec1[1]):
    return False
  return True

overlap3(rec_list[0],rec_list[1])

