#verilen matristeki 0 ların tüm eleman sayısına oranını bulan program
a=[[1,2,3,5],[4,5,6,0],[0,0,0,0],[0,0,0,0],[0,5,6,9]]
row=len(a)
colm=len(a[0])
max=row*colm
zCount=0
for i in range(row):
    for j in range(colm):
        if(a[i][j]==0):
            zCount+=1

percent=(zCount*100)//max
print("matristeki 0 sayisi :",zCount)
print("matristeki toplam eleman sayisi: ",max)
print("matristeki 0 orani %",percent)
