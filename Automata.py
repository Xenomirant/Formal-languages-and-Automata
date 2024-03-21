from typing import Optional, TypeAlias
from icecream import ic
import re
from warnings import warn
from functools import partial
from collections import defaultdict
from copy import deepcopy

PARSED: TypeAlias = (bool, int)

'''

We'll use the following grammar for RegExp

A ::= B `|` A | B
B ::= C B | C
C := (A)|(A)+|(A)*| a | a+ | a*

'''


class State:

    def __init__(self, number: int) -> None:
        self.isStartingState: bool = False
        self.isTerminatingState: bool = False
        self.id: int = number
        self.Transitions: dict[str, set] = defaultdict(set)

    def __repr__(self) -> str:
        return str(self.id)

    def __str__(self) -> str:
        return str(self.id)

    def __setitem__(self, key, value):
        self.Transitions[key].add(value)
        return None

    def __getitem__(self, item):
        return self.Transitions[item]


class NonDetAutomaton(object):

    def __init__(self, regex: str) -> None:

        # let "ε" represent 0-transition symbol
        self.zero = "ε"

        self.regex: str = regex
        self.matrix: dict[State, dict[str, set[State]]] = {}
        self.__state_count: int = -1
        self.states = []
        # stack for brackets
        self.bracket_stack = []
        # stack for start and term states on all levels
        self.level_stack = []
        self.cur_state: Optional[State] = None

        self.token = "[A-Za-z0-9_]"
        self.lookup_re = partial(self.lookup_re, re_lex=self.token)

        # self.__meta = {"*": self.star,
        #                "+": self.plus
        #                }

    @property
    def length(self):
        return len(self.regex)

    def new_state(self) -> State:
        """
        Create and return a new state with unique id
        :return: State
        """
        self.__state_count += 1

        state = State(self.__state_count)
        self.states.append(state)

        return state

    def star(self, symbol: Optional[str] = None, next_state: Optional[State] = None, bracket: bool = False) -> None:

        if next_state is None:
            next_state = self.new_state()

        # if bracket -- work with first and last states inside the bracket
        if bracket:
            self.cur_state[self.zero] = self.level_stack[-1][0]
            self.cur_state = self.level_stack[-1][0]
            self.cur_state[self.zero] = next_state
            self.cur_state = next_state
            return None

        # if just one symbol -- work with preceding state and transitions
        self.cur_state[self.zero] = next_state
        self.cur_state = next_state
        self.cur_state[symbol] = self.cur_state

        next_state = self.new_state()
        self.cur_state[self.zero] = next_state
        self.cur_state = next_state
        return None

    def plus(self, symbol: Optional[str] = None, next_state: Optional[State] = None, bracket: bool = False) -> None:

        if next_state is None:
            next_state = self.new_state()

        # if bracket -- add zero transition to first bracket state and zero transition to next state outside bracket
        if bracket:
            self.cur_state[self.zero] = self.level_stack[-1][0]
            self.cur_state[self.zero] = next_state
            self.cur_state = next_state
            return None

        # if just one symbol -- work with preceding state and transitions
        self.cur_state[symbol] = next_state
        self.cur_state = next_state
        self.cur_state[symbol] = self.cur_state

        next_state = self.new_state()
        self.cur_state[self.zero] = next_state
        self.cur_state = next_state
        return None

    def cat(self, symbol: str, next_state: Optional[State] = None) -> None:

        if next_state is None:
            next_state = self.new_state()

        self.cur_state[symbol] = next_state
        self.cur_state = next_state

        return None

    def A(self, cur_pos) -> (bool, int):

        if cur_pos == self.length:
            return False, cur_pos
        res_b, cur_pos = self.B(cur_pos)
        if not res_b:
            return False, cur_pos
        if self.length == cur_pos:
            self.cur_state[self.zero] = self.level_stack[-1][1]
            return True, cur_pos
        check, cur_pos = self.lookup(cur_pos, "|")
        if not check:
            return True, cur_pos
        # add transition to top final state in stack with zero symbol
        self.cur_state[self.zero] = self.level_stack[-1][1]
        self.cur_state = self.level_stack[-1][0]

        res_a, cur_pos = self.A(cur_pos)
        return True, cur_pos

    def B(self, cur_pos) -> (bool, int):

        if cur_pos == self.length:
            return False, cur_pos
        res_c, cur_pos = self.C(cur_pos)
        if not res_c:
            return False, cur_pos
        if cur_pos == self.length:
            return True, cur_pos
        res_b, cur_pos = self.B(cur_pos)
        return True, cur_pos

    def C(self, cur_pos) -> (bool, int):

        if cur_pos == self.length:
            return False, cur_pos
        # ic(f"bracket start. {cur_pos}")
        check, cur_pos = self.lookup(cur_pos, "(")
        # ic(cur_pos, self.regex[cur_pos])
        if not check:
            res_symbol, cur_pos, symbol = self.lookup_re(cur_pos)
            if not res_symbol:
                return False, cur_pos
            if cur_pos == self.length:
                # if EOS -- cat last symbol
                self.cat(symbol)
                return True, cur_pos

            rec, cur_pos = self.lookup(cur_pos, "+")
            if rec:
                self.plus(symbol=symbol)
                return True, cur_pos

            rec, cur_pos = self.lookup(cur_pos, "*")
            if rec:
                self.star(symbol=symbol)
                return True, cur_pos

            self.cat(symbol)
            return True, cur_pos

        save = cur_pos
        # create low-level start and end states
        self.create_edge_states()
        self.cur_state[self.zero] = self.level_stack[-1][0]
        self.cur_state = self.level_stack[-1][0]
        # ic(f"Start A processing. cur_pos - {cur_pos}")
        res_a, cur_pos = self.A(cur_pos)
        # ic(f"A processed. cur_pos - {cur_pos}, cur_sym - {self.regex[cur_pos]}, res - {res_a}")
        if res_a:
            check, cur_pos = self.lookup(cur_pos, ")")
            if check:
                if cur_pos == self.length:
                    self.cat(self.zero, self.level_stack[-1][1])
                    self.level_stack.pop()
                    return True, cur_pos

                rec, cur_pos = self.lookup(cur_pos, "+")
                if rec:
                    self.plus(bracket=True)
                rec, cur_pos = self.lookup(cur_pos, "*")
                if rec:
                    self.star(bracket=True)
                # pop from level-stack and go to upper level
                self.cat(self.zero, self.level_stack[-1][1])
                self.level_stack.pop()
                return True, cur_pos
        return False, save

    def lookup(self, cur_pos: int, lex: str) -> PARSED:
        res = self.regex[cur_pos:cur_pos + len(lex)] == lex
        # ic(res, cur_pos + len(lex) * res, lex)
        return res, cur_pos + len(lex) * res

    def lookup_re(self, cur_pos, re_lex):
        res = re.match(re_lex, self.regex[cur_pos:])
        if res is None or res.pos != 0:
            return False, cur_pos, None
        # ic(bool(res), res.group())

        return bool(res), cur_pos + res.span()[1], res.group()

    def create_edge_states(self, first=False):

        start = self.new_state()
        if first:
            start.isStartingState = True

        end = self.new_state()
        if first:
            end.isTerminatingState = True

        self.level_stack.append((start, end))

        return start

    def compile(self):

        if self.length == 0:
            warn("Your automata is already perfect. No need to proceed.")
            return None

        if self.zero in self.regex:
            raise ValueError("Control character in string. Can't proceed")

        # check bracket balance at the first step
        lstack = []
        for i in range(self.length):

            if self.regex[i] == "(":
                lstack.append(self.regex[i])
            if self.regex[i] == ")":
                try:
                    lstack.pop()
                except IndexError:
                    print("Check bracket balance!")

        start = self.create_edge_states(first=True)
        self.cur_state = start
        res, cur_pos = self.A(0)
        if cur_pos != self.length:
            ic(cur_pos, self.length)
            raise ValueError("Your string doesn't satisfy the grammar. Check again.")

        return None


