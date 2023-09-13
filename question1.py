og_list = ['this' , 'is', 'a', 'sentence', '.']


def inplace_swap(alist):
    alist[0], alist[-1] = alist[-1],alist[0]
    
sorted_list = inplace_swap(og_list)
print(f'{og_list =} after')