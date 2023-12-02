''' REAL TIME SOUND PROCESSING '''
# https://python-sounddevice.readthedocs.io/en/0.2.2/

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

###

def loop(fichier,dureedufichier,limite):

    compteur = 0
    duree = 0

    while duree < limite :
        sd.play(fichier)
        sd.wait()
        compteur+=1
        duree = dureedufichier*compteur

def fonction():

    dureeduson = 1  #must be int
    son = sd.rec(dureeduson*44100,44100,channels = 1)
    sd.wait()

    contre = -1*son

    loop(contre,dureeduson,30)

###

fonction()


### exemple

temps = np.linspace(0,1,1000)
base = np.array([np.sin(2*np.pi*50*t) for t in temps])
contre = np.array([-np.sin(2*np.pi*50*t) for t in temps])
final = base + contre

plt.close('all')

plt.subplot(3,1,1)
plt.plot(temps, base)
plt.ylabel("A")
plt.title("Enregistrement du signal")

plt.subplot(3,1,2)
plt.plot(temps, contre)
plt.ylabel("A")
plt.title("Signal contre")

plt.subplot(3,1,3)
plt.plot(temps, final)
plt.ylabel("A")
plt.title("Signal de sortie")

plt.xlabel("Temps")

plt.show()





