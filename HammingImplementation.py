str1WT = "((((...))))"
str1MUT = ".(((...)))."
str2WT = "((((...))))"
str2MUT = "(((...))).."
case1WT = ".....(((((.(((..(((((((((....)))))))))..)))))))).."
case1MUT = "......(.((((((..(((((((((....)))))))))..)))))).).."
case2WT = "(((((((((((((............))))))........)))))))...."
case2MUT = "(((((((..((((((..........))))))........)))))))...."

def Hamming(string1, string2):
    HammingNumber = 0
    for i in range(len(string1)):
        print(string1[i], string2[i])
        if string1[i] != string2[i]:
            HammingNumber += 1
        else:
            continue
    return HammingNumber

def basepairlocations(string):
    stringstack = []
    stringtuples = []
    for i in range(len(string)):
        if string[i] == "(":
            stringstack.append(i)
        elif string[i] == ".":
            continue
        elif string[i] == ")":
            openbrackval = stringstack.pop()
            stringtuples.append((openbrackval,i))
    return stringtuples

def basepairdist(string1, string2):
    str1LOT = basepairlocations(string1)
    str2LOT = basepairlocations(string2)
    bpdnum = 0
    print(str1LOT)
    for cur_tuple in str1LOT:
        print(cur_tuple,str2LOT)
        if cur_tuple not in str2LOT:
            bpdnum += 1
    for cur_tuple in str2LOT:
        print(cur_tuple,str2LOT)
        if cur_tuple not in str1LOT:
            bpdnum += 1
    return bpdnum