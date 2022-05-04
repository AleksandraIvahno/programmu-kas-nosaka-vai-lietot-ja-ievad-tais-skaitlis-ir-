def numCheck(num):
  # чётное число
  if num % 2 == 0:
    print("Pāra skaitlis:")
  # нечётное число
  elif num % 2 != 0:
    print("Nepāra skaitlis")
  
  return

numInput = int(input("Ievadiet numuru: "))
numCheck(numInput)