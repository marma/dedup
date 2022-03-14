

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

