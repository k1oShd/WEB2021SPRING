def not_string(str):
  if(str[0:3]=="not"):
    return str
  else:
    str = "not " + str
    return str
