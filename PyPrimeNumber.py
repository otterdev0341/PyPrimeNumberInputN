def getEtratrosPrime(limit_num: int):
    #Define list for collect result
    PrimeNumber: int = []

    #Base case to prevent problem
    if limit_num == 1:
        PrimeNumber.append(1)
    else:
        for eachNumber in range(1, limit_num + 1):
            slug: str = getPrimeSlug(eachNumber)
            match slug:
                case "two":
                    PrimeNumber.append(2)
                case "three":
                    PrimeNumber.append(3)
                    slug = "two"
                case "five":
                    PrimeNumber.append(5)
                    slug = "two"
                case "seven":
                    PrimeNumber.append(7)
                    slug = "two"
                case _:
                    innerSlug: bool = False
                    for pn in PrimeNumber:
                        if eachNumber % pn == 0 and pn != 1:
                            innerSlug = True
                            break
                    if innerSlug == False and PrimeNumber.count(eachNumber) == 0:
                        PrimeNumber.append(eachNumber)
    # Remove 1 from list
    PrimeNumber.pop(0)
    return PrimeNumber
#---------------------------------------------
def getPrimeSlug(input_num: int):
    primeSlug: str = ""
    if input_num == 2:
        primeSlug = "two"
    elif input_num == 3:
        primeSlug = "three"
    elif input_num == 5:
        primeSlug = "five"
    elif input_num == 7:
        primeSlug = "seven"
    return primeSlug