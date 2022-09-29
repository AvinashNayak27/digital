import numpy as np
import matplotlib.pyplot as plt

X = np.loadtxt('codes/fft.dat', dtype=float)
plt.stem(X)
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.title('$8$-point FFT')
plt.grid()
plt.savefig('./figs/xk8pointFFT.png')
plt.show()
