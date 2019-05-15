def elofordulas(a,b):
    db=0
    while(True):
        idx=a.find(b)
        if idx >=0:
            db+=1
        else:
            break
        a=a[idx+1:]

    return db
def main():
    a="hello szia hello hello szia"
    b="hello"
    print(elofordulas(a,b))

main()
