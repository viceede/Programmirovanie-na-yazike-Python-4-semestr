class StateMachineException(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'k5'
        self.vars = {}
        self.transitions = {
            'k5': {
                'cue': lambda: ('k0', 'E3') if self.vars.get('t') == 1 else ('k5', 'E6')
            },
            'k0': {
                'make': lambda: ('k2', 'E1') if self.vars.get('r') == 1 else ('k7', 'E1')
            },
            'k2': {
                'share': lambda: ('k5', 'E6')
            },
            'k7': {
                'boost': lambda: ('k1', 'E0')
            },
            'k1': {
                'boost': lambda: ('k6', 'E0')
            },
            'k6': {
                'boost': lambda: ('k4', 'E2'),
                'make': lambda: ('k6', 'E1'),
                'share': lambda: ('k4', 'E5')
            },
            'k4': {
                'cue': lambda: ('k3', 'E7') if self.vars.get('j') == 0 else ('k5', 'E2')
            },
            'k3': {}
        }

        self.in_edges = {
            'k0': ['k5'],
            'k1': ['k7'],
            'k2': ['k0'],
            'k3': ['k4'],
            'k4': ['k6'],
            'k5': ['k2', 'k4', 'k5'],
            'k6': ['k1', 'k6'],
            'k7': ['k0']
        }

    def set_var(self, name, value):
        self.vars[name] = value

    def __getattr__(self, item):
        if item in ['cue', 'make', 'boost', 'share']:
            if item in self.transitions.get(self.state, {}):
                def transition_fn():
                    try:
                        next_state, output = self.transitions[self.state][item]()
                        self.state = next_state
                        return output
                    except KeyError:
                        raise StateMachineException('unsupported')
                return transition_fn
            raise StateMachineException('unsupported')
        raise StateMachineException('unknown')

    def part_of_loop(self):
        visited = set()
        rec_stack = set()

        return self._dfs_loop(self.state, visited, rec_stack)

    def _dfs_loop(self, state, visited, rec_stack):
        if state in rec_stack:
            return True
        if state in visited:
            return False

        visited.add(state)
        rec_stack.add(state)

        for next_state in self._get_next_states(state):
            if self._dfs_loop(next_state, visited, rec_stack):
                return True

        rec_stack.remove(state)
        return False

    def _get_next_states(self, state):
        results = []
        for method, trans in self.transitions.get(state, {}).items():
            try:
                next_state, _ = trans()
                results.append(next_state)
            except (StateMachineException, KeyError):
                continue
        return results

    def has_max_in_edges(self):
        max_count = max(len(v) for v in self.in_edges.values())
        return len(self.in_edges.get(self.state, [])) == max_count


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
        obj.put()
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
    assert obj.part_of_loop() is True
    assert obj.cue() == 'E7'
    assert obj.part_of_loop() is True

    try:
        obj.skew()
    except StateMachineException as e:
        assert str(e) == 'unknown'
