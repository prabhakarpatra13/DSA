def main():
#You are given an integer N you need to print all the Armstrong Numbers between 1 to N.

    ip=int(input())
    for i in range(1,ip+1):
        sum=0
        div=i
        while(div>0):
            sum+= (div%10) * (div%10) * (div%10)
            div//=10
        if sum==i:
            print(i)

    return 0

if __name__ == '__main__':
    main()