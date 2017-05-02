# Testing out Try Catch

try:
    f = open('ex15_sample.txt')
    s = f.readlines()
    print s[2]
    #raise Exception('Test Exception')

except Exception as e:
    print "ERROR:", e
