from hashlib import md5

#                 Hardcoded password choices
#              00     01        10           11
passList = [ "pass","1234","coolPassword","noPass"]

# Simple digesting function for MD5
def digester(passval):
    m = md5()
    m.update(passval.encode('utf-8'))
    return m.hexdigest()

# This is a trivial, kinda lame looking oracleself.
# What we are doing in here is that, we are getting user hash
# comparing it with our hashes to return something 0,1,2,3 indicating the
# location of true answer. This is required for checking the result and
# using our Grover's search.
def oracle(realHex):
    for i in range(4):
        currHex = digester(passList[i])
        if currHex == realHex:
            return i
