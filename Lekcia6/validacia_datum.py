import datetime

datetime.datetime.strptime("830228", "%y%m%d")


datum = "836118"
if datum[2] in ["5", "6"]:
    datum = datum[:2]+str(int(datum[2])-5)+datum[3:6]
print(datum)
datetime.datetime.strptime(datum, "%y%m%d")
