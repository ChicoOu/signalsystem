# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

class Ex22:
    _n = None
    _y = None
    _no = 221
    _start_index = -10
    _end_index = 11
    _step = 1

    def draw(self, x=None, scale=1, offset=0):
        plt.subplot(self._no)
        if(scale != 1):
            tmpy = np.zeros(self._y.size)
            for i in self._n:
                index = scale*i + offset
                if( index >= self._start_index and index < self._end_index ):
                    if( x == None ):
                        tmpy[i - self._start_index] = self._y[index - self._start_index]
                    else:
                        tmpy[i - self._start_index] = x(index - self._start_index)

            plt.stem(self._n, tmpy)
        else:
            plt.stem(self._n + offset, self._y)
        self._no = self._no + 1

    def h(self, n):
        print("haha")
        return 0


    def show(self):
        plt.show()

    def __init__(self):
        self._n = np.arange(self._start_index, self._end_index, self._step)
        self._y = np.array([0, 0, 0, 0, 0, 0, -1, -0.5, 0.5, 1, 1, 1, 1, 0.5, 0, 0, 0, 0, 0, 0, 0])


if(__name__ == '__main__'):
    ex = Ex22()
    ex.draw(None, 1, 0)
    ex.draw(None, 1, -4)
    ex.draw(None, 3, 1)
    ex.draw(None, -1, 4)
    ex.show()
    f = ex.h
    f(2)