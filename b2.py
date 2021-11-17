# ví dụ bên excel
# counting sort
# thuật toán UTC nam 3
# Thuật toán và ứng dụng-Nguyễn Tuấn Ngọc
# import numpy
# a=[1,4,1,2,7,1,2,5,3,6]
# tanxuat=[]
# caonhat=[]
# places=[]
# def fillmang():
#     for i in range(len(a)):
#         tanxuat.append(0)
#         places.append(0)
# def timtanxuat():
#     fillmang()
#     tmp=0
#     for i in a:
#         tanxuat[i]+=1
#     tmp=max(tanxuat)
#     for i in range(len(tanxuat)):
#         if tanxuat[i]==tmp:
#             caonhat.append(i)
# def countingsort():
#     for i in range(1,len(a)):
#         tanxuat[i]+=tanxuat[i-1]
#     for i in range(len(a)):
#         places[tanxuat[a[i]]-1]=a[i]
#         tanxuat[a[i]]-=1  
# if __name__ == '__main__':
#     timtanxuat()
#     countingsort()
    # print("mốt",caonhat)
    # if len(places)%2==0:
    #      print("Phan tu trung vi",(places[0]+places[len(places)-1])/2)
    # else:
    #      print("Phan tu trung vi",places[int(len(places)/2)])



# II sắp xếp ngoài
# bai 4
# 1
import math
class TronRun:
    def __init__(self,arr):
        self.arr=arr;
    def timm(TronRun):
        m=0
        while pow(2,m)<len(TronRun.arr):
            TronRun.batdautron(m)
            m+=1
    def Print(TronRun):
        print(TronRun.arr)
    def batdautron(TronRun,m):
        l=0
        f1=[]
        f2=[]
        f0=[]
        for i in range(len(TronRun.arr)):
            if l<pow(2,m):
                f1.append(TronRun.arr[i])
            else:
                f2.append(TronRun.arr[i])
            l+=1
            if l==2*pow(2,m):
                l=0
        while len(f1)>=1 and len(f2)>=1:
            top=0
            bottom=0
            while len(f0)<len(TronRun.arr):
                if len(f1)==0 or len(f2)==0:
                    if len(f1)==0:
                        while len(f2)>0:
                            f0.append(f2[0])
                            f2.pop(0)
                        TronRun.arr=f0
                        # print(f0)
                        return 0;
                    if len(f2)==0:
                        while len(f1)>0:
                            f0.append(f1[0])
                            f1.pop(0)
                        TronRun.arr=f0
                        # print(f0)
                        return 0;
                if f1[0]<f2[0] and top<pow(2,m):
                    f0.append(f1[0])
                    f1.pop(0)
                    top+=1
                elif bottom<pow(2,m):
                    f0.append(f2[0])
                    f2.pop(0)
                    bottom+=1
                if top==pow(2,m) and bottom==pow(2,m):
                    top=0
                    bottom=0
                elif top<pow(2,m) and bottom==pow(2,m) :
                    for i in range(top,pow(2,m)):
                        f0.append(f1[0])
                        f1.pop(0)
                    bottom=0
                elif top==pow(2,m):
                    for i in range(bottom,pow(2,m)):
                        f0.append(f2[0])
                        f2.pop(0)
                    top=0            
        TronRun.arr=f0
if __name__ == '__main__':
    a=[24,12,67,33,58,42,11,34,29,31]
    # a=[12,24,33,67,42,58,11,34,29,31]
    tron= TronRun(a)
    tron.timm()
    tron.Print()
    




        


