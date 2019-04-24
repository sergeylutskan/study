# Create a list of invited to party friends

def add_friends(nameOfPerson, listOfFriends): #создаем функцию add_friends от 2 аргументов
   global friends #обозначаем глобальный словарь friends
   friends = {nameOfPerson:listOfFriends} #в словарь по ключу имя добавляем список друзей данного человека

def is_friends(nameOfPerson1, nameOfPerson2):
   global friends #обозначаем глобальный словарь friends
   return nameOfPerson2 in friends[nameOfPerson1] #логическое выражение - проверка наличия имени в словаре по ключу


def print_friends(nameOfPerson):
   global friends #обозначаем глобальный словарь friends
   print(*friends[nameOfPerson].sort()) #выводим на печать сортированный список 


add_friends("Алла", ["Марина", "Иван"])
print(is_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(is_friends("Алла", "Мария"))
