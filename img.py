from PIL import Image
import numpy as np
import sys


# --------- Note ---------
# This converter supports different image formats (png, bmp, jpg...)
# --------- Input ---------
# python3 img.py input_image_file
# --------- Output ---------
# img: .word image_height image_width pixel[0][0] pixel[0][1] ...


if len(sys.argv) != 2:
    exit()
im = Image.open(sys.argv[1])
p = np.array(im)
print("img: .word", im.size[1], im.size[0], end = "")
flag = True
for l in p:
    for i in l:
        if flag:
            flag = False
        else:
            print(",", end = "")
        print(" 0x" + '{:08x}'.format(i[2] + i[1] * 16**2 + i[0] * 16**4),
              end = "")
print("")
