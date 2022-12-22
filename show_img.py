import numpy as np
import matplotlib.pyplot as plt
# lines = np.loadtxt("out.txt")
# for i in range(1000):
#     pic = lines[i].reshape(16, 51)
#     pic = np.flip(pic, axis=0)
#     plt.imshow(pic, 'gray')
#     plt.savefig("./pic/{}.PNG".format(i))
import PIL
image=[]
for i in range(1000):
    new=PIL.Image.open('./pic/{}.PNG'.format(i))
    image.append(new)
image[0].save('cs.gif',format='GIF',
    append_images=image[1: ],
    save_all=True,duration=0.002,
    loop=0
)