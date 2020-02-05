def m():
    s=input()
    t=l=s.split()
    l=[abs(float(i))for i in l]
    return t[l.index(min(l))]


