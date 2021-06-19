try:
    fi = open("file1.txt", "r")
    sen = fi.read()
    fi.close()
except:
    print("File not found")
else:
    str_List = list(sen.split())
    uni = []
    for i in str_List:

        x = i + str(len(i))
        if (x not in uni):
            if (len(uni) == 0):
                uni.append(x)
            else:
                for j in range(len(uni)):
                    if (len(x) <= len(uni[j])):
                        uni.insert(j, x)
                        break
                    elif (j == len(uni) - 1):
                        uni.append(x)
                        break
    print(uni)