n = int(input("Enter nth iteration"))
put = ["," for i in range(n*2)].insert(n,0)
put[0] = n
used = []
while put[0] != 0:
    for i in range(len(put)):
        
