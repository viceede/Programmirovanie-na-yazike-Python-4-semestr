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
            else:
                raise StateMachineException('unsupported')
        else:
            raise StateMachineException('unknown')

    def make(self):
        if self.state == 'k0':
            if self.vars['r'] == 1:
                self.state = 'k0'
                return 2
            elif self.vars['r'] == 0:
                self.state = 'k2'
                return 3
            else:
                raise StateMachineException('unsupported')
        elif self.state == 'k6':
            self.state = 'k4'
            return 6
        else:
            raise StateMachineException('unknown')

    def share(self):
        if self.state == 'k2':
            self.state = 'k7'
            return 4
        elif self.state == 'k6':
            self.state = 'k1'
            return 5
        else:
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
        else:
            raise StateMachineException('unknown')

    def part_of_loop(self):
        # States that are part of loops: k0, k5, k0-k2-k7-k1-k6-k4-k3
        return self.state in {'k0', 'k5', 'k2', 'k7', 'k1', 'k6', 'k4', 'k3'}

    def has_max_in_edges(self):
        # Count in-edges for each state based on the graph
        in_edges = {
            'k0': 2,  # from k5 and make transition
            'k5': 1,  # from k0
            'k2': 2,  # from k0 and k6
            'k7': 1,  # from k2
            'k1': 1,  # from k7
            'k6': 2,  # from k1 and boost
            'k4': 1,  # from k6
            'k3': 1   # from k4
        }
        max_edges = max(in_edges.values())
        return in_edges.get(self.state, 0) == max_edges


def main():
    return Mealy()


def test():
    o = main()

    # Test initial state
    assert o.state == 'k0'

    # Test cue from k0 to k5
    assert o.cue() == 0
    assert o.state == 'k5'

    # Test cue from k5 back to k0
    assert o.cue() == 1
    assert o.state == 'k0'

    # Test make from k0 with r=1
    o.set_var('r', 1)
    assert o.make() == 2
    assert o.state == 'k0'

    # Test make from k0 with r=0
    o.set_var('r', 0)
    assert o.make() == 3
    assert o.state == 'k2'

    # Test share from k2 to k7
    assert o.share() == 4
    assert o.state == 'k7'

    # Test boost from k7 to k1
    assert o.boost() == 8
    assert o.state == 'k1'

    # Test boost from k1 to k6
    assert o.boost() == 9
    assert o.state == 'k6'

    # Test make from k6 to k4
    assert o.make() == 6
    assert o.state == 'k4'

    # Test cue from k4 with j=0 to k3
    o.set_var('j', 0)
    assert o.cue() == 7
    assert o.state == 'k3'

    # Reset and test alternative paths
    o = main()
    o.set_var('r', 0)
    o.make()  # k0 -> k2
    o.share()  # k2 -> k7
    o.boost()  # k7 -> k1
    o.boost()  # k1 -> k6
    o.share()  # k6 -> k1
    assert o.state == 'k1'

    # Test boost from k6 to k2
    o = main()
    o.set_var('r', 0)
    o.make()  # k0 -> k2
    o.share()  # k2 -> k7
    o.boost()  # k7 -> k1
    o.boost()  # k1 -> k6
    o.boost()  # k6 -> k2
    assert o.state == 'k2'

    # Test part_of_loop
    assert o.part_of_loop()
    o.state = 'k3'
    assert o.part_of_loop()

    # Test has_max_in_edges
    o.state = 'k0'
    assert o.has_max_in_edges()
    o.state = 'k6'
    assert o.has_max_in_edges()
    o.state = 'k2'
    assert o.has_max_in_edges()
    o.state = 'k5'
    assert not o.has_max_in_edges()

    # Test error handling
    try:
        o.state = 'k3'
        o.cue()  # Should raise unknown
        assert False
    except StateMachineException as e:
        assert str(e) == 'unknown'

    try:
        o.state = 'k4'
        o.set_var('j', 1)
        o.cue()  # Should raise unsupported
        assert False
    except StateMachineException as e:
        assert str(e) == 'unsupported'


test()