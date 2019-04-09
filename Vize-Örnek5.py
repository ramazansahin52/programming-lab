#verilen matrisin satır ve sutundaki elemanlar toplamının en büyük ve küçük değerlerin satır ve sutun numaraları
a=[[1,2,3],[4,5,6],[7,8,9]]
def fonk(mymatrix):
    rowssum=[]
    colmsum=[]
    n=len(mymatrix)
    for i in range(n):
        rowssum.append(0)
        colmsum.append(0)

    for i in range(n):
        for j in range(n):
            rowssum[i]+=mymatrix[i][j]
            colmsum[i]+=mymatrix[j][i]
    print("Satirlar toplami en büyük olan index :",rowssum.index(max(rowssum))+1)
    print("Satirlar toplami en kücük olan index :",rowssum.index(min(rowssum))+1)
    print("Sutunlar toplami en büyük olan index :",colmsum.index(max(colmsum))+1)
    print("Sutunlar toplami en büyük olan index :",colmsum.index(min(colmsum))+1)

fonk(a)
