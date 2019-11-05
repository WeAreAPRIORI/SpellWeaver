# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:35:16 2019

@author: Efren
"""

def populate_matrix(temp_chords,ts,ss):
    import numpy as np
    N_ts = len(ts)
    N_ss = len(ss)
    D = np.zeros((N_ts,N_ss))
    for tt in range(0,len(ts)):
        c = temp_chords[ts[tt]]
        for ii in c:
            rs = np.where(ss == ii)
            D[tt,rs] = 1
    return D;

def populate_matrix_binary(chords,ts,ss):
    import numpy as np
    N_ts = len(ts)
    N_ss = len(ss)
    D = np.zeros((N_ts,N_ss))
    for tt in range(0,len(ts)):
        c = chords[ts[tt]]
        c = np.asarray(c)
        c = np.where(c == 1)
        for ii in c[0]:
            rs = np.where(ss == ii)
            D[tt,rs] = 1    
    return D;

def create_treadle_sequence(my_message):
    import numpy as np
    # create alphabet
    alphabet = ['abcdefghijklmnopqrstuvwxyz']
    alphabet = list(alphabet[0])
    alphabet = np.asarray(alphabet)
    # now the sequence
    msg_list = list(my_message)
    ml = len(msg_list)
    # here catch if list is empty or too long.
    max_size = 500
    if (ml == 0):
        print("please write a message")
        return [0];
    elif (ml > max_size):
        msg_list = msg_list[0:max_size]
        ml = max_size
    treadle_sequence = np.zeros((ml))
    for ii in range(0,ml):
        ci = np.where(alphabet == msg_list[ii])
        if ci[0].size == 1:
            treadle_sequence[ii] = int(ci[0])
            # else just ignore the character
        treadle_sequence = np.array(treadle_sequence,dtype = int)
    return treadle_sequence;

def create_threading_sequence(a_chords_raw,treadle_sequence):
    import math
    import numpy as np
    N_shafts = len(a_chords_raw[0])
    L_shafts = len(treadle_sequence)
    shaft_sequence = np.zeros((L_shafts + math.floor(L_shafts/N_shafts)))
    cbit = -1
    for i in range(0,len(shaft_sequence)):
        if np.mod(i,N_shafts) == 0:
            cbit = cbit*(-1)
        if (cbit > 0):
            shaft_sequence[i] = np.mod(i,N_shafts)
        else:
             shaft_sequence[i] = N_shafts - 1 - np.mod(i,N_shafts)
    rep = N_shafts*(1 + np.arange(math.floor(L_shafts/N_shafts)))
    shaft_sequence = np.asarray(shaft_sequence)
    shaft_sequence = np.delete(shaft_sequence,rep)
    return shaft_sequence;
    


















#####################################################