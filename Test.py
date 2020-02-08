# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:21:36 2019

@author: LENOVO
"""
from pygame import mixer
import time
def alert():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()   
alert()