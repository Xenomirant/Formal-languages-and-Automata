from typing import Optional, Sequence, Mapping, \
    Iterable, TypeAlias
import icecream as ic

PARSED: TypeAlias = (bool, int)

'''
We'll use the following grammar for RegExp

<expr> ::= <term> | <term> '|' <expr>
<term> ::= <factor> | <factor> <term>
<factor> ::= <atom> | <atom> <meta-char>
<atom> ::= <char> | '('<expr>')'
<char> ::= <any-char-except-meta>
<meta-char> ::= '?' | '*' | '+'

'''

class NonDetAutomaton(object):

    def __init__(self, regex: str) -> None:

        # Let -1 represent the final state
        # let "#" represent 0-transition symbol


        self.regex: str = regex
        self.matrix: dict[int, dict[str, set[int]]] = {}
        self.__state_count: int = 0
        self.stack = []

        # probably refactorize to dict of functions
        self.__meta = ["*", "?", "+"]

    @property
    def length(self):
        return len(self.regex)

    def add_state(self) -> (int, int):
        """
        Add state and return the previous one
        :return: int, previous state id,
                 int, added state id
        """
        self.matrix[self.__state_count] = {}
        self.__state_count += 1
        return self.__state_count - 1,  self.__state_count

    def add_transition(self, from_state, to_state, symbol) -> None:
        """
        add transition from one state to another
        :param from_state:
        :param to_state:
        :param symbol:
        :return:
        """
        if symbol not in self.matrix[from_state]:
            self.matrix[from_state][symbol] = set()
        self.matrix[from_state][symbol].add(to_state)

    def lookup(self, cur_pos: int, lex: str) -> PARSED:
        res = self.regex[cur_pos:cur_pos + len(lex)] == lex
        return res, cur_pos + len(lex) * res

    def expr(self, cur_pos: int) -> PARSED:

        save = cur_pos
        if self.length == cur_pos:
            return False, cur_pos
        res_term, cur_pos = self.term(cur_pos)
        if not res_term:
            return False, save
        if self.length == cur_pos:
            return True, cur_pos
        save = cur_pos
        res_lex, cur_pos = self.lookup(cur_pos, "|")
        if not res_lex:
            return False, save
        res_expr, cur_pos = self.expr(cur_pos)
        return True, cur_pos

    def term(self, cur_pos: int) -> PARSED:







    # def split_by_or(self):
    #     lstack = []
    #     flag: int = 0
    #
    #     for i in range(len(self.regex)):
    #         if self.regex[i] == "|":
    #             self.stack.append(self.regex[:i])
    #             flag = i+1
    #
    #         # check bracket balance at the first step
    #         if self.regex[i] == "(":
    #             lstack.append(self.regex[i])
    #         if self.regex[i] == ")":
    #             try:
    #                 lstack.pop()
    #             except IndexError:
    #                 print("Check bracket balance!")
    #
    #         if flag != 0:
    #             self.stack.append(self.regex[flag:])



    def compile(self):

        if len(self.regex) == 0:
            print("Your automata is already perfect. No need to proceed.")

        pass




def main():

    m = NonDetAutomaton("a*b+C|c|C?")
    m.compile()


if __name__ == '__main__':
    main()
