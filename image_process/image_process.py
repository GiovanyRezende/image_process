import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class image():

  def __init__(self,path):
    self.path = np.array(Image.open(path))

  def show_image(self):
    plt.imshow(self.path)

  def show_array(self):
    print(self.path)

  def invert(self):
    plt.imshow(np.flip(self.path))

  def filter(self, color, filter):
        colors = {'r': 0, 'g': 1, 'b': 2}

        if isinstance(color, str):
            color = [color]
        if not isinstance(color, list):
            raise ValueError("The color must be a string or a list")

        if isinstance(filter, int):
            filtro = [filter] * len(color)
        elif isinstance(filter, list) and len(filter) != len(color):
            raise ValueError("The filter list must have the same length than colors list")

        if not all(c in colors for c in color):
            raise ValueError("The color must be in ['r', 'g', 'b']")

        for c, f in zip(color, filter):
            index = colors[c]
            self.path[:, :, index] = np.clip(self.path[:, :, index] + f, 0, 255)

        self.show_image()

  def weak(self):
    plt.imshow(np.where(self.path == 255, 50, self.path - 10))