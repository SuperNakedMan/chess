#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:48:30 2020

@author: pasq
"""

import numpy as np
import tensorflow as tf
import math

c = tf.constant(2)

index64 = [
    0, 47,  1, 56, 48, 27,  2, 60,
   57, 49, 41, 37, 28, 16,  3, 61,
   54, 58, 35, 52, 50, 42, 21, 44,
   38, 32, 29, 23, 17, 11,  4, 62,
   46, 55, 26, 59, 40, 36, 15, 53,
   34, 51, 20, 43, 31, 22, 10, 45,
   25, 39, 14, 33, 19, 30,  9, 24,
   13, 18,  8, 12,  7,  6,  5, 63
]

def ls1b(bb):
    debrujin = 0x03f79d71b4cb0a89
    assert(bb != 0)
    index_val = ((bb ^ (bb-1))*debrujin) >> 58
    return index64[index_val], index_val

class BitBoard():
    def __init__(self, num):
        self.bb = num
        self.bbbinary = bin(self.bb)
    
    def printbb(self):
        full_bb = 2**64-1
        pos = bin(full_bb - self.bb)
        pos = pos.replace("0", "x")
        pos = pos.replace("1", "0")
        for i in range((len(pos)-2)//8+1):
            print(pos[2+8*i:(i+1)*8+2])
        
        print(pos)


class Piece(BitBoard):
    def __init__(self, num, color):
        super().__init__(num)
        self.color = color
        assert(math.log(self.bb, 2).is_integer())
        self.position = int(math.log(self.bb, 2))
    
    def rankMask(self):
        return(0xff << (self.position & 56))
        
    def fileMask(self):
        return (0x0101010101010101 << (self.position & 7))
    
    
    def diagonalMask(self):
        maindia = 0x8040201008040201
        diag = 8*(self.position & 7) - (self.position & 56)
        nort = -diag & ( diag >> 31)
        sout =  diag & (-diag >> 31)
        return(maindia >> sout)<<nort
    
    def antidiagMask (self):
        maindia = 0x0102040810204080
        diag = 56- 8*(self.position &7) - (self.position&56)
        nort = -diag & ( diag >> 31)
        sout =  diag & (-diag >> 31)
        return (maindia >> sout) << nort



class Root(Piece):
    def __init__(self, num, color):
        super().__init__(num, color)
    
    def attacks(self):
        return self.rankMask() | self.fileMask()
        

#Initial value of the occupied bb
occupiedBB = BitBoard(18446462598732906495)
root = BitBoard(2**7)

0b
x0000000
0x000000
00x00000
000x0000
0000x000
00000x00
000000x0
0000000x