''' si tout se passait bien '''


import scipy.io.wavfile as wave
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\Paya Mathilde\Documents\MPSI\TIPE')
###

#faire attention à être dans le bon répertoire : os.getcwd() pour vérifier, os.chdir(r'C:\Users\Paya Mathilde\Documents\MPSI\TIPE') pour le changer

rate,data = wave.read('chantier.wav')

n = len(data)
duree = n/rate

signal = []
for i in range (n):
    signal.append( data[i] )

temps = np.linspace(0,duree,n)

''' CONCLUSION : on a les listes SIGNAL et TEMPS qui définissent le signal '''
plt.close('all')
plt.plot(temps,signal)
plt.xlabel("temps (s)")
plt.ylabel("A")
plt.show()



### création du spectre en fréquence

#Ne est le nombre d'échantillons, Te le pas d'échantillonnage

Ne = len(signal)
Te = temps[1]-temps[0]
spectre = 2*np.absolute(np.fft.rfft(signal))/Ne
frequences = np.arange(Ne/2+1,)*1.0/(Te*Ne)

''' OPTIONNEL : montrer le spectre '''
plt.close('all')
plt.plot(frequences,spectre)
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.axvline(75, color = 'r')
plt.xlim([0,1500])
plt.show()


### récupération des données



def liste_frequences(spectre,frequences):
    L = []
    A = []

    for i in range (len(frequences)-1):

        if frequences[i] > 75 and spectre[i] > 100:
            L.append(frequences[i])
            A.append(spectre[i])

    return L,A

frequences2 = liste_frequences(spectre,frequences)[0]
spectre2 = liste_frequences(spectre,frequences)[1]

''' OPTIONNEL : montrer le spectre '''
plt.close('all')
plt.plot(frequences2,spectre2)
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.axvline(75, color = 'r')
plt.xlim([0,1500])
plt.show()


### création du signal de sortie

def sommefonctionssin(L,A,t):
    res = 0

    for i in range (len(L)):
        res += A[i]*np.sin(2*np.pi*L[i]*t)
    return res


def signalfinal(frequences,amplitudes):

    res = []

    for i in range(len(temps)):
        x = sommefonctionssin(frequences,amplitudes,temps[i])
        res.append(x)
    return res

signaldesortie = signalfinal(frequences2,spectre2)

''' OPTIONNEL : montrer le signal '''
plt.close('all')
plt.plot(temps,signaldesortie)
plt.xlabel("temps (s)")
plt.ylabel("A")
plt.show()


### création du fichier .wav

result = np.array(signaldesortie)
scaled = result/np.max(np.abs(result)) * 32767
wave.write("sitoutallaitbien.wav", 44100 , scaled.astype(np.int16))


















