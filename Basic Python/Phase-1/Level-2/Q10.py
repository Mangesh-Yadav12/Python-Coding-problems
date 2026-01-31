"""Take a month number (1–12) and print the number of days in that month (ignore leap
years)."""

def MonthNumber(month):
    months = {
        1: "Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",
        7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"
    }
    print(months.get(month,"Invaild Month Number"))



MonthNumber(11)
MonthNumber(15)