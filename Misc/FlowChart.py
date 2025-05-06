#variables
s = 12
p = int(input("p: "))

#functions
def isPrime(p): #function to check if p is prime
    for eachNumber in range(2,p):
        #if p/eachNumber remainder returns a whole number
        if p%eachNumber==0:
            #print("p is not prime")
            return False
    return True

def isEven(p):  #function to check if p is even or odd
    if p%2==0:
        return True
    return False

while True:
    if isEven(p):
        p+=1
        break
    else:
        if isPrime(p):
            if p<s:
                s-=p
                p+=2
            else:
                s-=1
                if s==0:
                    print(p)
                else:
                    p+=2
                    break
        else:
            p+=2
#output p
print(f"P: {p}")

#while True:
    #if p i is even - rhombus is a conditiona;
    #if p%2==0:
        #p=p+1
        #print("p is even")
        #break
    #else:
        #print("p is not even")
        #if p is prime
        #for eachNumber in range(1,p):
            #if p%eachNumber!=0:
                #print("p is not prime")
                #p = p + 2
            #else:
                #print("p is prime")
                #if p is < s
                #if p < s:
                    #print("p is less than s")
                    #s = s - p
                    #p = p + 2
                #else:
                    #print("p is not less than s")
                    #s -= s - 1
                    #if s=0?
                    #if s == 0:
                        #print("s equals 0")
                        #break
                    #else:
                        #print("s does not equal 0")
                        #p = p + 2

#output p
#print(f"P: {p}")