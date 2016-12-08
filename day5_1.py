from hashlib import md5

#input = "abc"
input = "cxdnnyjw"

i = 0
result = 0
while result < 8:
    currentString = input + str(i)
    currentHash = md5(currentString).hexdigest()
    if currentHash[0:5] == "00000":
        print currentHash[5],
        result += 1
    i += 1
