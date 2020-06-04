#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:53:05 2020

@author: usuario
"""


import random

import time

from mpi4py import MPI 
 

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

 

# Complete the how_many_max_values_parallel function below.

def how_many_max_values_parallel(ar):
    

    
    
    MASTER = 0
    FROM_MASTER = 1
    FROM_WORKER = 2
   
    source = 0
    rows = 0
    
    
    
    
    
    comm = MPI.COMM_WORLD
    
    #Obtener tamano de grupo de proceso
    numtasks = comm.size
    
    #Obtener el id de procesos
    taskid = comm.Get_rank()
    
    
    #if rc != 0:
        #print("error al inicializar MPI y obtener los id tasks")
        
    numworkers = numtasks - 1
    
    #Mastertask
    #print('Llego hasta aqui 1')
    
    if taskid == MASTER:
        
        #print('Llego hasta aqui 2')
        """
        ar_1 = ar[0 : int(len(ar)/8)]
        ar_2 = ar[int(len(ar)/8) : int(2 * len(ar)/8)]
        ar_3 = ar[int(2 * len(ar)/8) : int(3 * len(ar)/8)]
        ar_4 = ar[int(3 * len(ar)/8 ): int(4 * len(ar)/8)]
        ar_5 = ar[int(4 * len(ar)/8) : int(5 * len(ar)/8)]
        ar_6 = ar[int(5 * len(ar)/8) : int(6 * len(ar)/8)]
        ar_7 = ar[int(6 * len(ar)/8) : int(7 * len(ar)/8)]
        ar_8 = ar[int(7 * len(ar)/8) : len(ar)]
        """
    
    
        print("Numero de tareas de trabajo",numworkers)
        
        
        
        averow = len(ar)//numworkers
        #extra = ar_1%numworkers
        offset = 0
        mtype = FROM_MASTER
        
        for dest in range(numworkers):
            
            if dest+1 <= extra:
                rows = averow + 1
            else:
                rows = averow
                
            comm.send(offset, dest=dest+1, tag=mtype)
            comm.send(rows, dest=dest+1, tag=mtype)
            comm.send(matrizA[offset:rows+offset], dest=dest+1, tag=mtype)
            
            comm.send(matrizB, dest=dest+1, tag=mtype)
            
            offset = offset + rows
            
        mtype = FROM_WORKER
        
        concat = []
        for n in range(numworkers):
            
            source = n
            
            offset = comm.recv(source=source+1, tag=mtype)
            rows = comm.recv(source=source+1, tag=mtype)
            aux = comm.recv(source=source+1, tag=mtype)
            aux = aux[:rows]
            concat = concat + aux
        
        #print(concat)
            
        end_time = time.time()
        
        print("Time Secuencial with", dimension, "x", dimension, "dimension: ", end_time - start_time)
    
        
        #print('Aqui las 30 primeras filas de el resultado Matriz C ')
        
        
        
    if(taskid > MASTER):
        mtype = FROM_MASTER
        offset = comm.recv(source=MASTER,tag=mtype)
        rows = comm.recv(source=MASTER,tag=mtype)
        matrizA = comm.recv(source=MASTER,tag=mtype)
        matrizB = comm.recv(source=MASTER,tag=mtype)
        
        for k in range(columna2):
            #print('rows = ' + str(rows))
    
            for i in range(rows):
                #print('Si esta entrando, revisa los fors pedazo de idiota.')
    
                
                    
        mtype = FROM_WORKER
        comm.send(offset,dest=MASTER,tag=mtype)
        comm.send(rows,dest=MASTER,tag=mtype)
        comm.send(matrizC,dest=MASTER,tag=mtype)
        #print(matrizC)
    
    
    return 0

 

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