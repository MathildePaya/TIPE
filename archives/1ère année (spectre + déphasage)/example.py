from scipy.io.wavfile import write
import numpy as np
import os

samplerate = 44100; fs = 500

t = np.linspace(0., 1., samplerate)

amplitude = np.iinfo(np.int16).max

data = amplitude * np.sin(2. * np.pi * fs * t)

write("example.wav", samplerate, data.astype(np.int16))