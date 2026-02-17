import argparse
from cleaner.core import cleaner
import logging

logging.basicConfig(level=logging.DEBUG)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("source")
  parser.add_argument("destination")
  parser.add_argument("--uppercase", action="store_true")
  args = parser.parse_args()
  logging.info(f"Source: {args.source}")
  logging.info(f"Destination: {args.destination}")
  if args.uppercase:
    logging.info("Uppercase mode enabled")
  else:
    logging.info("Uppercase mode not enabled")
  
  try:
    with open(args.source, "r") as f:
      lines = f.read().splitlines()
      cleaned_lines, stats = cleaner(lines)
      
      with open(args.destination, "w") as c:
        for line in cleaned_lines:
          line_to_write = line.upper() if args.uppercase else line
          c.write(line_to_write + "\n")
            
      logging.info(f"Before: {stats["before"]}")
      logging.info(f"After: {stats["after"]}")
      logging.info(f"Output written to: {args.destination}")
  except FileNotFoundError:
    logging.error(f"{args.source} not exists")
    return
    
if __name__ == "__main__":
  main()