def main():
    inf = open("names.txt","r")
    outf = open("namesFlipped.txt","w")
    line = inf.readline()
    while line != "":
        names = line.split()
        outf.write(names[1],names[0][:-1])
        line = inf.readline()

    inf.close

main()
