import numpy as np
import matplotlib.pyplot as plt
#if using termux
import subprocess
import shlex
#end if
# import os
# os.system('Xvfb :1 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8
# os.environ['DISPLAY']=':1.0'    # tell X clients to use our virtual DISPLAY :1.0.

#DTFT
def H(z):
	num = np.polyval([1,0,1],z**(-1))
	den = np.polyval([0.5,1],z**(-1))
	H = num/den
	return H
		


#Input and Output
omega = np.linspace(int(-3*np.pi),int(3*np.pi),int(1e2))

#subplots
plt.plot(omega, abs(H(np.exp(1j*omega))))
plt.title('Filter Frequency Response')
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})| $')
plt.grid()# minor

#if using termux
# plt.savefig('../figs/dtft.pdf')
# plt.savefig('../figs/dtft.png')
# subprocess.run(shlex.split("termux-open ../figs/dtft.pdf"))
#else
plt.show()





