class DFA():
    def __init__(self, path=None):
        if path:
            pass
        else:
            self.n_states = 1
            self.transitions = {0: {}}
            self.F = [False]

    def add_state(self, final=False):
        self.n_states += 1
        self.transitions[self.n_states - 1] = dict()
        self.F.append(final)

    def set_final(self, state):
        self.F[state] = True

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

    def _next_state(self, current, character):
        return self.transitions[current][character]

    def process_string(self, string):
        curr = 0
        history = [curr]
        for letter in string:
            if letter in self.transitions[curr]:
                curr = self._next_state(curr, letter)
                history.append(curr)
            else:
                return False, history
        return self.F[curr], history
