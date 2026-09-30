import ctypes


class CommonList:
    def __init__(self):
        self._length = 0
        self._capacity = 1
        self._array = self.make_array(self._capacity)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if not 0 <= index < self._length:
            raise IndexError("Out of range")
        return self._array[index]

    def append_to_common_list(self,item):
        if self._length == self._capacity:
            self._resize(2*self._capacity)

        self._array[self._length] = item
        self._length += 1

    def _resize(self,new_capacity):
        #создание нового списка
        new_array = self.make_array(new_capacity)
        #Копирование старых элементов в новый список
        for i in range(self._length):
            new_array[i] = self._array[i]

        self._array = new_array
        self._capacity = new_capacity

    def make_array(self, capacity):

        return (capacity * ctypes.py_object)()

    def __repr__(self):
        items = [str(self._array[i]) for i in range(self._length)]
        return "#" + ' & '.join(items) + "#"


my_common_list = CommonList()
my_common_list.append_to_common_list("Hi dady")
my_common_list.append_to_common_list("Hi momy")
print(my_common_list)

print()
# эксперимент с id сравнить наш лист с обычным списком

print(iter(my_common_list)) # Iter: <iterator object at 0x00000183F06F7A60> -> В нашей коллекции не пишет list_iterator, а значит что это кастомный итератор.

print(id(my_common_list)) # ID: 1666186234768

print()

my_common_list.append_to_common_list("1")

print(iter(my_common_list))
print(id(my_common_list))

print("ID у нашей коллекции при добавлении не изменяется")

print()
print()

print("Для примера вот обычный лист:")

lst = ["Hi dady", "Hi momy"]

print(iter(lst)) # Iter: <list_iterator object at 0x000001C36E8F7A60>
print(id(lst)) # ID: 1938885166080

print()

lst.append("1")

print(iter(lst)) # <list_iterator object at 0x00000201A59F7A60>
print(id(lst)) # ID: 2206096934016

# my_common_list.remove(1)
# print(my_common_list) - выводит ошибку - AttributeError: 'CommonList' object has no attribute 'remove'
print()

print("Вывод: наша коллекция очень похожа на лист с точки зрения итератора (так как метод интерации не меняеться), \n"
      "но если смотреть на функционал и ID (он не изменяется) при добавление обьекта id не изменяеться, \n"
      "а значит что используется 1 ячейка памяти")

print()

print("Пояснение: У нашей коллекции выводится с помощью метода iter выводит выводит: # Iter: <iterator object at 0x00000183F06F7A60> \n"
      "Потому что мы создали собственную коллекцию (лист без листа) в котором логика самого итератора (перебора) другая. \n"
      "А также мы с помощью функции id выводили ячейку которую занимает наша коллекция, \n"
      "И при изменении ячейка не изменяеться как у обычного листа. \n"
      "При попытке применить методы списков от python (такие как remove(), append(), pop() и тд.) выходит ошибка"
      "- AttributeError: 'CommonList' object has no attribute 'remove'")