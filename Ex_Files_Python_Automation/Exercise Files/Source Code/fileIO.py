f = open('inputFile.txt', 'r')
passFiles = open('PassFiles.txt', 'w')
failFile = open('FailFile.txt', 'w')
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFiles.write(line) 
    else:
        failFile.write(line)
f.close()
passFiles.close()
failFile.close()