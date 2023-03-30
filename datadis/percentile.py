from turtle import TPen
import numpy
import matplotlib.pyplot as plt
age=[10,11,20,50,90,100,32,77]
x=numpy.percentile(age,100)
print(x)

random_no=numpy.random.uniform(4,5,6)
print(random_no)

normal=numpy.random.normal(4,5,6)
print(normal)

height=numpy.random.uniform(3,7,8)
print(type(height))

plt.scatter(age,height)
plt.show()




