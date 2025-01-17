def partition(array, begin, end, cmp):
    while begin < end:
         while begin < end:
            if cmp(array[begin], array[end]):
                (array[begin], array[end]) = (array[end], array[begin])
                break
            end -= 1
         while begin < end:
            if cmp(array[begin], array[end]):
                (array[begin], array[end]) = (array[end], array[begin])
                break
            begin += 1
    return begin

def sort(array, cmp=lambda x, y: x > y, begin=None, end=None):
    if begin is None: begin = 0
    if end   is None: end   = len(array)
    if begin < end:
        i = partition(array, begin, end-1, cmp)
        sort(array, cmp, begin, i)
        sort(array, cmp, i+1, end)
