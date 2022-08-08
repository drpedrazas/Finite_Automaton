class DFA():
    def __init__(self, path=None):
        if path:
            pass
        else:
            self.transitions = dict()
            self.F = set()

    def add_state(self, new_state, final = False):
        if new_state not in self.transitions:
            self.transitions[new_state] = {}
            if final:
                self.F.add(new_state)
        else:
            pass

    def add_transition(self, current, character, state):
        if current not in self.transitions:
            self.add_state(current)
            if state not in self.transitions:
                self.add_state(state)
                self.transitions[current][character] = state
            else:
                self.transitions[current][character] = state
        else:
            if state not in self.transitions:
                self.add_state(state)
                self.transitions[current][character] = state
            else:
                self.transitions[current][character] = state
