''' TEST COMPLET 1.0 '''

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
plt.axvline(120, color = 'r')
plt.xlim([0,500])
plt.show()


### récupération des fréquences



def liste_frequences(spectre,frequences):
    L = []
    A = []

    for i in range (len(frequences)-1):

        if frequences[i] < 120 and spectre[i] > 130:
            L.append(frequences[i])
            A.append(spectre[i])

    return L,A


#test

listefrequences = liste_frequences(spectre,frequences)[0]
amplitudes = liste_frequences(spectre,frequences)[1]

### récupération des fréquences
'''

def liste_frequences(spectre,frequences):
    L = []
    A = []
    compteur = 0        #pour savoir si on monte (compteur = 0) ou on descend (compteur = 1)
    for i in range (len(frequences)-1):

        if frequences[i] < 75 and spectre[i] > 100:

            if spectre[i] > spectre[i+1] and compteur == 0:         #quand ça redescend, on a atteint un pic (donc une fréquence intéressante)
                L.append(frequences[i])
                A.append(spectre[i])
                compteur = 1

            elif spectre[i] < spectre[i+1] and compteur == 1:
                compteur = 0
    return L,A


#test

listefrequences = liste_frequences(spectre,frequences)[0]
amplitudes = liste_frequences(spectre,frequences)[1]


'''
### création du signal en opposition de phase

def fonctionsindecalee(L,A,t):
    res = 0

    '''
    for i in range (len(L)):
        res += A[i]*np.sin(2*np.pi*L[i]*t + (2/8)*2*np.pi)
    '''
    res = A[0]*np.sin(2*np.pi*L[0]*t + (5/8)*2*np.pi) + A[1]*np.sin(2*np.pi*L[1]*t + (7/8)*2*np.pi) + A[2]*np.sin(2*np.pi*L[2]*t + (2/8)*2*np.pi) + A[3]*np.sin(2*np.pi*L[3]*t + (5/8)*2*np.pi) + A[4]*np.sin(2*np.pi*L[4]*t + (5/8)*2*np.pi)

    return res


def creationsignalcontraire(liste,amplitudes,duree):
    temps = np.linspace(0,duree,n)

    res = []
    for i in range(len(temps)):
        x = signal[i] + fonctionsindecalee(liste,amplitudes,temps[i])
        res.append(x)
    return (temps,res)

signaldesortie = creationsignalcontraire(listefrequences,amplitudes,duree)

Ne = len(signal)
Te = temps[1]-temps[0]
spectre2 = 2*np.absolute(np.fft.rfft(signaldesortie[1]))/Ne
frequences2 = np.arange(Ne/2+1,)*1.0/(Te*Ne)


plt.close('all')
plt.plot(frequences,spectre,color = 'g')
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.plot(frequences2,spectre2,color = 'r')
plt.xlim([40,120])
plt.show()






###
plt.close('all')

plt.plot(temps, signaldesortie[1], color = 'brown')
plt.plot(temps, signal, color = 'g')

plt.show()


### création du fichier .wav


result = np.array(signaldesortie[1])
scaled = result/np.max(np.abs(result)) * 32767
wave.write("chantiermodifiev2.wav", 44100 , scaled.astype(np.int16))











