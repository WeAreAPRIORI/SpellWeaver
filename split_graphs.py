# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 16:13:11 2019

@author: Efren
"""

# this funtion checks if message is too long and in that case it splits it
# into chunks and creates little networks our of it.

def make_multiple_graphs(my_message,chords,my_file_size):
    # first split message into words
    my_words = my_message.split()
    lw=len(my_words)
    mwr = 5 # you may make bigger but var "my_file_size" has to appropriately grow
    max_words = mwr**2
    if (lw > max_words):
        my_words = my_words[0:max_words]
        lw=max_words
    # then create a treadle sequence, shaft sequence, and design for each word
    from computation_functions import create_treadle_sequence
    from computation_functions import create_threading_sequence
    from computation_functions import populate_matrix_binary
#    Wl = [list(wi) for wi in my_words]
#    Ts = [[create_threadle_sequence(wi)] for wi in Wl]
#    Ss = [[create_threading_sequence(wi)] for wi in Wl]
    Ts = []
    Ss = []
    D = []
    for ii in range(0,lw):
        wi = my_words[ii]
        wi = list(wi)
        tsi = create_treadle_sequence(wi)
        ssi = create_threading_sequence(chords,wi)
        di = populate_matrix_binary(chords,tsi,ssi)
        Ts.append(tsi)
        Ss.append(ssi)
        D.append(di)
    # now we create the networks and display them!!!
    import matplotlib.pyplot as plt
#    plt.ioff()
    import networkx as nx
    import math
    import numpy as np
    fig2 = plt.figure(2,figsize=(my_file_size,my_file_size))
    magic_list = np.asarray([4, 6, 9, 12, 16, 20, 25, 30, 36, 42, 49, 56, 64, 72, 81, 90, 100])
    which_factor = np.where(lw<=magic_list)[0]
    qs = magic_list[which_factor[0]]
    a=math.floor(math.sqrt(qs))
    b=math.ceil(math.sqrt(qs))
    browny_color = '#614537'
    for ii in range(0,lw):
        if lw > 3:
            plt.subplot(a,b,ii+1)
        else:
            plt.subplot(1,lw,ii+1)
        G = nx.from_numpy_array(D[ii])
        posG = nx.kamada_kawai_layout(G)
##        nx.draw_kamada_kawai(G)
#        posG = nx.shell_layout(G)
        nx.draw(G,posG)
        if (lw>5):
            nsize = 300
            nw = 1
        else:
            nsize=500
            nw=2
        nx.draw_networkx_nodes(G,posG,
                nodelist = list(G.nodes),
                node_color = 'white',
                edgecolors = browny_color,
                linewidths = nw,
                node_size = nsize)
        nx.draw_networkx_edges(G,posG,
                edgelist = list(G.edges),
                edge_color = browny_color,
                width = 2, alpha = .75)
    plt.show()
    return fig2;