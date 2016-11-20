# coding=utf-8
f1=open("tabliczkamnozenia.txt","wb")
for i in range (1,11):
    for j in range (1,11):
        print "%3i" % (i*j),
        f1.write("%3i" % (i*j),)
    print "\n"
    f1.write("\n")