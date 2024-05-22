#!/usr/bin/env python3

def return_evens(num_list):
    even_lc = [n for n in num_list if n % 2 == 0]
    return even_lc

    pass

def make_exclamation(sentence_list):
   exclamation_szn = [n + "!"for n in sentence_list
    ]
   return exclamation_szn
    