import numpy as np
from scipy import signal
x = np.linspace(0, 10, 20, endpoint=False)
y = np.cos(-x**2/6.0)
f = signal.resample(y, 100)
xnew = np.linspace(0, 10, 400, endpoint=False)
import matplotlib.pyplot as plt
plt.plot(x, y, 'go-', xnew, f, '.-', 10, y[0], 'ro')
plt.legend(['data', 'resampled'], loc='best')
plt.show()

def getTheYCoordinates(newX,signalX,signalY):
    print('------------------------------')
    y = []
    for x_coordinate in newX:
        for index in range(0,len(signalX)):
            if x_coordinate < signalX[index]:
                previousXIndex = index-1
                followingXIndex = index
                break
        followingX = signalX[followingXIndex]
        previousX = signalX[previousXIndex]
        followingY = signalY[followingXIndex]
        previousY = signalY[previousXIndex]
        newYCoordinate = (x_coordinate-followingX)*(previousY - followingY)/(previousX - followingX)+(followingY)
        y.append(newYCoordinate)
    
    return y        

import numpy as np
import matplotlib.pyplot as plt
f1=300
fs=800
t_min =0
t_max= 10/f1
t= np.arange(t_min,t_max,.00001)
x1=np.sin(2*np.pi*f1*t)
Ts= 1/fs
ts = np.arange(t_min,t_max,Ts)
x1resampled=np.sin(2*np.pi*f1*ts)
x1reconstructed=np.zeros(len(t))
samples = len(ts)
for i in range(1,len(t)):
    for n in range(1,samples):
        x1reconstructed[i]=x1reconstructed[i]+x1resampled[n]*np.sinc((t[i]-n*Ts)/Ts);
plt.subplot(3,1,1)
plt.plot(t,x1)

plt.subplot(3,1,2)
plt.scatter(ts,x1resampled)


plt.subplot(3,1,3)
plt.plot(t,x1reconstructed)
plt.show()



#noise=0.0002*np.asarray(random.sample(range(0,3000),3000))
# interpolatedSignalAxis.plot(discreteTime, signalAfterSampling, 'ro-', reconstructionTimeAxis, signalAfterReconstruction, '.-')
