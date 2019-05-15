lehetseges_tld=['com','hu','co.uk']

def is_email(e):
    if "@" not in e:
        return False
    if "." not in e:
        return False
    kukac_idx=e.find("@")
    pont_idx=e.rfind(".")
    if kukac_idx>=pont_idx:
        return False

    fel=e[:kukac_idx]

    tld=e[pont_idx+1:]

    if tld not in lehetseges_tld:
        e2=e[:]
        e2=e2[:pont_idx]
        pont_idx=e2.rfind(".")

        tld=e[pont_idx+1:]
        if tld not in lehetseges_tld:
            return False

    kisz=e[kukac_idx+1:pont_idx]

    if not(fel[0].isalpha() or fel[0].isnumeric()):
        return False
    if not(fel[len(fel)-1].isalpha() or fel[len(fel)-1].isnumeric()):
        return False

    fel2=fel[1:len(fel)-1]

    lehetseges_fel=["-","_","."]
    dupla_pont=".."

    if dupla_pont in fel2:
        return False
    if not(fel2.isalpha() or fel2.isnumeric()):
        for c in fel2:
            if not(c.isalpha() or c.isnumeric() or (c in lehetseges_fel)):
                return False

    if not (kisz[0].isalpha() or kisz[0].isnumeric()):
        return False
    if not (kisz[len(kisz)-1].isalpha() or kisz[len(kisz)-1].isnumeric()):
        return False

    kisz2 = kisz[1:len(kisz)-1]

    lehetseges_kisz=["-","."]
    dupla_pont=".."

    if dupla_pont in kisz2:
        return False
    if not (kisz2.isalpha() or kisz2.isnumeric()):
        for c in kisz2:
            if not (c.isalpha() or c.isnumeric() or (c in lehetseges_kisz)):
                return False

    return True

def main():
    e=input()
    while(e!="0"):
        if is_email(e):
            print("Ez egy email cim")
        else:
            print("Ez nem egy email cim")
        e=input()

main()