import pandas as pan
file=('G:\core\python\panda\wthr.xlsx')
fok=pan.read_excel(file)
print(fok)

newdf=fok.fillna({
    'temperature':0,
    'windspeed':0,
    'event':'no event'
})
print(newdf)

newdf=fok.fillna(method='ffill')
print(newdf)
 

newdf=fok.interpolate()
print(newdf)
