'LMS filter sur un bruit de ventilateur'


import scipy.io.wavfile as wave
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r'C:\Users\Paya Mathilde\Desktop\TIPE\enregistrements')

###


p = 34
X = np.zeros(p)
W = np.zeros(p)


###


rate,data = wave.read('ventilateur _ tapis.wav')

n = len(data)
duree = n/rate

signal = []
for i in range (n):
    signal.append( data[i] )

temps = np.linspace(0,duree,n)

plt.close('all')
plt.plot(temps,signal)
plt.xlabel("temps (s)")
plt.ylabel("A")
plt.show()

###

length = n

y = np.zeros(length)
e = np.zeros(length)
s = np.zeros(length)

mulim = 0.5
mu = mulim

for k in range (length):
    #mise a jour des coeffs de X
    X[1:]=X[0:-1]
    X[0]=signal[k]

    #signal contraire à émis à l'instant k
    y[k]=np.dot(X,W)
    s[k]=-y[k]

    #calcul de l'erreur
    e[k]=signal[k]-y[k]

    #mise à jour du coefficient mu
    if np.dot(X,X)!=0:
        mu = mulim / np.dot(X,X)

    #mise à jour de la matrice de l'équation pondérée
    W=W+mu*e[k]*X


###

plt.close('all')

plt.plot(temps[:length],e, color='r',label='bruit résiduel')
plt.plot(temps,signal,color='g',alpha=0.5,label='signal originel')
plt.legend(fontsize = 20)


plt.show()







