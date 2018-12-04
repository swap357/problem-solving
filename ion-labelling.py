def parent_of(element,h):
    last_el = 2**h-1
    sub_size = last_el/2
    sub1 = sub_size
    sub2 = sub1 + sub_size
    parent = -1

    if element == last_el or element > last_el:
        return parent

    while sub_size!=0:
        if sub1==element or sub2==element:
            parent = sub2+1
            break

        sub_size /= 2
        # print sub_size
        if element < sub1:
            sub1 -= sub_size+1
        else:
            sub1 += sub_size
        sub2 = sub1 + sub_size

    return parent

def answer(h,q):
    res= []
    for i in range(len(q)):
        res.append(parent_of(q[i],h))
    return res

print answer(29,[1,6,14,31])