import logging
logging.basicConfig(level=logging.INFO)

def cleaner(x):
  try: 
    outputLines = []
    inputLines = x
    for i in inputLines:
      clean = i.strip()
      if clean == "" or clean.startswith("#"):
        continue
      else:
        outputLines.append(clean)
    stats = {"before": len(x), "after": len(outputLines)}
    return outputLines, stats
  except Exception as e:
    logging.info("Error: ", e)
    return [], {"before": 0, "after": 0}