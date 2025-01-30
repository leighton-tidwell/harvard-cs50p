def main():
  equation = input("Please input your expression, the format is x y z: ")
  x, y, z = equation.split(" ")

  match y:
    case "+":
      print(f"{int(x) + int(z):.1f}")
    case "-":
      print(f"{int(x) - int(z):.1f}")
    case "*":
      print(f"{int(x) * int(z):.1f}")
    case "/":
      print(f"{int(x) / int(z):.1f}")
      
      

main()