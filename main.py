str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

if sorted(str1.lower()) == sorted(str2.lower()):
  print("Строки являются анаграммами.")
else:
  print("Строки не являются анаграммами.")
