import matplotlib.pyplot as plt
import numpy as np

###

T = np.linspace(0,0.05,1000)
Y1 = [np.sin(2*np.pi*50*t) for t in T]
Y2 = [np.sin(2*np.pi*50*t + np.pi) for t in T]
Y3 = [ Y1[i] + Y2[i] for i in range (len(T))]

plt.close('all')
plt.subplot(2,1,1)
plt.plot(T,Y1, 'r', label = 'fonction sin')
plt.plot(T,Y2, 'g', label = 'fonction sin déphasée')
plt.plot(T,Y3, label = 'somme')
plt.axis([0,0.05,-1,1])
plt.legend()
plt.xlabel('temps (s)')
plt.show()