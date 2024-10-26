if __name__ == "__main__":
    num = int(input("enter the number:"))

    units = {0:"zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine"}

    tens = {0:"",10:"ten",20:"twenty",30:"thirty",40:"fourty",
            50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
    teens ={11:"eleven",12:"twelve.",13:"thirteen",14:"fourteen",
            15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    units_place = num % 10
    tens1 = (num // 10) % 10
    tens_place = tens1 * 10
    thou = (num // 1000)% 10
    lakh = (num // 10000)% 10
    crore = (num // 100000) % 10
    hund = (num // 100) % 10
    if (num>=0 and num<10):
        print(units[num])
    if num<0:
        print("enter a valid number")
        exit(1)
    if num % 10 == 0 and num<100:
        print(tens[num])
    if num % 100 == 0:
       print(units[hund],"hundered")
    elif num>=10 and num < 20:
        print(teens[num])
    elif num<100:
        print("{} {}".format(tens[tens_place],units[units_place]))
    elif(num>100 and num <= 999 and num % 100 !=0):
        print(units[hund],"hundered",tens[tens_place],units[units_place])
    elif (num>1000 and num <= 9999  and num % 1000 !=0):
        print(units[thou],"thousand",units[hund], "hundered", tens[tens_place], units[units_place])
    elif (num >= 99999 and num % 1000 !=0):
        print(units[lakh],"lakhs",units[thou],"thousand",units[hund], "hundered", tens[tens_place], units[units_place])
        #ten_thou =
    #elif (num <= 999999 and num % 1000 !=0):
      #  print(units[crore],"crore",units[lakh],"lakhs",units[thou],"thousand",units[hund], "hundered", tens[tens_place], units[units_place])








