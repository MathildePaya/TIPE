''' boucle expérience 1 '''

import scipy.io.wavfile as wave
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\Paya Mathilde\Desktop\TIPE\enregistrements\script complet résultats')

### définition des fonctions

# retourne la liste des fréquences et de leurs amplitudes à partir du spectre en fréquences
def liste_frequences(spectre,frequences, borne):
    L = []
    A = []

    for i in range (len(frequences)-1):

        if spectre[i] > borne:
            L.append(frequences[i])
            A.append(spectre[i])

    return L,A

# retourne f(t) avec f la somme des fonctions sinus modulées en amplitude
def fonctionsindecalee(L,A,t,dephasage):
    res = 0

    for i in range (len(L)):
        res += A[i]*np.sin(2*np.pi*L[i]*t + (dephasage[i]/10)*np.pi)
    return res

# création du signal complet de l'anti-bruit
def creationsignalcontraire(liste,amplitudes,duree,dephasage):
    temps = np.linspace(0,duree,n)

    res = []
    for i in range(len(temps)):
        x = fonctionsindecalee(liste,amplitudes,temps[i],dephasage)
        res.append(x)
    return (temps,res)

def rechercheamplitude(valeurfrequence,frequences,amplitudes):
    indice = 0

    while frequences[indice]!=valeurfrequence:
        indice += 1

    return amplitudes[indice]

### traitement du signal .wav récupéré

#faire attention à être dans le bon répertoire : os.getcwd() pour vérifier, os.chdir(r'C:\Users\Paya Mathilde\Documents\MPSI\TIPE') pour le changer

rate,micro = wave.read('chantierdebase.wav')

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
frequences = np.arange(Ne/2+1,)*1.0/(Te*Ne)

plt.close('all')
plt.plot(frequences,spectre)
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.title("Enregistrement du bruit de chantier")
plt.xlim([-100,2000])
plt.ylim([-50,2000])
plt.show()

###
# récupération des fréquences et création de l'anti-bruit

listefrequences = liste_frequences(spectre,frequences,1750)[0]
listeamplitudes = liste_frequences(spectre,frequences,1750)[1]

###

dephasage = [1]
#[1 for i in range (len(listefrequences))]

for i in range (len(listefrequences)):
    valeuramplitude = listeamplitudes[i]

    while valeuramplitude>listeamplitudes[i]/2:

        contre = np.array(creationsignalcontraire(listefrequences,listeamplitudes,duree,dephasage)[1])

        # somme des deux signaux

        final = micro + contre

        # transformation en une liste
        finalliste = []
        for k in range (n):
            finalliste.append( final[k] )

        # création du spectre en fréquence de la somme
        spectrefinal = 2*np.absolute(np.fft.rfft(finalliste))/Ne

        valeuramplitude = rechercheamplitude(listefrequences[i],frequences,spectrefinal)

        dephasage[i] += 1

###

plt.close('all')
plt.plot(frequences,spectrefinal)
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.title("Simulation spectre final du bruit de chantier")
plt.xlim([-100,2000])
plt.ylim([-50,2000])
plt.show()

### création du fichier .wav


result = np.array(finalliste)
scaled = result/np.max(np.abs(result)) * 32767
wave.write("chantierpluscontre.wav", 44100 , scaled.astype(np.int16))




