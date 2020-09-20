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
    set qubit f01 at node, f01 = (2n-1)*c/(4*L) = (2n-1)*alpha.
                           f12 = 2*(n-1)*alpha
                           lc = (4(n+k)/(4n-3) - 1)*L
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
            frequency = (2*n-1)*self.alpha
            Freq.append(frequency)
        self.n = n-1
        freq = Freq[-2]
        SecFreq = Freq[-3]
        return freq,SecFreq,n
    def Freq12(self):
        return 2*(self.n - 1)*self.alpha,2*(self.n - 2)*self.alpha
    def AvoidAnti(self,k):
        lc = (4*(self.n + k) / (4*self.n-3) - 1)*self.result
        return lc

if __name__ == '__main__':

    Alpha = [200*10**6,340*10**6]#Hz
    LightSpeed = [0.9*10**8,1.2*10**8] #m/s

    Weak = TwoQubit('weak')
    for alpha in Alpha:
        for c in LightSpeed:
            print('--------------')
            Lweak = Weak.MirrorLength(c, alpha)
            print('%s couple,c = %sx10^8m/s,alpha = %s MHz,length = %s mm' % (
            'weak',Lweak[0] / 10 ** 8, Lweak[1] / 10 ** 6, Lweak[2]))
            Freq01Weak = Weak.Freq01()
            Freq12Weak = Weak.Freq12()
            print("frequency 01 limit: %sGHz,n = %s" % (Freq01Weak[0] / 10 ** 9, Freq01Weak[2] - 1))
            print("frequency 12 limit: %sGHz,n = %s" % (Freq12Weak[0] / 10 ** 9, Freq01Weak[2] - 1))
            for k in range(3):
                LcWeak = Weak.AvoidAnti(k)
                print("k = %s,lc = %s mm"%(k,LcWeak))
            print('<=======>')
            print("frequency second: %sGHz,n = %s" % (Freq01Weak[1] / 10 ** 9, Freq01Weak[2]- 2))
            print("frequency 12 second: %sGHz,n = %s" % (Freq12Weak[1] / 10 ** 9, Freq01Weak[2] - 2))
            print('--------------')


    Strong = TwoQubit('strong')
    for alpha in Alpha:
        for c in LightSpeed:
            print('--------------')
            Lstrong = Strong.MirrorLength(c, alpha)
            print('%s couple,c = %s x10^8m/s,alpha = %s MHz,length = %s mm' % (
                'weak', Lstrong[0] / 10 ** 8, Lstrong[1] / 10 ** 6, Lstrong[2]))
            Freq01Strong = Strong.Freq01()
            Freq12Strong = Strong.Freq12()
            print("frequency 01 limit: %sGHz,n = %s" % (Freq01Strong[0] / 10 ** 9, Freq01Strong[2] - 1))
            print("frequency 12 limit: %sGHz,n = %s" % (Freq12Strong[0] / 10 ** 9, Freq01Strong[2] - 1))
            for k in range(3):
                LcStrong = Strong.AvoidAnti(k)
                print("k = %s,lc = %s mm"%(k,LcStrong))
            print('<=======>')
            print("frequency second: %sGHz,n = %s" % (Freq01Strong[1] / 10 ** 9, Freq01Strong[2] - 2))
            print("frequency 12 second: %sGHz,n = %s" % (Freq12Strong[1] / 10 ** 9, Freq01Strong[2] - 2))
            print('--------------')