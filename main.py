from PyPrimeNumber import *
def main():
    limit_num: int = 100_000
    primeList: int = getEtratrosPrime(limit_num)
    print(primeList)

if __name__=="__main__":
    main()