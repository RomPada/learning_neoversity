import copy

a = 2
b = a 
c = copy.deepcopy(a)

c = c + 1

print(a,b, c)