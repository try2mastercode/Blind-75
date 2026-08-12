a={"a":1,"b":2,"c":3,"d":4,"e":5}
print(a)
a["6"]=10
print(a)
a.pop("6")
print(a)
print("key:",a.keys(),"\n",a.values())
for i,j in a.items():
    print(i,":",j)
a=[1,2,3,4,5,1,2,3,4,1,2,3,1,2,1,1,2,3,4,5,6]
from collections import Counter
print(Counter(a))