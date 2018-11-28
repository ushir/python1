

def longmatch(s):
    longstr = ""
    rev_s = s[::-1]
    lenofs = len(s)
    print(s)
    print(rev_s)

    for i in range(lenofs):
        endofs = lenofs - i
        for j in range(endofs):
            if (rev_s[j] == s[i]):               
                if (s[i:lenofs-j] == rev_s[j:endofs]):
                    if (len(s[i:lenofs-j]) > len(longstr)):   
                        #if (((lenofs-j) -i) > 1):
                            longstr = s[i:lenofs-j]
                        
    return (longstr)


print ("final:", longmatch("abacdfgdcaba"))
