''' tests TIPE '''

import numpy as np
import matplotlib.pyplot as plt

### création du signal

def f2(t):
    return( 5*np.sin(2*np.pi*110*t) )           #110Hz == voix d'un homme


def f1(t):
    return( 2*np.sin(2*np.pi*50*t + 0.5) )


### récupération des données et tracé du signal

temps = np.linspace(0,0.2,1000)
signal = [f1(t)+f2(t) for t in temps]

plt.close('all')
plt.plot(temps, signal, color = 'r')
plt.xlabel('temps (s)')
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
plt.title('Spectre signal source')
plt.show()

### récupération des fréquences

def liste_frequences(spectre,frequences):
    L = []
    A = []
    compteur = 0        #pour savoir si on monte (compteur = 0) ou on descend (compteur = 1)
    for i in range (len(frequences)-1):

        if spectre[i] > spectre[i+1] and compteur == 0:         #quand ça redescend, on a atteint un pic
            L.append(frequences[i])
            A.append(spectre[i])
            compteur = 1

        elif spectre[i] < spectre[i+1] and compteur == 1:
            compteur = 0
    return L,A



listefrequences = liste_frequences(spectre,frequences)[0]
listeamplitudes = liste_frequences(spectre,frequences)[1]

### sélection des fréquences à atténuer

bufferfreq = []
bufferampli = []

for k in range (len(listefrequences)):
    if listefrequences[k] <= 75:
        bufferfreq.append(listefrequences[k])
        bufferampli.append(listeamplitudes[k])

listefrequences,listeamplitudes = bufferfreq, bufferampli





### création du signal en opposition de phase

##fonctions

# retourne f(t) avec f la somme des fonctions sinus modulées en amplitude
def fonctionsindecalee(L,A,t,dephasage):
    res = 0

    for i in range (len(L)):
        res += A[i]*np.sin(2*np.pi*L[i]*t + (dephasage[i]/10)*np.pi)
    return res

# création du signal complet de l'anti-bruit
def creationsignalcontraire(liste,amplitudes,dephasage):

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


##

dephasage = [1 for i in range(len(listefrequences))]

for i in range (len(listefrequences)):
    valeuramplitude = listeamplitudes[i]

    while valeuramplitude>listeamplitudes[i]/2:

        contre = np.array(creationsignalcontraire(listefrequences,listeamplitudes,dephasage)[1])

        # somme des deux signaux

        final = signal + contre

        # transformation en une liste
        finalliste = []
        for k in range (len(temps)):
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
plt.title("Simulation spectre final")
plt.show()












