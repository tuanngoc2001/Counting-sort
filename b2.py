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







        


