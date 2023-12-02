''' tests TIPE '''


import scipy.io.wavfile as wave
import os
import numpy as np
import matplotlib.pyplot as plt

###

#faire attention à être dans le bon répertoire : os.getcwd() pour vérifier, os.chdir(r'C:\Users\Paya Mathilde\Documents\MPSI\TIPE') pour le changer

rate,data = wave.read('testcomplete.wav')

n = len(data)
duree = n/rate

signal = []
for i in range (n):
    signal.append( data[i,0] )


temps = np.linspace(0,duree,n)
plt.close('all')
plt.plot(temps,signal)
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