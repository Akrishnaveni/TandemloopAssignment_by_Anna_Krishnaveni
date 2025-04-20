#Problem-3
def selective_odd_numbers(a:int)->str:
    x=a//2 if a%2==0 else ((a+1)//2)
    result=[]
    for i in range(x):
        result.append(str(2*i+1))
    return ",".join(result)

if __name__=="__main__":
    a=int(input())
    print("selective Odd Numbers:",selective_odd_numbers(a))