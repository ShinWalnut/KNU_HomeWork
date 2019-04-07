import cv2 as cv
import numpy as np
import time as t
import copy

files = ['lena.jpg', 'cat.jpg', 'flower.jpg']
save_img = []


def Err_Dif_Dithering(_img):
    copy_img = copy.deepcopy(_img)
    new_img = np.zeros(shape=img.shape, dtype=np.uint8)
    width, height = copy_img.shape[0:2]
    
    for y in range(height-1):
        for x in range(1, width-1):
            if copy_img[x,y] <128:
                new_img[x,y] = 0
                err = copy_img[x,y]
            else:
                new_img[x,y] = 255
                err = copy_img[x,y] - 255
            copy_img[x+1,y] += 7*err/16
            copy_img[x-1,y+1] += 3*err/16
            copy_img[x,y+1] += 5*err/16
            copy_img[x+1,y+1] += err/16
    return new_img

               
start = t.time()


for file in files:
    img = cv.imread(file)
    save_img.append(img)
    print(file, "의 size : ", img.shape)
    
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    save_img.append(img)
    
    img = Err_Dif_Dithering(img)
    save_img.append(img)

end = t.time()

for i in range(9):
    cv.imwrite(str(i)+'.jpg',save_img[i])
    #cv.imshow(str(i), save_img[i])
    #cv.waitKey(0)
    #cv.destroyAllWindows()

print("소요시간 : ", end - start)







    
