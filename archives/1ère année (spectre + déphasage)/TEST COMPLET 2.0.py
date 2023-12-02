''' TEST COMPLET 2.0 '''


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
plt.xlim([0,75])
plt.show()


### récupération des fréquences



def liste_frequences(spectre,frequences):
    L = []
    A = []

    for i in range (len(frequences)-1):

        if frequences[i] < 75 and spectre[i] > 125 and frequences[i] < 500:
            L.append(frequences[i])
            A.append(spectre[i])

    return L,A


#test

listefrequences = liste_frequences(spectre,frequences)[0]
amplitudes = liste_frequences(spectre,frequences)[1]



### création du signal en opposition de phase

def fonctionsindecalee(L,A,t):
    res = 0

    for i in range (len(L)):
        res += A[i]*np.sin(2*np.pi*L[i]*t + np.pi)
    return res


def creationsignalcontraire(liste,amplitudes,duree):
    temps = np.linspace(0,duree,n)

    res = []
    for i in range(len(temps)):
        x = signal[i] + fonctionsindecalee(liste,amplitudes,temps[i])
        res.append(x)
    return (temps,res)

signaldesortie = creationsignalcontraire(listefrequences,amplitudes,duree)


plt.close('all')

plt.plot(temps, signaldesortie[1], color = 'brown')
plt.plot(temps, signal, color = 'g')

plt.show()



# principe : tester pour chaque fréquence quel déphasage permet une atténuation maximale
# problème : complexité trop élevée ?





























