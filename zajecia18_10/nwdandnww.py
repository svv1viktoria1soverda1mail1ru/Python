
print "Podaj dwie liczby naturalne:"
a = input("Pierwsza:")
b = input("Druga:")


def funkcja(a,b):
    zm = ""
    if a > b:
        w = a
        m = b
    else:
        w = b
        m = a
    r = w % m
    while r:
        w = m
        m = r
        r = w % m
    zm+= "NWD liczb %i i %i wynosi %i, a ich NWW wynosi %i" % (a,b,m,a*b/m)
    return zm


print funkcja(a,b)