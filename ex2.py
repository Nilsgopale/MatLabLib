import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave form")
plt.plot(x, y)
plt.show()