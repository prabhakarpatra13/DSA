import math as m
#Given an integer A, you have to tell whether it is a prime number or not.
def main():
    inp = int(input())
    count=1
    prime='NO'
    if inp >1:
        for i in range(2,int(m.sqrt(inp)) +1):
            if inp%i ==0:
                count+=1
    if count ==1:
        prime='YES'
    
    print(prime)

    return 0

if __name__ == '__main__':
    main()
