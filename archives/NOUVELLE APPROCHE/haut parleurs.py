''' expérience haut parleurs '''

import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

###

temps = np.linspace(0,30,1323000) #fréquence d'échantillonnage = 44100
fonction = [np.sin(2*np.pi*1000*t) for t in temps]  #création de la sinusoïde
son = np.array(fonction)

sd.play(son,44100)





