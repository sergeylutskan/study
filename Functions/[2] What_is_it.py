# Creates 2 lists: list of even numbers and list of odd

numbers = [2, 5, 7, 7, 8, 4, 1, 6] 
odd = [] #ошибка в том, что создавалось 2 одинаковых объекта с разными именами
#изменяя один объект (массив), автоматически менялся другой
even = []
#объявив 2 различных массива по отдельности программа работает правильно
for number in numbers: 
   if number % 2 == 0: 
       even.append(number) 
   else: 
       odd.append(number)
print(even,odd)
