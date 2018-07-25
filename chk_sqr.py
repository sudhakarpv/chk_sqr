# chk_sqr
def main():
    pass
    n=list(map(int,input().split()))
    k=n[0]
    m=n[1]
    o=int(k*m)
    if (o==(m**2)):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
