# Originally it was code with mistakes and I have to correct it. 

def mirror(arr): #ошибка заключалась в том, что метод reverse() изменяет исходный массив
    arr = arr + arr[::-1] #один из вариантов использовать срез с шагом -1
    return arr

print(mirror([1,2,3,4,5]))
