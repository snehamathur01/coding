import cv2
#start camera
cap=cv2.VideoCapture(0)

tp1=cap.read()[1] #take 1
tp2=cap.read()[1] #take 2
tp3=cap.read()[1] #take 3

#to make it more perfect
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)  #converting into gray
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)  #converting into gray
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)  #converting into gray

#now creating image differentiator 
def img_diff(x,y,z):
     #difference between x,y --gray1,gray2  --d1
     d1=cv2.absdiff(x,y)
     #difference between y,z --gray2,gray3  --d2
     #absolute difference d1-d2
     d1=cv2.absdiff(y,z)
