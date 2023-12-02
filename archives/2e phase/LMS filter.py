''' LMS filter '''

import numpy as np
import matplotlib.pyplot as plt

###


p = 34
X = np.zeros(p)
W = np.zeros(p)
f = 50
fs = 3000
mu = 0.0210

def x1(t):
    return 1*np.sin(2*np.pi*t*f/fs)

def x2(t):
    return 0.8*np.sin(2*np.pi*t*2*f/fs)

def x3(t):
    return 0.5*np.sin(2*np.pi*t*3*f/fs)

def x(t):
    return x1(t) + x2(t) + x3(t)



###

abs = np.linspace(0,100,100)
ord = [x(a) for a in abs]

plt.close('all')
plt.plot(abs,ord)
plt.show()



###

#nombre d'itérations
nb = 2000


y = np.zeros(nb)
e = np.zeros(nb)
s = np.zeros(nb)

for k in range (nb):
    #mise a jour des coeffs de X
    X[1:]=X[0:-1]
    X[0]=x(k)

    #signal contraire à émis à l'instant k
    y[k]=np.dot(X,W)
    s[k]=-y[k]

    #calcul de l'erreur
    e[k]=x(k)-y[k]

    #mise à jour de la matrice de l'équation pondérée
    W=W+mu*e[k]*X

    #LMS
    g = e**2


###

temps = [k for k in range (nb)]
T = np.array(temps)

plt.close('all')

plt.plot(T,e, color='r')

plt.show()

###

plt.close('all')

plt.plot(T,x(T),color='g',alpha=0.7)
plt.plot(T,x(T)+s,color='r')


plt.show()

###################################################################























