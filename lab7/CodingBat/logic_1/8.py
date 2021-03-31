def alarm_clock(day, vacation):
  if(vacation==True):
    if(day>0 and day<6):
      return "10:00"
    if(day==0 or day==6):
      return "off"
  else:
    if(day==0 or day==6):
      return "10:00"
    else:
      return "7:00"
