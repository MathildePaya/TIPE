''' RTSP 05/12/2021 '''


import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

###
import time

###

def max(liste):

    max = liste[0]

    for l in liste :
        if l >= max:
            max = l

    return max

###

def frequence(frequences,spectre):

    res = []

    maximum = max(spectre)

    for i in range(len(frequences)):

        if spectre[i]>=(maximum/2):
            res.append(frequences[i])

    return res


###

#enregistrer le son et faire son spectre en fréquence

enregistrement = sd.rec(6*44100,44100,channels = 1)

sd.wait()
#

#t0 = time.time()

rate = 44100

n = len(enregistrement)
duree = n/rate

signal = []
for i in range (n):
    signal.append( enregistrement[i][0] )

temps = np.linspace(0,duree,n)

# création du spectre en fréquence

Ne = len(signal)
Te = temps[1]-temps[0]
spectre = 2*np.absolute(np.fft.rfft(signal))/Ne
frequences = np.arange(Ne/2 +1,)*1.0/(Te*Ne)


# plt.close('all')
# plt.plot(frequences,spectre)
# plt.xlabel("f (Hz)")
# plt.ylabel("A")
# plt.title("Enregistrement du bruit")
# plt.xlim([-100,1000])
# plt.show()
#

#

sinusoide = frequence(frequences,spectre)

f = np.round(sinusoide[0])

#t1 = time.time()

listetemps = np.arange(0,30,1/44100)

fonctionsin = -np.sin(2*np.pi*f*listetemps)

#t2 = time.time()

#contre = (-1)*bruit
# une fois qu'on connait la fréquence, on enregistre une durée correspondant à un nombre rond de périodes, on inverse
# le signal, puis on balance le contre bruit
#
# periode = 1/f
#
# bruit = sd.rec(int(np.round(periode*1000))*44100,44100,channels = 1)
#
# sd.wait()

#time.sleep(abs(1/f - (t2-t0)))


sd.play(fonctionsin,44100)





















