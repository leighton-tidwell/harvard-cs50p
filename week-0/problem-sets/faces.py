def main():
  prompt = input("Please enter your smiley or sad face: ")
  print(convert(prompt))

def convert(text: str):
  return text.replace(":(", "🙁").replace(":)", "🙂")

main()

# Test prompts
# Hello :) -> Hello 🙂
# Goodbye :( -> Goodbye 🙁
# Hello :) Goodbye :( -> Hello 🙂 Goodbye 🙁