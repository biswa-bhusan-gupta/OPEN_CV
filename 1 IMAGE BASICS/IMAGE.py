import cv2

Image=cv2.imread('Cat or Dog.jpg')

while True:
    
   cv2.imshow('Kitten',Image)

   # We have waited 1 Millisecond and we have pressed the Esc 
   if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()