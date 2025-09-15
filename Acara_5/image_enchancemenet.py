# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('Acara_5/img/daun.jpeg')
# plt.hist(img.ravel(), 256, [0,256]);
# plt.savefig('Acara_5/img/output/CitraHist.jpeg')

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Acara_5/img/daun.jpeg')

hist = cv2.calcHist([img], [0], None, [256], [0, 256]) \
     + cv2.calcHist([img], [1], None, [256], [0, 256]) \
     + cv2.calcHist([img], [2], None, [256], [0, 256])

plt.plot(hist)
plt.xlim([0, 256])
plt.savefig('Acara_5/img/output/CitraHist2.jpeg')