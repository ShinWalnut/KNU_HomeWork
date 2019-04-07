import cv2 as cv
import numpy as np
import time as t

files = ['lena.jpg', 'cat.jpg', 'flower.jpg']
save_img = []

def _error(pixel):
    if pixel > 127:
        return pixel - 255
    else:
        return pixel
    
    
def Err_Dif_Dithering(img):
    new_img = np.zeros(img.shape, dtype=np.uint8)
    width, height = img.shape[0:2]
    
    for y in range(height-1):
        for x in range(1, width-1):
            err = _error(img[x,y])
            if img[x,y] < 128:
                new_img[x,y]=0
            else:
                new_img[x,y]=255
            img[x+1,y] += 7*err/16
            img[x-1,y+1] += 3*err/16
            img[x,y+1] += 5*err/16
            img[x+1,y+1] += err/16
    return new_img

               
start = t.time()


for file in files:
    img = cv.imread(file)
    save_img.append(img)

    print(file, "의 size : ", img.shape)
    print(img.dtype)
    
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    save_img.append(img)
    print(img.dtype)
    
    img = Err_Dif_Dithering(img)
    save_img.append(img)
    print(img.dtype)

end = t.time()

for i in range(9):
    cv.imshow("title", save_img[i])
    cv.waitKey(0)
    cv.destroyAllWindows()

print("소요시간 : ", end - start)







    
