def isLeapYear(year: int) -> bool:
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    years = [2020, 2021, 2023]
    #results: list[bool] = [print(f"{years[index]} : {isLeapYear(year)}")
    # for index, year in enumerate(years)]
    results = [print(f"{year} is leap year") if isLeapYear() 
    else print(f"{year} is not leap year") for year in years]
    
    # print(f"{year} is a Leap Year" if isLeapYear(year) else f"{year} is not a Leap Year")
    # year: int = 2021
    # print(f"{year} is a Leap Year" if isLeapYear(year) else f"{year} is not a Leap Year")
    # year: int = 2022
    # print(f"{year} is a Leap Year" if isLeapYear(year) else f"{year} is not a Leap Year")

