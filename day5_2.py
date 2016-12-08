from hashlib import md5

#input = "abc"
input = "cxdnnyjw"

i = 0
resultCount = 0
result = 8*['X']

while resultCount < 8:
    currentString = input + str(i)
    currentHash = md5(currentString).hexdigest()
    if currentHash[0:5] == "00000":
        try:
            position = int(currentHash[5])
            if position < 8 and result[position] == 'X':
                result[position] = currentHash[6]
                print result
                resultCount += 1
        except:
            pass 
    i += 1
print "".join(result)
