#problem-4
def count_multiples(list_a):
    result={i:0 for i in range(1,10)}
    for num in list_a:
        for i in range(1,10):
            if num%i==0:
                result[i]+=1
    return result
if __name__=="__main__":
    list_a=list(map(int,input().split()))
    print(count_multiples(list_a))
