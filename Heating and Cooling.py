def heatingandcooling():
    Temp = input("Enter the average daily temperatures with spaces between the temperatures: ")
    Temp = Temp.split(" ")
    CoolDays = 0
    HeatingDays = 0
    
    for i in Temp:
        if int(i) > 80 or int(i) < 60:
            if int(i) > 80:
                CoolDayss += int(i) - 80
            else:
                HeatingDays += 60 - int(i) 
    
    print("There are" , CoolDays , "cooling degree days.")
    print("There are" , HeatingDays , "heating degree days")
    
heatingandcooling()
