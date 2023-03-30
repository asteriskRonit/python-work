import pandas as pd
def cal_sum(data):
    k=0;
    for d in range(0,data["calories"].count()):
          k+=data["calories"][d]
    return k    
data={
    "cal":[100,200],
    "dur":[10,20]
}
df=pd.DataFrame(data,index=["day1","day2"])
print(df)
print(type(df))
#print(df.loc[[0,1]])
file=('G:\core\python\panda\Book1.xlsx')
fg=pd.read_excel(file)
print(fg.shape)
sort=fg.sort_values(['calories'],ascending=False)
print(sort)
print("calories of sum :",cal_sum(fg))
print(sort.describe(),"\n\n",sort["calories"].mean())
fg=sort.describe()
print(sort["calories"])

#fg.to_excel("outp.xlsx")


