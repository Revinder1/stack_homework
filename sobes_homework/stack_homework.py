class Stack:
    def __init__(self):
        self.layers = []

    def isEmpty(self):
        return len(self.layers) == 0

    def push(self, layer):
        self.layers.append(layer)

    def pop(self):
        if self.isEmpty():
            return 'Empty stack'
        elif len(self.layers) == 1:
            self.layers.pop()
            return 'Empty stack'
        self.layers.pop()
        return self.layers[-1]

    def peek(self):
        if not self.isEmpty():
            return self.layers[-1]

    def size(self):
        return len(self.layers)


def isBalanced():
    stack = Stack()
    _input = input('Введите последовательность скобок: ')
    for element in _input:
        if element in ["(", "[", "{"]:
            stack.push(element)
        else:
            if stack.isEmpty():
                return 'Не сбалансированно'
            else:
                on_top = stack.peek()
                if (element == ')' and on_top == '(') or (element == ']' and on_top == '[')\
                        or (element == '}' and on_top == '{'):
                    stack.pop()
                else:
                    return 'Не сбалансированно'
    if stack.isEmpty():
        return 'Сбалансированно'
    return 'Не сбалансированно'


if __name__ == '__main__':
    print(isBalanced())
