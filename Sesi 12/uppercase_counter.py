def count_uppercase(text):
  count = 0

  for char in text:
    if char.isupper():
      count += 1

  return count