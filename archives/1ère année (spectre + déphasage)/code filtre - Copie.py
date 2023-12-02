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
    return( 2*np.sin(2*np.pi*50*t) )

def f5(t):
    return( 4*np.sin(2*np.pi*60*t) )

### récupération des données et tracé du signal

temps = np.linspace(0,0.2,1000)
signal = [f(t)+f2(t)+f3(t)+f4(t)+f5(t) for t in temps]

plt.close('all')
plt.plot(temps, signal, color = 'r')
plt.xlabel('temps (s)', fontsize = 20)
plt.show()

### création du spectre en fréquence

#Ne est le nombre d'échantillons, Te le pas d'échantillonnage

Ne = len(signal)
Te = temps[1]-temps[0]
spectre = 2*np.absolute(np.fft.rfft(signal))/Ne
frequences = np.arange(Ne/2+1,)*1.0/(Te*Ne)


plt.close('all')
plt.plot(frequences,spectre)
plt.xlabel("f (Hz)", fontsize = 20)
plt.ylabel("A", fontsize = 20)
plt.show()

### on zoom sur la partie intéressante

plt.close('all')
plt.plot(frequences,spectre)
plt.xlabel("f (Hz)", fontsize = 20)
plt.ylabel("A", fontsize = 20)
plt.axis([0,500,-0.2,5.2])
plt.axvline(75, color = 'r')
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



liste = liste_frequences(spectre,frequences)[0]
amplitudes = liste_frequences(spectre,frequences)[1]


### création du signal en opposition de phase

def fonctionsindecalee(L,A,t):
    res = 0

    for i in range (len(L)):
        res += A[i]*np.sin(2*np.pi*L[i]*t + np.pi)
    return res


def creationsignalcontraire(liste,amplitudes,duree):
    L=[]
    for i in range (len(liste)):
        if liste[i]<75:
            L.append(liste[i])
    temps = np.linspace(0,duree,1000)
    signaldesortie = [fonctionsindecalee(L,amplitudes,t) + f(t)+f2(t)+f3(t)+f4(t)+f5(t) for t in temps]
    return (temps,signaldesortie)

temps = np.linspace(0,0.2,1000)
signalobjectif = [f2(t)+f3(t) for t in temps]
signaldesortie = creationsignalcontraire(liste,amplitudes,0.2)


plt.close('all')
plt.plot(temps, signalobjectif, color = 'g', label = 'signal résultant théorique')
plt.plot(signaldesortie[0], signaldesortie[1], color = 'violet', label = 'signal résultant')
plt.legend(fontsize = 20)
plt.xlabel('temps (s)', fontsize = 24)
plt.ylabel('amplitude', fontsize = 24)
plt.show()


###


Ne = len(signaldesortie[1])
Te = temps[1]-temps[0]
spectre = 2*np.absolute(np.fft.rfft(signaldesortie[1]))/Ne
frequences = np.arange(Ne/2+1,)*1.0/(Te*Ne)
plt.close('all')
plt.plot(frequences,spectre)
plt.title('Spectre du signal résultant')
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.show()
















