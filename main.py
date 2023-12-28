from PyPrimeNumber import *

#info : for limit_num = 100_000 code=0 in 4.535 seconds
#info : for limit_num = 200_000 code=0 in 15.834 seconds
#info : for limit_num = 300_000 code=0 in 32.743 seconds
#info : for limit_num = 800_000 code=0 in 198.453 seconds

def main():
    limit_num: int = 250
    primeList: int = getEtratrosPrime(limit_num)
    
    #write to file
    try:
        result_file: open = open('result.txt','w')
        
        for x in primeList:
            result_file.write("{}\n".format(x))
        result_file.close()
        
    except IOError:
        print("File no allow to write!")


if __name__=="__main__":
    main()