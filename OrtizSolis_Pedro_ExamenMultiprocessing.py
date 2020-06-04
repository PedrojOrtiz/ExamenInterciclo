#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:52:02 2020

@author: usuario
"""

import random

import time
 

import multiprocessing

def how_many_max_values_sequential(ar):

    #find max value of the list

    maxValue = 0

    for i in range(len(ar)):

        if i == 0:

            maxValue = ar[i]

        else:

            if ar[i] > maxValue:

                maxValue = ar[i]

    #find how many max values are in the list

    contValue = 0

    for i in range(len(ar)):

        if ar[i] == maxValue:

            contValue += 1

 

    return contValue

 

def find_max_value(ar):
    
    maxValue = 0

    for value in ar:
        if value > maxValue:
            maxValue = value
       
    return maxValue

def cont_max_value(ar, maxValue):
    
    contValue = 0

    for value in ar:

        if value == maxValue:

            contValue += 1

    return contValue
    
    

# Complete the how_many_max_values_parallel function below.

def how_many_max_values_parallel(ar):

    
    ar_1 = ar[0 : int(len(ar)/8)]
    ar_2 = ar[int(len(ar)/8) : int(2 * len(ar)/8)]
    ar_3 = ar[int(2 * len(ar)/8) : int(3 * len(ar)/8)]
    ar_4 = ar[int(3 * len(ar)/8 ): int(4 * len(ar)/8)]
    ar_5 = ar[int(4 * len(ar)/8) : int(5 * len(ar)/8)]
    ar_6 = ar[int(5 * len(ar)/8) : int(6 * len(ar)/8)]
    ar_7 = ar[int(6 * len(ar)/8) : int(7 * len(ar)/8)]
    ar_8 = ar[int(7 * len(ar)/8) : len(ar)]
    
    maxValues = []
    
    p = multiprocessing.Pool(8)
    
    maxValues.append(p.apply(find_max_value, (ar_1, )))
    maxValues.append(p.apply(find_max_value, (ar_2, )))
    maxValues.append(p.apply(find_max_value, (ar_3, )))
    maxValues.append(p.apply(find_max_value, (ar_4, )))
    maxValues.append(p.apply(find_max_value, (ar_5, )))
    maxValues.append(p.apply(find_max_value, (ar_6, )))
    maxValues.append(p.apply(find_max_value, (ar_7, )))
    maxValues.append(p.apply(find_max_value, (ar_8, )))
    
    maxValue = find_max_value(maxValues)
    
    #p = multiprocessing.Pool(8)
    
    """
    contMaxValue = 0
    
    contMaxValue += p.apply(cont_max_value, (ar_1, maxValue, ))
    contMaxValue += p.apply(cont_max_value, (ar_2, maxValue, ))
    contMaxValue += p.apply(cont_max_value, (ar_3, maxValue, ))
    contMaxValue += p.apply(cont_max_value, (ar_4, maxValue, ))
    contMaxValue += p.apply(cont_max_value, (ar_5, maxValue, ))
    contMaxValue += p.apply(cont_max_value, (ar_6, maxValue, ))
    contMaxValue += p.apply(cont_max_value, (ar_7, maxValue, ))
    contMaxValue += p.apply(cont_max_value, (ar_8, maxValue, ))
    """
    
    contMaxValue = cont_max_value(ar, maxValue)
    
    return contMaxValue

 

if __name__ == '__main__':

    ar_count = 40000000

    #Generate ar_count random numbers between 1 and 30

    ar = [random.randrange(1,30) for i in range(ar_count)]

    inicioSec = time.time()

    resultSec = how_many_max_values_sequential(ar)

    finSec =  time.time()

   

    inicioPar = time.time()   

    resultPar = how_many_max_values_parallel(ar)

    finPar = time.time()   

   

    print('Results are correct!\n' if resultSec == resultPar else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms with %d items\n' % ((finSec - inicioSec)*1000, ar_count))

    print('Parallel Process took %.3f ms with %d items\n' % ((finPar - inicioPar)*1000, ar_count))
