
def swapFileData():
    file1=input("enter file1: ")
    file2=input("enter file2: ")

    with open(file1,"r") as A:
        data1=A.read()
    
    with open(file2,"r") as B:
        data2=B.read()

    with open(file1,"w") as A:
        A.write(data2)

    with open(file2,"w") as B:
        B.write(data1)

swapFileData()
