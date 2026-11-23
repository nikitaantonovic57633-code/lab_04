class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        """Возвращает верхний элемент. Если стек пуст, вызывает IndexError"""
        if not self.items:
            raise IndexError("Стек пуст")
        return self.items[-1]

    def pop(self):
        """Извлекает и возвращает верхний элемент. Если стек пуст, вызывает IndexError"""
        if not self.items:
            raise IndexError("Стек пуст")
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)