class StateMachineException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Mealy:
    def __init__(self):
        self.state = 'k0'
        self.vars = {'t': 0, 'r': 0, 'j': 0}

    def set_var(self, name, value):
        self.vars[name] = value

    def cue(self):
        if self.state == 'k0':
            self.state = 'k5'
            return 0
        elif self.state == 'k5':
            self.state = 'k0'
            return 1
        elif self.state == 'k4':
            if self.vars['j'] == 0:
                self.state = 'k3'
                return 7
            raise StateMachineException('unsupported')
        raise StateMachineException('unknown')

    def make(self):
        if self.state == 'k0':
            if self.vars['r'] == 1:
                self.state = 'k0'
                return 2
            elif self.vars['r'] == 0:
                self.state = 'k2'
                return 3
            raise StateMachineException('unsupported')
        elif self.state == 'k6':
            self.state = 'k4'
            return 6
        raise StateMachineException('unknown')

    def share(self):
        if self.state == 'k2':
            self.state = 'k7'
            return 4
        elif self.state == 'k6':
            self.state = 'k1'
            return 5
        raise StateMachineException('unknown')

    def boost(self):
        if self.state == 'k7':
            self.state = 'k1'
            return 8
        elif self.state == 'k1':
            self.state = 'k6'
            return 9
        elif self.state == 'k6':
            self.state = 'k2'
            return 10
        raise StateMachineException('unknown')

    def part_of_loop(self):
        return self.state in {'k0', 'k5', 'k2', 'k7', 'k1', 'k6', 'k4', 'k3'}

    def has_max_in_edges(self):
        in_edges = {
            'k0': 2,
            'k5': 1,
            'k2': 2,
            'k7': 1,
            'k1': 1,
            'k6': 2,
            'k4': 1,
            'k3': 1
        }
        max_edges = max(in_edges.values())
        return in_edges.get(self.state, 0) == max_edges


def main():
    return Mealy()


def test():
    o = main()
    assert o.state == 'k0'
    assert o.cue() == 0
    assert o.state == 'k5'
    assert o.cue() == 1
    assert o.state == 'k0'
    o.set_var('r', 1)
    assert o.make() == 2
    assert o.state == 'k0'
    o.set_var('r', 0)
    assert o.make() == 3
    assert o.state == 'k2'
    assert o.share() == 4
    assert o.state == 'k7'
    assert o.boost() == 8
    assert o.state == 'k1'
    assert o.boost() == 9
    assert o.state == 'k6'
    assert o.make() == 6
    assert o.state == 'k4'
    o.set_var('j', 0)
    assert o.cue() == 7
    assert o.state == 'k3'

    o = main()
    o.set_var('r', 0)
    o.make()
    o.share()
    o.boost()
    o.boost()
    o.boost()
    assert o.state == 'k2'

    o = main()
    o.set_var('r', 0)
    o.make()
    o.share()
    o.boost()
    o.boost()
    o.share()
    assert o.state == 'k1'

    assert o.part_of_loop()
    o.state = 'k3'
    assert o.part_of_loop()

    o.state = 'k0'
    assert o.has_max_in_edges()
    o.state = 'k6'
    assert o.has_max_in_edges()
    o.state = 'k2'
    assert o.has_max_in_edges()
    o.state = 'k5'
    assert not o.has_max_in_edges()
    o.state = 'k7'
    assert not o.has_max_in_edges()
    o.state = 'k1'
    assert not o.has_max_in_edges()
    o.state = 'k4'
    assert not o.has_max_in_edges()
    o.state = 'k3'
    assert not o.has_max_in_edges()

    try:
        o.state = 'k3'
        o.cue()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unknown'

    try:
        o.state = 'k4'
        o.set_var('j', 1)
        o.cue()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'

    try:
        o.state = 'k1'
        o.make()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unknown'

    try:
        o.state = 'k3'
        o.share()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unknown'

    try:
        o.state = 'k4'
        o.boost()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unknown'

    o.state = 'k0'
    o.set_var('r', 2)
    try:
        o.make()
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'


test()