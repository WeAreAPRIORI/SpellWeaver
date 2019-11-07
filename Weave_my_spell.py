# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:17:02 2019

@author: Efren
"""

def weave_my_spell(my_message):
    #
    my_message = my_message.lower()
    mlist = list(my_message)
    ml = len(mlist)
    #
    # We start by designing the tie-up patterns
    def create_coding_chords():
        a_chords_raw = [[0,0,1,1,1,1,0,0],
                     [0,1,1,1,0,1,1,0],
                     [0,1,1,1,0,1,0,0],
                     [0,1,0,1,1,0,0,0],
                     [0,1,1,1,0,0,1,1],
                     [0,1,0,1,0,1,0,1],
                     [0,1,0,1,1,0,0,1],
                     [0,1,0,1,0,1,1,1],
                     [0,1,0,0,1,0,0,1],
                     [1,0,0,0,1,1,1,1],
                     [1,0,0,0,1,1,1,0],
                     [1,0,0,0,1,0,0,1],
                     [1,0,0,0,0,1,0,1],
                     [1,0,1,1,1,1,0,1],
                     [1,0,1,1,0,0,1,0],
                     [1,0,1,0,1,1,0,0],
                     [1,0,1,0,1,0,1,0],
                     [1,0,1,0,0,1,0,1],
                     [1,0,0,1,1,1,0,0],
                     [1,0,0,1,0,1,0,0],
                     [1,0,0,0,1,0,1,0],
                     [1,0,0,0,0,1,1,0],
                     [1,1,0,0,0,0,1,1],
                     [1,0,0,0,0,0,1,0],
                     [1,0,0,1,1,0,0,1],
                     [1,0,0,1,0,0,1,0]
                     ]
        return a_chords_raw;
    a_chords_raw = create_coding_chords()
    #
    # treadle sequence
    from computation_functions import create_treadle_sequence
    treadle_sequence = create_treadle_sequence(my_message)

    # threading sequence
    from computation_functions import create_threading_sequence
    shaft_sequence = create_threading_sequence(a_chords_raw,treadle_sequence)

    # make design
    from computation_functions import populate_matrix_binary
    design = populate_matrix_binary(a_chords_raw,treadle_sequence,shaft_sequence)
    #
    ### ::: CREATE SOME PLOTS ::: ###
    # First let's get an appropriate image size, in inches
    my_image_size = 10
    
    import matplotlib.pyplot as plt
    plt.figure(1,figsize=(my_image_size,my_image_size))
    plt.imshow(design)
    plt.axis('off')
    plt.show();
    
    # Now, let's obtain the network from the weave.
    # In order for it not to be messy, we have to split the spell into words.
    # To spare you the time, we have a function that does this in another file. We'll just call it.
    # now we just call the other function
    from split_graphs import make_multiple_graphs
    make_multiple_graphs(my_message,a_chords_raw,my_image_size)
    return ;