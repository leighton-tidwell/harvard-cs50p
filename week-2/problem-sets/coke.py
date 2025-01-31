def main():
  owed = 50

  while owed > 0:
    print("Amount Due:", owed)
    
    match int(input("Insert Coin: ")):
      case 25:
        owed -= 25
      case 10:
        owed -= 10
      case 5:
        owed -= 5

  print("Change Owed:", owed * -1)

main()