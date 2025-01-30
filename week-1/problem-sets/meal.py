def main():
    time = input("What time is it? ")
    convertedTime = convert(time)
    
    if 7 <= convertedTime <= 8:
      print("breakfast time")
    elif 12 <= convertedTime <= 13:
      print("lunch time")
    elif 18 <= convertedTime <= 19:
      print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes_to_hours = int(minutes) / 60
    total_time = float(int(hours) + minutes_to_hours)
    return total_time


if __name__ == "__main__":
    main()