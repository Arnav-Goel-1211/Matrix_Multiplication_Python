while True:
    print("\n1.) Two Different Matrix")
    print("2.) Square Matrix \n")
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        m = int(input("Enter M:"))
        n = int(input("Enter N:"))
        p = int(input("Enter P:"))
        print("\n Enter A Matrix \n")
        d1 = {}
        for i in range(1, m + 1):
            d1["mn{0}".format(i)] = []
            for j in range(1, n + 1):
                a = int(input("Enter a[" + str(i) + str(j) + "] Element:"))
                d1["mn{0}".format(i)].append(a)
        print("\n Enter B Matrix \n")
        d2 = {}
        for i in range(1, n + 1):
            d2["np{0}".format(i)] = []
            for j in range(1, p + 1):
                a = int(input("Enter b[" + str(i) + str(j) + "] Element:"))
                d2["np{0}".format(i)].append(a)

        d3 = {}
        for i in range(1, m + 1):
            a = 0
            d3["mp{0}".format(i)] = []
            for j in range(1, p + 1):
                a = 0
                for k in range(1, n + 1):
                    a = a + d1["mn{0}".format(i)][k - 1] * d2["np{0}".format(k)][j - 1]
                d3["mp{0}".format(i)].append(a)
        for i in range(m):
            a=''
            for j in range(p):
                a=a+(str(d3["mp{0}".format(i+1)][j])+' ')
            print(a)
    if choice==2:
        o=int(input("Enter Order:"))

        d2 = {}
        for i in range(1, o + 1):
            d2["np{0}".format(i)] = []
            for j in range(1, o + 1):
                a = int(input("Enter a[" + str(i) + str(j) + "] Element:"))
                d2["np{0}".format(i)].append(a)

        d3 = {}
        for i in range(1, o + 1):
            a = 0
            d3["mp{0}".format(i)] = []
            for j in range(1, o + 1):
                a = 0
                for k in range(1, o + 1):
                    a = a + d2["np{0}".format(i)][k - 1] * d2["np{0}".format(k)][j - 1]
                d3["mp{0}".format(i)].append(a)
        for i in range(o):
            a=''
            for j in range(o):
                a=a+(str(d3["mp{0}".format(i+1)][j])+' ')
            print(a)
    else:
        print("\n Wrong Input! \n Try Again\n")