#list comprehension
x = [ i for i in range(4)]
print(x)
b = [ c for c in list(x)]
print(b)
if [i for  i in list(b) if i > 3 in i ]:
    print("yes got it ")
x = ['1','2','3','5']
y = [int(i) for i in x]
print(y)


vec = [[1,2,3],[4,5,6],[7,8,9]]
result = [num for elem in vec for num in elem]
print(result)