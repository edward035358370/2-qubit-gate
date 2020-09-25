# 2 qubit gate parameter counting
'''
1.f01 had better close to 8GHz
2.mirror's length formula L=c/(4*alpha)
    c is speed of light
    alpha is Anharmonicity
3. 2 kinds of Ec, 200MHz and 340MHz
4. 2 kinds of c, 0.9x10**8 m/s and 1.2x10**8 m/s
5. 2 kinds of coupling, strong couple and weak couple
6. for avoiding the anti-crossing between transmission line
    and qubit, we have to set transmisssion line's resonance
    between f01 and f12.
7. considering the length of bounding, the mirror length must
    be more 2.5 mm

8.Avoid anti-crossing induced by cavity, the length from input
    port to qubit is lc, for capacitance mirror,
    set qubit f01 at node, f01 = (2n+1)*c/(4*L) = (2n+1)*alpha.
                           f12 = 2*n*alpha
                           lc = (4(n+k)/(4n+1) - 1)*L
9. considering the bounding line length, lc at chip may be minus
    2.5 mm.
'''

class TwoQubit():
    def __init__(self,couple):
        self.couple = couple

    def MirrorLength(self,c,alpha):
        self.c = c
        if self.couple == 'strong':
            self.alpha = alpha + 10 * 10 ** 6
        elif self.couple == 'weak':
            self.alpha = alpha
        self.result = self.c*10**3/(4*self.alpha)
        return self.c,self.alpha,self.result
    def Freq01(self):
        n = 0
        Freq = []
        frequency = 0
        while frequency < 8*10**9:
            n += 1
            frequency = (2*n+1)*self.alpha
            Freq.append(frequency)
        self.n = n-1
        self.freq = Freq[-2]
        self.SecFreq = Freq[-3]
        return self.freq,self.SecFreq,n
    def Freq12(self):
        self.freq12 = 2*self.n*self.alpha
        self.freq12sec = 2*(self.n - 1)*self.alpha
        return self.freq12,self.freq12sec
    def AvoidAnti(self,k):
        lc = (4*(self.n + k) / (4*self.n+1) - 1)*self.result
        fc = 0.5*(self.n + k)*self.c/(self.result +lc)
        return lc,fc

if __name__ == '__main__':

    Alpha = [200*10**6,340*10**6]#Hz
    LightSpeed = [0.9*10**8,1.2*10**8] #m/s
    coupling = ['weak','strong']
    for couple in coupling:
        Couple = TwoQubit(couple)
        for alpha in Alpha:
            for c in LightSpeed:
                print('--------------')
                Lcouple = Couple.MirrorLength(c, alpha)
                print('%s couple,c = %sx10^8m/s,alpha = %s MHz,length = %s mm' % (
                couple,Lcouple[0] / 10 ** 8, Lcouple[1] / 10 ** 6, Lcouple[2]))
                Freq01Couple = Couple.Freq01()
                Freq12Couple = Couple.Freq12()
                print("frequency 01 limit: %sGHz,n = %s" % (Freq01Couple[0] / 10 ** 9, Freq01Couple[2] - 1))
                print("frequency 12 limit: %sGHz,n = %s" % (Freq12Couple[0] / 10 ** 9, Freq01Couple[2] - 1))
                for k in range(1,4):
                    LcCouple = Couple.AvoidAnti(k)
                    print("k = %s,lc = %s mm,fc = %s GHz"%(k,LcCouple[0],LcCouple[1]/10**6))
                print('<=======>')
                print("frequency second: %sGHz,n = %s" % (Freq01Couple[1] / 10 ** 9, Freq01Couple[2]- 2))
                print("frequency 12 second: %sGHz,n = %s" % (Freq12Couple[1] / 10 ** 9, Freq01Couple[2] - 2))
                print('--------------')


