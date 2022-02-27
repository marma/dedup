#!/usr/bin/env python3

from sys import stdin,stderr,stdout
from re import compile,match,sub,split
from hashlib import md5
from collections import Counter
from json import dumps
from multiprocessing import Pool

split_sentence_p = r'([.!?][ .!?]*)'
remove_chars = r'[^0-9a-zA-ZåäöÅÄÖéÉ\-]'


def normalize(text):
    return ' '.join(sub(remove_chars, ' ', text).split())


def sentencize(text):
    s = split(split_sentence_p, text)
    sentences = [ (s[2*i] + s[2*i+1]).strip() for i in range(int(len(s)/2)) ]

    return sentences


def hashes(sentences):
    ret = []

    if len(sentences) < 3:
        sentences += (3-len(sentences)) * [ '$' ]

    for i in range(len(sentences)-2):
        ngram = normalize(' '.join(sentences[i:i+3]))

        ret += [ md5(ngram.encode('utf-8')).hexdigest() ]

    return ret


def chunker(i):
    # assume document starts with '### START'
    d = []
    id = None

    for line in i:
        if line.startswith('## START ##'):
            if d != []:
                yield (id, '\n'.join(d))
                d = []

            id = line[12:-1]
        else:
            d += [ line[:-1] ]

    if d != []:
        yield (id, '\n'.join(d))
            

def work(chunk):
    i,text = chunk
    s = sentencize(text)
    h = hashes(s)
    
    return dumps({ i: h })


if __name__ == '__main__':
    n_processes = 4

    # sentencize and get hashes
    with Pool(processes=n_processes) as pool:
        for jl in pool.imap_unordered(work, chunker(stdin)):
            print(jl)

