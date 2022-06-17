from ru.vienoulis.service.state import State
from ru.vienoulis.di.conf import current_state
# current_state = State.empty


def set_state(state: State):
    current_state = state


def get_state():
    return current_state
