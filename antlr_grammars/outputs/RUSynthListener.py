# Generated from RUSynth.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RUSynthParser import RUSynthParser
else:
    from RUSynthParser import RUSynthParser

import pymorphy3
import re

morph = pymorphy3.MorphAnalyzer()
pattern = re.compile(r"_[A-Z]{4}")

def get_tags(string):
    string = re.sub(pattern, "", string)
    return string, morph.parse(string)[0].tag

def add_subj(stack, string, tags):
    if "subj" in stack[-1]:
        return
    if tags.case == "nomn":
        stack[-1]["subj"] = (string, tags)
        return
    return

def add_verb(stack, string, tags):
    if "verb" in stack[-1]:
        return
    stack[-1]["verb"] = (string, tags)
    return

def check_clause(stack):
    if all(k in stack[-1] for k in ("subj", "verb")):
        print(f"Subj found - {stack[-1]['subj']}")
        print(f"Verb found - {stack[-1]['verb']}")
        if stack[-1]["verb"][1].tense == "past":
            if stack[-1]["verb"][1].gender == stack[-1]["subj"][1].gender:
                print("Agreement admitted")
                stack.pop()
                return
        if stack[-1]["verb"][1].tense in ("pres", "futr"):
            if stack[-1]["verb"][1].number == stack[-1]["subj"][1].number:
                print("Agreement admitted")
                stack.pop()
                return
        print("Disagreement found")
        stack.pop()
    return


# This class defines a complete listener for a parse tree produced by RUSynthParser.
class RUSynthListener(ParseTreeListener):

    # Enter a parse tree produced by RUSynthParser#sentence.
    def enterSentence(self, ctx:RUSynthParser.SentenceContext):
        pass

    # Exit a parse tree produced by RUSynthParser#sentence.
    def exitSentence(self, ctx:RUSynthParser.SentenceContext):
        pass


    # Enter a parse tree produced by RUSynthParser#clause.
    def enterClause(self, ctx:RUSynthParser.ClauseContext):
        pass

    # Exit a parse tree produced by RUSynthParser#clause.
    def exitClause(self, ctx:RUSynthParser.ClauseContext):
        pass


    # Enter a parse tree produced by RUSynthParser#dep_clause.
    def enterDep_clause(self, ctx:RUSynthParser.Dep_clauseContext):
        pass

    # Exit a parse tree produced by RUSynthParser#dep_clause.
    def exitDep_clause(self, ctx:RUSynthParser.Dep_clauseContext):
        pass


    # Enter a parse tree produced by RUSynthParser#sub_conj.
    def enterSub_conj(self, ctx:RUSynthParser.Sub_conjContext):
        pass

    # Exit a parse tree produced by RUSynthParser#sub_conj.
    def exitSub_conj(self, ctx:RUSynthParser.Sub_conjContext):
        pass


    # Enter a parse tree produced by RUSynthParser#prep_phrase.
    def enterPrep_phrase(self, ctx:RUSynthParser.Prep_phraseContext):
        pass

    # Exit a parse tree produced by RUSynthParser#prep_phrase.
    def exitPrep_phrase(self, ctx:RUSynthParser.Prep_phraseContext):
        pass


    # Enter a parse tree produced by RUSynthParser#adj_phrase.
    def enterAdj_phrase(self, ctx:RUSynthParser.Adj_phraseContext):
        pass

    # Exit a parse tree produced by RUSynthParser#adj_phrase.
    def exitAdj_phrase(self, ctx:RUSynthParser.Adj_phraseContext):
        pass


    # Enter a parse tree produced by RUSynthParser#noun_phrase.
    def enterNoun_phrase(self, ctx:RUSynthParser.Noun_phraseContext):
        pass

    # Exit a parse tree produced by RUSynthParser#noun_phrase.
    def exitNoun_phrase(self, ctx:RUSynthParser.Noun_phraseContext):
        pass


    # Enter a parse tree produced by RUSynthParser#verb_phrase.
    def enterVerb_phrase(self, ctx:RUSynthParser.Verb_phraseContext):
        pass

    # Exit a parse tree produced by RUSynthParser#verb_phrase.
    def exitVerb_phrase(self, ctx:RUSynthParser.Verb_phraseContext):
        pass


    # Enter a parse tree produced by RUSynthParser#grnd_phrase.
    def enterGrnd_phrase(self, ctx:RUSynthParser.Grnd_phraseContext):
        pass

    # Exit a parse tree produced by RUSynthParser#grnd_phrase.
    def exitGrnd_phrase(self, ctx:RUSynthParser.Grnd_phraseContext):
        pass


    # Enter a parse tree produced by RUSynthParser#inf_phrase.
    def enterInf_phrase(self, ctx:RUSynthParser.Inf_phraseContext):
        pass

    # Exit a parse tree produced by RUSynthParser#inf_phrase.
    def exitInf_phrase(self, ctx:RUSynthParser.Inf_phraseContext):
        pass



del RUSynthParser