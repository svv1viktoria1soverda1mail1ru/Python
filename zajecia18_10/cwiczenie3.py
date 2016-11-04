#funkcje
def pierw(n):
    return n**0.5

print pierw(3)

def pierw2(n):
    if n>=0:  return n**0.5

print pierw2(4)

def pierw3(n):
    if n>=0: return n**0.5
    else:  return (-n)**0.5*1j

print pierw3(-6)

def rs(a,b):
    return a-b,a+b

print rs(8,4)

def suma(*arg):
    s=0
    for x in arg:
        s+=x
    return s

print suma(*range(10))