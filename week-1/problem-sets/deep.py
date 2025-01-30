def main():
  answer = input("What is the answer to the great question of life, the universe, and everything? ").strip().lower().replace("-", " ")
  
  if answer == "42" or answer == "forty two":
    print("Yes")
  else:
    print("No")

main()