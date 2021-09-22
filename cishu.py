List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
q=[]
for a in  List:
    if a in q:
        continue
    else:
        q.append(a)
# print(q)
for b in q:
    j=0#个数
    for c in List:
        if b==c:
            j=j+1
    print(j,b)
