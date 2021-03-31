def front3(str):
  if(len(str)<3):
    front = str[0:]
    return front*3
  else:
    front = str[0:3]
    return front*3
