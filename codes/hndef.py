import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if
import os
os.system('Xvfb :1 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8
os.environ['DISPLAY']=':1.0'    # tell X clients to use our virtual DISPLAY :1.0.

k = 12
h = np.zeros(k)
h[0] = 1
h[1] = -0.5*h[0]
h[2] = -0.5*h[1] + 1

for n in range(3,k-1):
		h[n] = -0.5*h[n-1]

#subplots
plt.stem(range(0,k),h)
plt.title('Impulse Response Definition')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/hndef.pdf')
plt.savefig('../figs/hndef.png')
subprocess.run(shlex.split("termux-open ../figs/hndef.pdf"))
#else
#plt.show()
