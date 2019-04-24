a = [i for i in range (10,100)]
print(sum(map(lambda x: x**2,filter(lambda x: x%9==0,a))))
