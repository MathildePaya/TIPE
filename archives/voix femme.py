
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wave

###


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

###

temps = np.linspace(0,duree,n)

# création du spectre en fréquence

Ne = len(signal)
Te = temps[1]-temps[0]
spectre = 2*np.absolute(np.fft.rfft(signal))/Ne
frequences = np.arange(Ne/2 +1,)*1.0/(Te*Ne)


plt.close('all')
plt.plot(frequences,spectre)
plt.xlabel("f (Hz)")
plt.ylabel("A")
plt.title("Enregistrement de voix")
plt.xlim([-100,1000])
plt.show()




###


result = np.array(signal)
scaled = result/np.max(np.abs(result)) * 32767
wave.write("voix.wav", 44100 , scaled.astype(np.int16))

