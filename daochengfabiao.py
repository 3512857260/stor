q=9
while q>0:#外边q是横向坐标
#内部循环m开始
    m=1
    while m<q+1:#里边m是纵向坐标
        print(str(m)+"x"+str(q)+"="+str(q*m)+"  ",end="")
        m=m+1
    q=q-1
    print()