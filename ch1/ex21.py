# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def x(t):
    if(t >= -2 and t < -1):
        return t + 1
    elif( t >= -1 and t < 0 ):
        return 1
    elif( t >= 0 and t < 1):
        return 2
    elif( t >= 1 and t < 2):
        return 2 - t
    else:
        return 0
    
    
def drawx(t, offset, reverse):
    y = []
    for i in t:
        if(reverse):
            i = -i
        y.append(x(i))
        
    if (offset != 0):
        t = t - offset
    plt.plot(t,y)

def cfgAndShow():
    plt.xticks(np.arange(-3,3,1))
    plt.yticks([-3, 3])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    plt.show()

def main():
    t = np.arange(-2, 3, 0.05)
    drawx(t, 0, False)
    drawx(t, 0, True)
    #t = np.arange(-2, 3, 0.05)
    drawx(t, -2, False)
    cfgAndShow()


if __name__ == '__main__':
    main()
