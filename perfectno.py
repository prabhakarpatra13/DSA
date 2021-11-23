def main():
    ip=int(input())
    li=[]
    for i in range(ip):
        li.append(int(input()))
    
    for j in li:
        count=0
        for k in range(1,j):
            if j%k==0:
                count+=k
        if count == j:
            print('YES')
        else:
            print('NO')

    return 0

if __name__ == '__main__':
    main()
