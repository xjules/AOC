import utils
import numpy as np
from copy import deepcopy


lines_raw = utils.read_lines_str_stripped("AOC2021/aoc20/test_input.txt")
image_filter = lines_raw[0]
image = [line for line in lines_raw[2:]]
xdim = len(image[0])
image = [c for line in image for c in line]
image = np.array(image).reshape(-1, xdim)
image_new = np.zeros(image.shape).astype(np.int32)
image_new[image == "#"] = 1
print(image_new)


class ImageFilter:
    def __init__(self, img, conv):
        self.img = img
        self.conv = conv
        self._xdim, self._ydim = img.shape

    def get_img(self, i, j):
        if i < 0 or i >= self._xdim or j < 0 or j >= self._ydim:
            return 0
        return self.img[j, i]

    def show(self):
        import matplotlib.pyplot as plt

        plt.imshow(self.img)
        plt.show()

    def do_conv_all(self):
        self._xdim, self._ydim = self.img.shape
        self.img_res = np.empty((self._ydim + 2, self._xdim + 2)).astype(self.img.dtype)
        for x in range(-1, self._xdim + 1):
            for y in range(-1, self._ydim + 1):
                self.do_conv(x, y)
        self.img = self.img_res.copy()
        # print(self.img.shape)

    def do_conv(self, i, j):
        c = ""
        dtf = {0: "0", 1: "1"}
        for y in range(j - 1, j + 2):
            for x in range(i - 1, i + 2):
                c += dtf[self.get_img(x, y)]
        num = int(c, 2)
        val = 0
        if self.conv[num] == "#":
            val = 1
        self.img_res[j + 1, i + 1] = val


def part_I():
    imf = ImageFilter(image_new, image_filter)
    print(len(imf.img[imf.img == 1]))
    imf.do_conv_all()
    print(len(imf.img[imf.img == 1]))
    imf.do_conv_all()
    print(len(imf.img[imf.img == 1]))
    imf.show()


def part_II():
    imf = ImageFilter(image_new, image_filter)
    for i in range(50):
        imf.do_conv_all()
    print(len(imf.img[imf.img == 1]))


part_I()
# part_II()
