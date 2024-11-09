def test():
    m = 0
    for i in range(1,10):
        print(i)
        for j in range(1,i+1):
            print(j)
            for k in range(1,j+1):
                print(k)
                m = m + 1
    print(m)

test()