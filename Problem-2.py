#Problem-2.py
def odd_series(a:int)->str:
    result=[]
    for i in range(a):
        result.append(str(2*i+1))
    return ",".join(result)
if __name__=="__main__":
    a=int(input())
    print("Odd series:",odd_series(a))