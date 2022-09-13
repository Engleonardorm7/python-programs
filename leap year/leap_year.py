def is_leap(year: int)->bool:
    leap = False
    
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False     
        
            if year%400==0:
                leap=True
    return leap

if __name__=="__main__":

    year = int(input("Type a year"))

    if is_leap(year):
        print("Is a Leap Year")
    else:
        print("Is not a Leap Year")