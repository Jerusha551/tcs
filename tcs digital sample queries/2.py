n=int(input())
if n<0:
    print("Wrong Input")
else:
    sn=n*n
    l=[]
    r=sn%10
    if r==n:
        print("Correct Number")
    else:
        print("Incorrect Number")