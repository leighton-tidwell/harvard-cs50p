def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    
    found_number = False
    for char in s[2:]:
        if char.isnumeric() and found_number == False:
            found_number = True
            if char == "0":
                return False
        
        if char.isalpha() and found_number:
            return False
        
    
    if 2 <= len(s) <= 6 and s.isalnum() and s[:1].isalpha():
        return True

        

main()