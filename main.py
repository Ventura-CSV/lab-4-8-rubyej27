
    ##################################################
    # Comlete your code here
    ##################################################
    
def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def main():
    plist = []
    
def main():
    plist = []
        
    while True:
        begin = int(input('Enter an integer: '))
        end = int(input('Enter an integer: '))
        if begin > 1 and end > begin:
            break
        else:
            print("Invalid Input")
    plist = [num for num in range(begin, end + 1) if is_prime(num)]
    print(plist)
    return plist
if __name__ == '__main__':
    main()
