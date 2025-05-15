#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    different_set_a = set_1.difference(set_2)
    different_set_b = set_2.difference(set_1)
    
    different_set = different_set_a.union(different_set_b)
    return(different_set)
