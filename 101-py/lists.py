any = [1,True,False,"none"]
any.extend([12,4,5])
monkey = any+[1,2,3,3,4,True,5]
monkey[0] = 10

print(len(monkey))