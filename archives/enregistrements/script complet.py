''' boucle expérience 1 '''



import scipy.io.wavfile as wave
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\Paya Mathilde\Desktop\TIPE\enregistrements')

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
        res += A[i]*np.sin(2*np.pi*L[i]*t + (dephasage/8)*np.pi)
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

rate,micro = wave.read('usine25.wav')

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
frequences = np.arange(Ne/2,)*1.0/(Te*Ne)


plt.close('all')
plt.plot(frequences,spectre[1:])
plt.xlabel("f (Hz)", fontsize = 24)
plt.ylabel("A", fontsize = 24)
plt.title("Spectre du bruit d'un ventilateur d'usine", fontsize = 24)
plt.xlim([-10,800])
plt.show()

###
# récupération des fréquences et création de l'anti-bruit

listefrequences = liste_frequences(spectre,frequences,1000)[0]
amplitudes = liste_frequences(spectre,frequences,1000)[1]

dephasage = 1
valeuramplitudesfinal = amplitudes[0]

while valeuramplitudesfinal>amplitudes[0]/2:


    contre = np.array(creationsignalcontraire(listefrequences,amplitudes,duree,dephasage)[1])


    # somme des deux signaux

    final = micro + contre


    # création du spectre en fréquence de la somme
    finalliste = []
    for i in range (n):
        finalliste.append( final[i] )
    spectrefinal = 2*np.absolute(np.fft.rfft(finalliste))/Ne
    frequencesfinal = np.arange(Ne/2,)*1.0/(Te*Ne)

    listefrequencesfinal = liste_frequences(spectrefinal,frequencesfinal,0)[0]
    amplitudesfinal = liste_frequences(spectrefinal,frequencesfinal,0)[1]

    valeuramplitudesfinal = rechercheamplitude(listefrequences[0],listefrequencesfinal,amplitudesfinal)



    dephasage += 1






plt.close('all')
plt.plot(frequencesfinal,spectrefinal)
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.title("Simulation spectre final du bruit du moteur à la fin du tube PVC")

plt.show()

































