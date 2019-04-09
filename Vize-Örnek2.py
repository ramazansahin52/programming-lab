#matristeki '0' oranı %30 un altında ise matrisi hashe atayan program
a=[[1,2,3,5],[4,5,6,2],[6,5,5,0],[4,0,0,0],[0,5,6,9]]
row=len(a)
colm=len(a[0])
max=row*colm
zCount=0
for i in range(row):
    for j in range(colm):
        if(a[i][j]==0):
            zCount+=1

percent=(zCount*100)//max
if(percent<30):
    my_hash={}
    for i in range(row):
        for j in range(colm):
            my_hash[(i,j)]=a[i][j]

    for key in my_hash:
        print(my_hash[key],end=" ")
else:
    print("matristeki 0 orani %",percent)
