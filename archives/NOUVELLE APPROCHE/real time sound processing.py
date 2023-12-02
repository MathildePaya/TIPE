''' REAL TIME SOUND PROCESSING '''
# https://python-sounddevice.readthedocs.io/en/0.2.2/

import sounddevice as sd
import scipy.io.wavfile as wave
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\Paya Mathilde\Desktop\TIPE\enregistrements\script complet résultats')

###

rate,micro = wave.read('ventilateur _ tapis.wav')

###


sd.play(micro,44100)

###

myrecording = sd.rec(4 * 44100, 44100, channels=1)




###

sd.play(myrecording)


###


temps = np.linspace(0,4,len(myrecording))


plt.close('all')
plt.plot(temps,myrecording)
plt.xlabel("Temps")
plt.ylabel("A")
plt.title("Enregistrement du bruit")
plt.show()

###

myrecording2 = sd.rec(4 * 44100, 44100, channels=1)



###

sd.play(myrecording+myrecording2)

### loop

compteur = 0
duree = 0

while duree < 10 :
    sd.play(myrecording)
    sd.wait()
    compteur+=1
    duree = 4*compteur

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

top = fonction()
























