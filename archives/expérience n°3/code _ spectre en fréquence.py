''' expérience n°3 : 22/10/2021 '''


import scipy.io.wavfile as wave
import os
import numpy as np
import matplotlib.pyplot as plt

#os.chdir(r'C:\Users\Paya Mathilde\Desktop\TIPE\expérience n°3')
#faire attention à être dans le bon dossier pour aller chercher le son


### traitement du signal .wav récupéré


rate,micro = wave.read('son.wav')

n = len(micro)
duree = n/rate

signal = []
for i in range (n):
    signal.append( micro[i] )

temps = np.linspace(0,duree,n)

# création du spectre en fréquence

Ne = len(signal)
Te = temps[1]-temps[0]
spectre = 2*np.absolute(np.fft.rfft(signal))/Ne
frequences = np.arange(Ne/2,)*1.0/(Te*Ne)


# affichage du spectre
plt.close('all')
plt.plot(frequences,spectre)
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.show()