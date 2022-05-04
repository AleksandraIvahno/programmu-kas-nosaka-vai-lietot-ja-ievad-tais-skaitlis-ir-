def numCheck(num):
  # чётное число
  if num % 2 == 0:
    print("Numurs", num, "ir pat")
  # нечётное число
  elif num % 2 != 0:
    print("Numurs", num, "ir nepat")
  
  return

numInput = int(input("Ievadiet numuru: "))
numCheck(numInput)