class StateMachineException(Exception):
    def __init__(self, message):
        super().__init__(message)


class StateMachineException(Exception):
    def __init__(self, message):
        super().__init__(message)


class StateMachine:
    def __init__(self):
        self.state = 'k5'
        self.vars = {}

    def set_var(self, name, value):
        self.vars[name] = value

    def cue(self):
        if self.state == 'k5':
            if self.vars.get('t') == 1:
                self.state = 'k0'
                return 'E3'
            else:
                return 'E6'
        if self.state == 'k4':
            if self.vars.get('j') == 0:
                self.state = 'k3'
                return 'E7'
            else:
                self.state = 'k5'
                return 'E2'
        raise StateMachineException('unsupported')

    def make(self):
        if self.state == 'k0':
            if self.vars.get('r') == 1:
                self.state = 'k2'
                return 'E1'
            else:
                self.state = 'k7'
                return 'E1'
        if self.state == 'k6':
            return 'E1'
        raise StateMachineException('unsupported')

    def boost(self):
        if self.state == 'k7':
            self.state = 'k1'
            return 'E0'
        if self.state == 'k1':
            self.state = 'k6'
            return 'E0'
        if self.state == 'k6':
            self.state = 'k4'
            return 'E2'
        if self.state == 'k3':
            self.state = 'k5'
            return 'E4'
        raise StateMachineException('unsupported')

    def share(self):
        if self.state == 'k2':
            self.state = 'k5'
            return 'E6'
        if self.state == 'k6':
            self.state = 'k4'
            return 'E5'
        raise StateMachineException('unsupported')

    def skew(self):
        raise StateMachineException('unknown')

    def part_of_loop(self):
        loop_states = {'k5', 'k0', 'k2', 'k6', 'k4'}
        return self.state in loop_states

    def has_max_in_edges(self):
        in_edges = {
            'k0': ['k5'],
            'k1': ['k7'],
            'k2': ['k0'],
            'k3': ['k4'],
            'k4': ['k6'],
            'k5': ['k2', 'k4', 'k5'],
            'k6': ['k1', 'k6'],
            'k7': ['k0'],
        }
        max_edges = max(len(v) for v in in_edges.values())
        return len(in_edges.get(self.state, [])) == max_edges


def main():
    return StateMachine()


def test():
    obj = main()
    obj.set_var('t', 1)
    obj.set_var('j', 0)
    obj.set_var('r', 1)

    assert obj.part_of_loop() is True
    assert obj.has_max_in_edges() is True
    assert obj.cue() == 'E3'

    try:
        obj.skew()
    except StateMachineException as e:
        assert str(e) == 'unknown'

    assert obj.has_max_in_edges() is False
    assert obj.make() == 'E1'
    try:
        obj.cue()
    except StateMachineException as e:
        assert str(e) == 'unsupported'

    assert obj.share() == 'E6'
    assert obj.boost() == 'E0'
    try:
        obj.skew()
    except StateMachineException as e:
        assert str(e) == 'unknown'

    assert obj.part_of_loop() is True
    assert obj.has_max_in_edges() is False
    assert obj.boost() == 'E0'
    assert obj.share() == 'E5'
    assert obj.cue() == 'E7'
    assert obj.part_of_loop() is True

    try:
        obj.skew()
    except StateMachineException as e:
        assert str(e) == 'unknown'


test()

