'''
for transmission impedance, arc length is better
bigger than line width 3 times.
'''
import numpy as np

ArcLength = 624.635 #micrometer

print('radius:',ArcLength/2*np.pi)
lc = 13698.6986
#X scale
XTransmon = 154.5214 #micrometer
XGateToSide = 9975.5130  #micrometer
Electrode = 50 #micrometer
bonding = 2500

#Y scale
HalfYEle = 940/2
YEleToSide = 5219.3152
YTransmon = 1225.8026

Radius = (121.8038 + 111.1038 + 94.4038 + 83.73080)/4 #micrometer
LineWidth = 16.7 #micrometer

TotalX = XTransmon + XGateToSide - Electrode
TotalY = YEleToSide - HalfYEle - Electrode - LineWidth / 2

Theta = np.linspace(0.01,89.99,360)
for theta in Theta:
    rad = theta * np.pi / 180
    ArcLen = Radius * theta / 360

    TotalX = XTransmon + XGateToSide - Electrode - 2*Radius*np.sin(rad)
    TotalY = YEleToSide - HalfYEle - Electrode - LineWidth / 2 - 2*(Radius - Radius*np.cos(rad))
    Total = TotalX + TotalY



    Totaltemp = Total - 2*ArcLen
    middle = TotalY/np.sin(rad)
    Xtemp = TotalX - middle*np.cos(rad)
    '''
    if totalize ArcLen, middle,and Xtemps is close enough
    to lc (that means between them is 10**-6), output the
    result theta and lc we will use in autocad

    '''
    if abs(2*ArcLen + middle + Xtemp - lc + bonding) <= 5:
        print(theta,'------------------')
        print('TotalX:',TotalX,'micrometer')
        print('TotalY:',TotalY,'micrometer')
        print('lc:',lc - bonding,'micrometer')
        print('ArcLen:',ArcLen,'micrometer')
        print('middle:',middle,'micrometer')
        print('X:',Xtemp,'micrometer')
        print('total:',2*ArcLen + middle + Xtemp,'micrometer')
        print('------------------')