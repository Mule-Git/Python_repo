from  mathfun.myfun import pow

def comp(a, b):
    result = pow(a, b)

    return f'{b} is postive' if result > 1 else f'{b} is negative'


print(comp(3,-4))