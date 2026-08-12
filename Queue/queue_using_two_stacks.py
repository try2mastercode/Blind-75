A=[1,2,3,4,5,6,7]
def stackout(A):
    while len(A)>0:
        print(A.pop(),end="-")
def queueusingstack(A):
    print(" ")
    B=[]
    while len(A)>0:
        B.append(A.pop())
    while len(B)>0:
        print(B.pop(),end="-")
print(stackout(A))
A=[1,2,3,4,5,6,7]
print(queueusingstack(A))