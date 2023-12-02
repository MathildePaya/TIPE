''' tests TIPE '''

import numpy as np
import matplotlib.pyplot as plt

### création du signal

def f(t):
    return( 2*np.sin(2*np.pi*100*t) )

def f2(t):
    return( np.sin(2*np.pi*200*t) )

### récupération des données et tracé du signal

temps = np.linspace(0,0.04,1000)
signal = [f(t)+f2(t) for t in temps]

plt.close('all')
plt.plot(temps, signal, color = 'r')
plt.show()

### création du spectre en fréquence

#Ne est le nombre d'échantillons, Te le pas d'échantillonnage

Ne = len(signal)
Te = temps[1]-temps[0]
spectre = 2*np.absolute(np.fft.rfft(signal))/Ne
frequences = np.arange(Ne/2+1,)*1.0/(Te*Ne)
plt.close('all')
plt.plot(frequences,spectre)
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.show()

### on zoom sur la partie intéressante

plt.close('all')
plt.plot(frequences,spectre)
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.axis([0,1000,-0.2,2.2])
plt.show()