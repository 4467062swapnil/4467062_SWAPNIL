#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    h=int(s[0:2])
    halftime=s[8:10]
    if halftime=="PM":
        if h==12:
            h=str(h)
        else:
            h=h+12
            h=str(h)

    else:
        if h==12:
            h=str("00")
        else:
            h="0"+str(h)
    print(h+":"+s[3:5]+":"+s[6:8])

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
