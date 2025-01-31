def main():
  tweet = input("What's the tweet? ")

  sanitize_tweet(tweet)

def sanitize_tweet(tweet: str):
  sanitized = ""
  
  for char in tweet:
    match char.lower():
      case "a" | "e" | "i" | "o" | "u":
        continue
    
    sanitized += char

  print(sanitized)
        


main()