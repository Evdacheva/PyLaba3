from StringFormater import StringFormatter  

string = "hello; it is me, how are you; i am fine 74382"

#Напишите простой класс StringFormatter для форматирования строк со следующим функционалом: 
print(StringFormatter.DelWords(string, 3)) #Удаление всех слов из строки, длина которых меньше n букв
print(StringFormatter.ReplaceNum(string))  #Замена всех цифр в строке на знак «*»
print(StringFormatter.CreateSpace(string)) #Вставка по одному пробелу между всеми символами в строке
print(StringFormatter.SortSize(string)) #Сортировка слов по размеру
print(StringFormatter.SortLex(string)) #сортировка слов в лексикографическом порядке    
