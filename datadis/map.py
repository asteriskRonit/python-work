from calendar import prmonth
def type_no(no):
    if no % 2==0:
        return "the number {} is even ".format(no)
    else:
        return "the number {} is odd ".format(no)

print(type_no(10),type_no(11))
lisy=[10,11,21,12,90,98]
lo=list(map(type_no,lisy))
print(lo)

