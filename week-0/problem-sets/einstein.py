def main():
  mass = int(input("Please enter the mass (kg): "))
  print(convert(mass))

def convert(mass):
  # E = mc^2
  return mass * 300000000 ** 2

main()

# Test prompts:
# 1 -> 90000000000000000
# 14 -> 1260000000000000000
# 50 -> 4500000000000000000