class DetFinAutomaton(object):

    def __init__(self, nfa: list[State]) -> None:

        self.NFA = deepcopy(nfa)
        self.zero = "ε"
        self.DFA = deepcopy(self.NFA)
        self.flag = False

        return None

    @staticmethod
    def merge_dicts(dict_a, dict_b):

        for (key, val) in dict_b.items():
            if a_vals := dict_a.get(key):
                dict_a[key] = a_vals | val
            else:
                dict_a[key] = val

        return dict_a

    def remove_zero_transitions(self, cur_state: State) -> None:

        save = cur_state

        if self.zero in cur_state.Transitions:
            for state in cur_state.Transitions[self.zero]:
                self.remove_zero_transitions(cur_state=state)
                save.isTerminatingState = state.isTerminatingState
                save.Transitions = self.merge_dicts(save.Transitions, state.Transitions)
                state.Transitions.pop(self.zero, 0)
            save.Transitions.pop(self.zero, 0)
            self.DFA[save.id] = save

        return None

    @staticmethod
    def add_reachable(state: State, reachable: set, stack: list) -> set[int]:

        reachable.add(state.id)
        for symbol, value in state.Transitions.items():
            for item in value:
                if item.id not in reachable:
                    stack.append(item)

        return reachable

    # do later
    def optimize(self):
        pass

    def to_dfa(self, debug: bool = False):

        # remove zero transitions
        for state in self.NFA:
            self.remove_zero_transitions(state)

        if debug:
            for state in self.DFA:
                ic("DFA", state, state.Transitions, state.isStartingState, state.isTerminatingState)

        reachable = set()
        stack = [self.DFA[0]]
        while stack:
            item = stack.pop()
            reachable = self.add_reachable(item, reachable, stack)

        self.DFA = [self.DFA[i] for i in range(len(self.DFA)) if i in reachable]
        self.flag = True
        if debug:
            for state in self.DFA:
                ic("New DFA", state, state.Transitions, state.isStartingState, state.isTerminatingState)

        return None

    def parse(self, string: str) -> bool:

        if not self.flag:
            raise Exception("Not transformed to DFA yet!")

        cur = self.DFA[0]

        for pos in range(len(string)):
            if string[pos] not in cur.Transitions:
                raise SyntaxError("Not a valid string")

            cur = list(cur.Transitions[string[pos]])[0]

        if len(string)-1 == pos:
            if cur.isTerminatingState:
                return True


def main(*, regex: str = "a*b+C|c+", string: str = None, show: bool = True):

    # interesting case = "a|a*b+C|c+"
    m = NonDetAutomaton(regex)
    m.compile()
    for state in m.states:
        ic("NFA", state, state.Transitions, state.isStartingState, state.isTerminatingState)

    dfa = DetFinAutomaton(nfa=m.states)
    dfa.to_dfa(debug=True)

    if show:
        ic(dfa.parse(string=string))

    return

if __name__ == '__main__':
    main(string="ccc")
