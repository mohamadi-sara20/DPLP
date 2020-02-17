## main.py
## Author: Yangfeng Ji
## Date: 09-25-2015
## Time-stamp: <yangfeng 09/26/2015 00:10:59>

from code.evalparser import evalparser
from cPickle import load
import gzip, sys

def main(path, draw=True):
    bcvocab={}
    with open("resources/fa/lemm_paths.txt") as f:
        lemmas = f.readlines()
        for lemma in lemmas:
           word_clust, word, idx = lemma.split('\t')
           bcvocab[word] = word_clust
    with open("resources/fa/word_paths.txt") as f:
        words = f.readlines()
        for word in words:
            word_clust, word, idx = word.split('\t')
            bcvocab[word] = word_clust  

    evalparser(path=path, report=False, draw=draw,
               bcvocab=bcvocab,
               withdp=False)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
        print 'Read files from: {}'.format(path)
        main(path)
    elif len(sys.argv) == 3:
        path = sys.argv[1]
        draw = eval(sys.argv[2])
        print 'Read files from {}'.format(path)
        main(path, draw)
    else:
        print "Usage: python rstparser.py file_path [draw_rst_tree]"
        print "\tfile_path - path to the segmented file"

