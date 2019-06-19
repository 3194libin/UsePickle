def out(x):
    return x%2
temp = range(50)
s = filter(out,temp)
print(list(s))
