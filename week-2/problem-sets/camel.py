def main():
  variable = input("What is your camel case variable?")

  snake_case = ""
  for c in variable:
    if c.isupper():
      snake_case += "_" + c.lower()
    else:
      snake_case += c

  print(snake_case)


main()