sum = input("Enter the sum: ") # this allows to give result for any number
with open("lecture01/task1.txt") as nfile:
    with open("lecture01/output1.txt", "w") as ofile:
        nlist = nfile.readlines()
        for x in range(0,len(nlist)):
            for y in range(x+1, len(nlist)):
                for z in range(y+1, len(nlist)):
                    a = int(nlist[x].rstrip('\n'))
                    b = int(nlist[y].rstrip('\n'))
                    c = int(nlist[z].rstrip('\n'))
                    if a+b+c == int(sum):
                        ofile.write(f"{a*b*c}\n")