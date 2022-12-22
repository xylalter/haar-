import numpy as np
import pywt
import matplotlib.pyplot as plt
def reshape(line):
    for i in range(len(line)):
        line[i] = eval(line[i])
    pic = np.array(line).reshape(16, 51)
    return pic
    
f = open("data.txt", "r", encoding="utf8")
line = f.readline()[:-1].split(" ")
pic = np.flip(reshape(line), axis=0)
coeffs = pywt.dwt2(pic, "haar")
cA, (cH, cV, cD) = coeffs
 
plt.subplot(221), plt.imshow(cA, 'gray'), plt.title("A")
plt.subplot(222), plt.imshow(cH, 'gray'), plt.title("H")
plt.subplot(223), plt.imshow(cV, 'gray'), plt.title("V")
plt.subplot(224), plt.imshow(cD, 'gray'), plt.title("D")

# AH = np.concatenate([cA, cH], axis=1)
# VD = np.concatenate([cV, cD], axis=1)
# img = np.concatenate([AH, VD], axis=0)
# plt.imshow(img,'gray')
# plt.title('result')
# plt.show()
plt.savefig("haar.PNG")