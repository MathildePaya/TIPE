''' tests TIPE '''

import numpy as np
import matplotlib.pyplot as plt

### création du signal

def f(t):
    return( 1*np.sin(2*np.pi*30*t) )            #30Hz == moteur d'une voiture

def f2(t):
    return( 5*np.sin(2*np.pi*110*t) )           #110Hz == voix d'un homme

def f3(t):
    return( 3*np.sin(2*np.pi*200*t) )           #200Hz == voix d'une femme


def f4(t):
    return( 2*np.sin(2*np.pi*35*t) )

def f5(t):
    return( 4*np.sin(2*np.pi*500*t) )

def f6(t):
    return( 4*np.sin(2*np.pi*550*t) )

def f7(t):
    return( 4*np.sin(2*np.pi*50*t) )

### récupération des données et tracé du signal

temps = np.linspace(0,10,100000)
signal = [f(t)+f2(t)+f3(t)+f4(t)+f5(t)+f6(t)+f7(t) for t in temps]

plt.close('all')
plt.plot(temps, signal, color = 'r')
plt.show()


###


Ne = len(signal)
Te = temps[1]-temps[0]
spectre = 2*np.absolute(np.fft.rfft(signal))/Ne
frequences = np.arange(Ne/2+1,)*1.0/(Te*Ne)


plt.close('all')
plt.plot(frequences,spectre)
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.axis([0,600,-0.2,5.2])
plt.axvline(75, color = 'r')
plt.show()







