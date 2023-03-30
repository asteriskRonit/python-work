def park():
    print("after 12")
    yield 12
    print("before 13")
    yield 13

df=park()
print(df.__next__())   
print(df.__next__()) 