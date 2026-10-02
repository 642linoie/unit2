def spaces (N, Y, T):
    count_spaces=0
    for i in range(N):
        if Y[i] =="C" and T[i]=="C":
            count_spaces += 1
    print (count_spaces)
spaces(5,"C.CCC", "CC.CC")
