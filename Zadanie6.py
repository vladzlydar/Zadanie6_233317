obecnySymbol = ""
global wskaznikPozycji
firstsO = "*:+-^"
firstsC = "0123456789"
firstsL = "0123456789"
firstsLPrim = "0123456789e"
firstsR = "0123456789"
firstsRPrim = ".e"
firstsP = "0123456789("
firstsWPrim = "*:+-^e"
firstsW = "0123456789("
firstsZ = "0123456789(e"
firstsS = "0123456789("

def obecnywFirst(firsty):
    global wskaznikPozycji, obecnySymbol
    if czyZakonczono():
        return False
    if obecnySymbol in firsty:
        return True
    return False

def czyZakonczono():
    global wskaznikPozycji, obecnySymbol
    if wskaznikPozycji == len(ciag)-1:
        return True
    return False

def produkcjaO():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaO")
    if obecnywFirst(firstsO):
        if zaladujSymbol():
            return True
    return False

def produkcjaC():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaC")
    if obecnywFirst(firstsC):
        if zaladujSymbol():
            return True
    return False

def produkcjaLPrim():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaLPrim")
    if obecnywFirst(firstsLPrim):
        if produkcjaL():
            return True
    elif "e" in firstsLPrim:
        print("Epsilon reached")
        return True
    else:
        return False

def produkcjaL():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaL")
    if obecnywFirst(firstsL):
        if produkcjaC():
            if produkcjaLPrim():
                return True
    return False

def produkcjaRPrim():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaRprim")
    if obecnywFirst(firstsRPrim):
        if obecnySymbol == ".":
            zaladujSymbol()
            if produkcjaL():
                return True
    elif "e" in firstsRPrim:
        print("Epsilon")
        return True
    return False

def produkcjaR():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaR")
    if obecnywFirst(firstsR):
        if produkcjaL():
            if produkcjaRPrim():
                return True
    return False

def produkcjaP():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaP")
    if obecnywFirst(firstsP):
        if obecnySymbol == "(":
            zaladujSymbol()
            if produkcjaW():
                if obecnySymbol == ")":
                    zaladujSymbol()
                    return True
        elif (produkcjaR()):
            return True
    return False

def produkcjaWPrim():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaWPrim")
    if obecnywFirst(firstsWPrim):
        if produkcjaO():
            if produkcjaW():
                return True
    elif "e" in firstsWPrim:
        print("Epsilon")
        return True
    return False

def produkcjaW():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaW")
    if obecnywFirst(firstsW):
        if produkcjaP():
            if produkcjaWPrim():
                return True
    return False


def produkcjaZ():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaZ")
    if obecnywFirst(firstsZ):
        if produkcjaW():
            if obecnySymbol == ";":
                zaladujSymbol()
                if produkcjaZ():
                    return True
    elif "e" in firstsZ:
        print("Epsilon")
        return True
    return False

def produkcjaS():
    global wskaznikPozycji, obecnySymbol
    print("ProdukcjaS")
    if obecnywFirst(firstsS):
        if produkcjaW():
            if obecnySymbol == ";":
                zaladujSymbol()
                if produkcjaZ():
                    return True
    return False

def zaladujSymbol():
    global wskaznikPozycji,obecnySymbol
    if wskaznikPozycji + 1 < len(ciag):
        wskaznikPozycji+=1
        obecnySymbol = ciag[wskaznikPozycji]
        if obecnySymbol == "$" and czyZakonczono():
            print("Koniec ciagu!")
        else:
            print("Obecny symbol %s" % obecnySymbol)
    return True

ciag = input("Prosze podac wyrazenie matematyczne do analizy: ")
ciag +="$"
wskaznikPozycji = 0
obecnySymbol = ciag[wskaznikPozycji]
print("Obecny symbol %s" %obecnySymbol)
print(produkcjaS())
