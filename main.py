def are_anagrams(str1, str2):
  return sorted(str1.lower()) == sorted(str2.lower())

str1 = input("Введите первую строку:" )
str2 = input("Введите вторую строкуЖ" )

if are_anagrams(str1 , str2):
  print("Строки являются анаграммами.")
else:
  print("Строки не являются анаграммами.")
