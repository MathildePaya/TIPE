''' boucle expérience 1 '''

import scipy.io.wavfile as wave
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\Paya Mathilde\Desktop\TIPE\expérience ALI')

### traitement du signal .wav récupéré

#faire attention à être dans le bon répertoire : os.getcwd() pour vérifier, os.chdir(r'C:\Users\Paya Mathilde\Documents\MPSI\TIPE') pour le changer

rate,micro = wave.read('cab_oreille.wav')

n = len(micro)
duree = n/rate

signal = []
for i in range (n):
    signal.append( micro[i][0] )

temps = np.linspace(0,duree,n)

# création du spectre en fréquence

Ne = len(signal)
Te = temps[1]-temps[0]
spectre = 2*np.absolute(np.fft.rfft(signal))/Ne
frequences = np.arange(Ne/2+1,)*1.0/(Te*Ne)

plt.close('all')
plt.plot(frequences,spectre)
plt.xlabel("f (Hz)", fontsize = 24)
plt.ylabel("A", fontsize = 24)
plt.title("Enregistrement du signal avec CAB", fontsize = 24)
plt.xlim([0,2500])
plt.ylim([0,1800])
plt.show()