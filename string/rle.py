def rle(data):
    prev = None
    count = 0
    ret = ''
    for c in data:
        if c != prev and prev is not None:
            ret += str(count) + prev
            count = 1
        else:
            count += 1
        prev = c
    ret += str(count) + prev
    return ret

str_to_compress = input('Enter string to compress....')

print('Compressed: ' + rle(str_to_compress))
