def hatvanyozo(szam):
    hatvany=1
    while(szam**hatvany<1000000):
        hatvany+=1

    print("{}^{}={}".format(szam,hatvany-1,szam**(hatvany-1)))
    return szam**(hatvany-1)

def main():
    szam=5
    print(hatvanyozo(2))

main()