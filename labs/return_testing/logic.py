# TODO: Írj egy függvényt:
# bemenet: list[str]
# kimenet: (list[str], dict)
# A dict legyen stats: {"before": ..., "after": ...}

lista = [" Egy ", "kettő", " Három", ""]

def keep_nonempty(lines):
  after = []
  before = len(lines)
  for i in lines:
    clean = i.strip()
    if clean == "":
      continue
    else:
      after.append(clean)
  return after, {"before": before, "after": len(after)}