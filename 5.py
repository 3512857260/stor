a=[1,5,21,30,15,9,30,24]
# print("排序前",a)
# a.sort()
# print("排序后",a)
b=0
for i in a:
    if i%5==0:
        b=b+i
print(b)