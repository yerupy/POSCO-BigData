import sys

print(sys.argv)


fr = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'w')

for line in fr:
    f2.write(line)

fr.close()
f2.close()