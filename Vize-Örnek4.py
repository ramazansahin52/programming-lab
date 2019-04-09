
#verilen listedeki sayıların ortalamasını ve standart sapmasını bulan fonksiyon
import math
a=[5,3,6,9,8,7,4]
def fonk(mylist):
    tp=0
    ort=sum(mylist)/len(mylist)
    for i in range(len(mylist)):
        tp+=((mylist[i]-ort)**2)
    stnd=tp/((len(mylist)-1))

    return ort,math.sqrt(stnd)

print(fonk(a))
