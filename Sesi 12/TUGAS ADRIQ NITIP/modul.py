kapital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def kapitalCount(text):
  kap = 0

  for char in text:
    if char in kapital:
      kap += 1

  return kap