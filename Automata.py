from typing import Optional, Sequence, Mapping, \
    Iterable, TypeAlias
from icecream import ic
import re
from warnings import warn
from dataclasses import dataclass
from functools import partial

PARSED: TypeAlias = (bool, int)

'''
We'll use the following grammar for RegExp

A ::= B `|` A | B
B ::= C B | C
C := (A)|(A)+|(A)*| a | a+ | a*

'''


@dataclass
class State(int):

    def __init__(self, number: int) -> None:

        self.isTerminatingState = False
        self.name = number
        self.Transitions = {}

    @property
    def __repr__(self) -> str:
        return str(self.name)

    def __setitem__(self, key, value):
        self.Transitions[key] = value
        return None

    def __getitem__(self, item):
        return self.Transitions[item]


class NonDetAutomaton(object):

    def __init__(self, regex: str) -> None:

        # let "ε" represent 0-transition symbol
        self.zero = "ε"

        self.regex: str = regex
        self.matrix: dict[State, dict[str, set[State]]] = {}
        self.__state_count: int = 0
        self.stack = []
        self.token = "[A-Za-z0-9_]"
        self.lookup_re = partial(self.lookup_re, re_lex=self.token)

        self.__meta = {"*": self.star,
                       "+": self.plus
                       }

    @property
    def length(self):
        return len(self.regex)

    def new_state(self) -> (int, int):
        """
        Add state and return the previous one
        :return: int, previous state id,
                 int, added state id
        """
        # self.matrix[self.__state_count] = {}
        self.__state_count += 1
        return self.__state_count

    def star(self, cur_state: State, added_state: State) -> State:
        cur_state[self.zero] = added_state.name
        pass

    def plus(self):
        pass

    def cat(self):
        pass

    def A(self, cur_pos) -> (bool, int):

        if cur_pos == self.length:
            return False, cur_pos
        res_b, cur_pos = self.B(cur_pos)
        if not res_b:
            return False, cur_pos
        if self.length == cur_pos:
            return True, cur_pos
        save = cur_pos
        check, cur_pos = self.lookup(cur_pos, "|")
        if not check:
            return False, save
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
        ic(f"bracket start. {cur_pos}")
        check, cur_pos = self.lookup(cur_pos, "(")
        ic(f"bracket end. {cur_pos}")
        ic(self.regex[cur_pos])
        if not check:
            res_symbol, cur_pos = self.lookup_re(cur_pos)
            if not res_symbol:
                return False, cur_pos
            if cur_pos == self.length:
                return True, cur_pos
            ######
            rec, cur_pos = self.lookup(cur_pos, "+")
            if rec:
                pass
            rec, cur_pos = self.lookup(cur_pos, "*")
            if rec:
                pass
            ######
            return True, cur_pos

        save = cur_pos
        res_a, cur_pos = self.A(cur_pos)
        if res_a:
            check, cur_pos = self.lookup(cur_pos, ")")
            if check:
                if cur_pos == self.length:
                    return True, cur_pos
                #####
                rec, cur_pos = self.lookup(cur_pos, "+")
                if rec:
                    pass
                rec, cur_pos = self.lookup(cur_pos, "*")
                if rec:
                    pass
                #####
                return True, cur_pos
        return False, save

    def lookup(self, cur_pos: int, lex: str) -> PARSED:
        res = self.regex[cur_pos:cur_pos + len(lex)] == lex
        ic(res, cur_pos + len(lex)*res)
        return res, cur_pos + len(lex) * res

    def lookup_re(self, cur_pos, re_lex):
        res = re.match(re_lex, self.regex[cur_pos:])
        if res is None or res.pos != 0:
            return False, cur_pos
        ic(bool(res), cur_pos + res.span()[1])
        return bool(res), cur_pos + res.span()[1]

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

        res, cur_pos = self.A(0)
        if cur_pos != self.length:
            raise ValueError("Your string doesn't satisfy the grammar. Check again.")

        return None


def main():
    regex = "a*b+C|c+|C+"
    print(len(regex))
    m = NonDetAutomaton(regex)
    m.compile()


if __name__ == '__main__':
    main()
