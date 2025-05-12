class StateMachineException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Mealy:
    def __init__(self):
        self.state = 'A'
        self.vars = {}

    def set_var(self, name, value):
        self.vars[name] = value

    def skew(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'E':
            self.state = 'F'
            return 5
        if self.state == 'F':
            self.state = 'G'
            return 8
        raise StateMachineException('skew')

    def widen(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'E':
            self.state = 'A'
            return 7
        if self.state == 'G':
            self.state = 'H'
            return 10
        if self.state == 'H':
            self.state = 'E'
            return 11
        raise StateMachineException('widen')

    def scrub(self):
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'C'
            return 6
        if self.state == 'F':
            self.state = 'D'
            return 9
        if self.state == 'B':
            self.state = 'G'
            return 2
        raise StateMachineException('scrub')

    def part_of_loop(self):
        return self.state in {'C', 'D', 'E', 'F', 'H'}

    def has_max_in_edges(self):
        in_edges = {
            'A': 1, 'B': 2, 'C': 2, 'D': 2,
            'E': 3, 'F': 1, 'G': 2, 'H': 1
        }
        max_edges = max(in_edges.values())
        return in_edges.get(self.state, 0) == max_edges


def main():
    return Mealy()


def test():
    o = main()

    # Тесты для set_var и vars
    o.set_var('x', 10)
    assert o.vars['x'] == 10

    o.set_var('flag', True)
    assert o.vars['flag'] is True

    # Перезапись переменной
    o.set_var('x', 20)
    assert o.vars['x'] == 20

    # Проверка других переменных
    assert o.vars['flag'] is True

    # Проверка отсутствия переменной
    assert 'y' not in o.vars

    # Оригинальные тесты автомата
    try:
        o.widen()
    except StateMachineException:
        pass
    try:
        o.scrub()
    except StateMachineException:
        pass

    assert o.skew() == 0
    try:
        o.skew()
    except StateMachineException:
        pass
    assert o.scrub() == 2

    try:
        o.skew()
    except StateMachineException:
        pass
    assert o.widen() == 10

    assert o.widen() == 11
    assert o.widen() == 7
    assert o.skew() == 0
    assert o.widen() == 1

    try:
        o.skew()
    except StateMachineException:
        pass
    try:
        o.widen()
    except StateMachineException:
        pass
    assert o.scrub() == 3

    assert o.scrub() == 4
    assert o.scrub() == 6
    assert o.scrub() == 3

    try:
        o.skew()
    except StateMachineException:
        pass
    try:
        o.widen()
    except StateMachineException:
        pass
    assert o.scrub() == 4
    assert o.skew() == 5

    assert o.scrub() == 9

    try:
        o.widen()
    except StateMachineException:
        pass
    assert o.scrub() == 4
    assert o.scrub() == 6
    assert o.scrub() == 3
    assert o.scrub() == 4
    assert o.skew() == 5
    assert o.skew() == 8
    assert o.widen() == 10

    assert o.part_of_loop()
    o.state = 'A'
    assert not o.part_of_loop()

    o.state = 'E'
    assert o.has_max_in_edges()
    o.state = 'A'
    assert not o.has_max_in_edges()


test()