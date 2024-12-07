import Arts.arts as arts

def bitxt(data): 
    '''
    This converts the binary code entered by user to text
    '''

    dec = []
    for b in data:
        d = int(f"0b{b}", 2)
        dec.append(d)

    english = ''
    for asc in dec:
        let = chr(asc)
        english += let

    return f"{arts.art["output"]}\n\n {english}"


def txtbi(dataeng):
    '''
    This converts text entered by user to binary
    '''

    bindata = ''
        
    for char in dataeng:
        ascd = ord(char)
        bi = bin(ascd)[2:]

        bindata = bindata + ' ' + bi

    return bindata