import pandas as pd
import numpy as np


class DFA():
    def __init__(self, path=None, finals=None):
        if not path:
            self.n_states = 1
            self.transitions = {0: {}}
            self.F = [False]

        else:
            states_matrix = pd.read_csv(path)
            states_matrix.to_numpy()
            self.n_states = states_matrix.size
            for i in range(self.n_states):
                self.transitions[i] = {}
                for j in range(self.n_states):
                    if np.isnan(states_matrix[i, j]):
                        continue
                    else:
                        self.transitions[i][j] = states_matrix[i, j]
            self.F = [i in finals for i in range(self.n_states)]

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

    def process_string(self, string):
        curr = 0
        history = [curr]
        for letter in string:
            if letter in self.transitions[curr]:
                curr = self.transitions[curr][letter]
                history.append(curr)
            else:
                return False, history
        return self.F[curr], history
