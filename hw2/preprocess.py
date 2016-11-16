from nltk.draw.tree import draw_trees
from nltk import tree, treetransforms
from copy import deepcopy
from random import randint
import sys

filename = sys.argv[1]

outputfile = "trees/testing_data.txt"

def reconst(string, val):
    new_s = ""
    p = string.find("(")
    while p != -1:
        new_s += "(" + str(val)
        b = string.find(" ", p)
        p = string.find("(", b)   
        new_s += string[b:p]
    return new_s

with open(filename, 'r') as f:
    s = ""
    trees_str = []
    for line in f:
        if line != "\n":
            s += line.strip()+" "
        else:
            trees_str.append(s)
            s = ""

with open(outputfile, 'w+') as f:
    for sentence in trees_str:
        t = tree.Tree.fromstring(sentence, remove_empty_top_bracketing=True)
        t.collapse_unary(collapsePOS=True, collapseRoot = True)
        t.chomsky_normal_form()
        s = ' '.join(t.pformat().split())
        print(s)
        print()
        s = reconst(s, 0)
        f.write( s +')'+'\n' )
