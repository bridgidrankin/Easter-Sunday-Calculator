#!/usr/bin/env python3

def calcEasterSunday(year):
    #perform Easter calculation
    D = year - 1900
    R = D % 19
    P = (7 * R + 1) // 19
    S = (11 * R + 4 - P) % 29
    Q = D // 4
    T = (D + Q + 31 - S) % 7
    result = 25 - S - T
    
    if result > 0:
        month = "April"
        day = str(result)
        date = day + ' ' + month
        return date
    
    elif result <= 0:
        month = "March"
        day = str(31 + result)
        date = day + ' ' + month
        return date

def main():
    
    #display a welcome message
    print("THE EASTER SUNDAY CALCULATOR : ")
    print("==============================")
    print("Enter a negative value to quit")
    print("==============================")
    print()
    
    while True:
        # get input from the user
        year = int(input("Enter year:\t\t"))
        
        if year < 0:
            break
        
        else:
            date = calcEasterSunday(year)
            print()
            print("(Western) Easter Sunday is " + date + ", " + str(year))
            print()
            
    print()
    print("Bye...")
    
if __name__ == "__main__":
    main()
