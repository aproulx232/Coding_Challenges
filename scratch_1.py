

def mult_but (a_list):
    out_list = []
    product= 1
    for x in a_list:
        product =product * x
    for j in a_list:
        out_list.append(product/j)
    return out_list

def mult_but2 (a_list):
    out_list = []
    for i in  a_list:
        product = 1
        for j in  a_list[:i-1]:
            product = product * j
        for k in a_list[i:]:
            product = product * k
        out_list.append(product)
    return out_list

print(mult_but2([1,2,3,4,5]))