# python3

def parallel_processing(n, m, data):
    output = []
    thrd = [(i,0) for i in range(n)]
    for i in range(m):
        thrd_numb, thrd_time = min(thrd, key=lambda x:x[1])
        output.append((thrd_numb,thrd_time))
        thrd[thrd_numb] = (thrd_numb, thrd_time + data[i])

    return output

def main():
    n = 0
    m = 0
    n, m = map(int,input().split())
    data = list(map(int,input().split()))
    result = parallel_processing(n,m,data)
    
    for i in range(m):
        left = result[i][0]
        right = result[i][1]
        print(left,right)



if __name__ == "__main__":
    main()
