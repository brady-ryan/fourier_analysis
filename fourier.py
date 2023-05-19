from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

N = 10000
T = 1./20000.

class Fourier:

    def __init__(self,x,func,N,T,title):

        self.x = x
        self.func = func
        self.N = N
        self.T = T
        self.title = title

    def plot(self):

        xf = fftfreq(self.N,self.T)
        yf = fft(self.func)

        fig, ax = plt.subplots(2)


        ax[0].plot(self.x[:self.N//10],self.func[:self.N//10])
        ax[0].set_xlabel('Time (s)')
        ax[0].set_ylabel('Amplitude')
        ax[0].set_title(self.title)

        ax[1].plot(xf[:self.N//10],2./N * np.abs(yf[:N//10]))
        ax[1].set_xlabel('Frequency (Hz)')
        ax[1].set_ylabel('Power')
        ax[1].set_title('Fourier Transform')

        plt.tight_layout()
        plt.show()

    
def sine(x):
    return np.sin(100.*2.*np.pi*x)

def cosine(x):
    return np.cos(500.*2.*np.pi*x)


x = np.linspace(0.,N*T,N,endpoint=False)

sine_test = Fourier(x,sine(x),N,T,'100 Hz Sine Wave')
cosine_test = Fourier(x,cosine(x),N,T,'500Hz Cosine Wave')

funcs = [sine_test,cosine_test]

for f in funcs:
    f.plot()
