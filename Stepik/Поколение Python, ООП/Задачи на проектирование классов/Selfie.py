import copy


class Selfie:
    def __init__(self):
        self._states = []

    def save_state(self):
        self._states.append(copy.deepcopy(self.__dict__))

    def recover_state(self, index):
        if 0 <= index < len(self._states):
            new_obj = Selfie()
            new_obj._states = copy.deepcopy(self._states)
            new_obj.__dict__ = copy.deepcopy(self._states[index])
            return new_obj
        return self

    def n_states(self):
        return len(self._states)
