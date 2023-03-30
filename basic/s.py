#add two number?
def solveMeFirst(a,b):

   return a+b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
res = solveMeFirst(num1,num2)
print(res)

#delete a number from array?
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

for row in array:
    for value in row:
        if value != 5:
            row.remove(value)

print(array)

[[2], [5], [8]]