def end_other(a, b):
  if((b in a) or (a in b)):
    return True
  if((b in a) or (b.swapcase() in a)):
    return True
  if((a in b) or (a.swapcase() in b)):
    return True
  else:
    return False
