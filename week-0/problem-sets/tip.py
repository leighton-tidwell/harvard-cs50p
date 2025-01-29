def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    num = float(d.replace("$",""))
    return round(num, 2)


def percent_to_float(p):
    num = int(p.replace("%",""))
    return round(num / 100, 2)


main()

# test prompts:
# $50.00 & 15% -> Leave $7.50
# $100.00 & 18% -> Leave $18.00
# $15.00 & 25% -> Leave $3.75