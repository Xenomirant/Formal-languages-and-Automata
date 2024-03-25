# Generated from RUSynth.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


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

def serializedATN():
    return [
        4,1,14,190,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,5,0,23,8,0,10,0,12,0,26,9,0,1,
        0,1,0,1,0,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,3,0,39,8,0,1,1,
        3,1,42,8,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,1,5,1,53,8,
        1,10,1,12,1,56,9,1,1,1,3,1,59,8,1,3,1,61,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,69,8,2,1,3,1,3,1,4,1,4,1,4,1,4,3,4,77,8,4,1,5,1,5,1,5,3,
        5,82,8,5,1,5,1,5,3,5,86,8,5,1,5,1,5,1,5,3,5,91,8,5,1,5,1,5,1,5,1,
        5,5,5,97,8,5,10,5,12,5,100,9,5,1,6,1,6,1,6,1,6,1,6,3,6,107,8,6,1,
        6,1,6,3,6,111,8,6,1,6,1,6,3,6,115,8,6,1,6,1,6,1,6,1,6,1,6,5,6,122,
        8,6,10,6,12,6,125,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,143,8,7,1,7,1,7,3,7,147,8,7,1,7,1,7,1,
        7,3,7,152,8,7,1,7,3,7,155,8,7,1,7,1,7,5,7,159,8,7,10,7,12,7,162,
        9,7,1,8,1,8,1,8,1,8,1,8,3,8,169,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,179,8,9,1,9,1,9,1,9,1,9,5,9,185,8,9,10,9,12,9,188,9,9,1,
        9,0,4,10,12,14,18,10,0,2,4,6,8,10,12,14,16,18,0,1,2,0,6,6,10,10,
        220,0,38,1,0,0,0,2,60,1,0,0,0,4,68,1,0,0,0,6,70,1,0,0,0,8,76,1,0,
        0,0,10,90,1,0,0,0,12,110,1,0,0,0,14,142,1,0,0,0,16,168,1,0,0,0,18,
        178,1,0,0,0,20,24,3,2,1,0,21,23,5,6,0,0,22,21,1,0,0,0,23,26,1,0,
        0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,
        3,2,1,0,28,39,1,0,0,0,29,30,5,6,0,0,30,32,3,2,1,0,31,29,1,0,0,0,
        32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,36,1,0,0,0,35,33,1,
        0,0,0,36,39,3,2,1,0,37,39,3,2,1,0,38,20,1,0,0,0,38,33,1,0,0,0,38,
        37,1,0,0,0,39,1,1,0,0,0,40,42,3,16,8,0,41,40,1,0,0,0,41,42,1,0,0,
        0,42,46,1,0,0,0,43,45,3,12,6,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,
        1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,61,3,14,7,0,
        50,54,3,14,7,0,51,53,3,12,6,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,
        1,0,0,0,54,55,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,57,59,3,16,8,0,
        58,57,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,41,1,0,0,0,60,50,1,
        0,0,0,61,3,1,0,0,0,62,63,3,6,3,0,63,64,3,2,1,0,64,69,1,0,0,0,65,
        66,3,6,3,0,66,67,3,14,7,0,67,69,1,0,0,0,68,62,1,0,0,0,68,65,1,0,
        0,0,69,5,1,0,0,0,70,71,7,0,0,0,71,7,1,0,0,0,72,73,5,13,0,0,73,77,
        3,12,6,0,74,75,5,13,0,0,75,77,5,10,0,0,76,72,1,0,0,0,76,74,1,0,0,
        0,77,9,1,0,0,0,78,79,6,5,-1,0,79,81,5,11,0,0,80,82,5,4,0,0,81,80,
        1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,91,5,10,0,0,84,86,5,4,0,0,
        85,84,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,5,11,0,0,88,91,5,
        10,0,0,89,91,5,10,0,0,90,78,1,0,0,0,90,85,1,0,0,0,90,89,1,0,0,0,
        91,98,1,0,0,0,92,93,10,5,0,0,93,97,3,8,4,0,94,95,10,4,0,0,95,97,
        3,4,2,0,96,92,1,0,0,0,96,94,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,
        98,99,1,0,0,0,99,11,1,0,0,0,100,98,1,0,0,0,101,102,6,6,-1,0,102,
        103,3,10,5,0,103,104,3,12,6,5,104,111,1,0,0,0,105,107,5,4,0,0,106,
        105,1,0,0,0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,5,5,0,0,109,
        111,6,6,-1,0,110,101,1,0,0,0,110,106,1,0,0,0,111,123,1,0,0,0,112,
        114,10,3,0,0,113,115,5,2,0,0,114,113,1,0,0,0,114,115,1,0,0,0,115,
        116,1,0,0,0,116,122,3,12,6,4,117,118,10,4,0,0,118,122,3,10,5,0,119,
        120,10,2,0,0,120,122,3,4,2,0,121,112,1,0,0,0,121,117,1,0,0,0,121,
        119,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,
        13,1,0,0,0,125,123,1,0,0,0,126,127,6,7,-1,0,127,128,5,4,0,0,128,
        143,3,14,7,8,129,143,5,3,0,0,130,131,3,8,4,0,131,132,3,14,7,6,132,
        143,1,0,0,0,133,134,3,18,9,0,134,135,3,14,7,5,135,143,1,0,0,0,136,
        137,5,8,0,0,137,143,3,18,9,0,138,139,5,7,0,0,139,143,5,11,0,0,140,
        141,5,7,0,0,141,143,6,7,-1,0,142,126,1,0,0,0,142,129,1,0,0,0,142,
        130,1,0,0,0,142,133,1,0,0,0,142,136,1,0,0,0,142,138,1,0,0,0,142,
        140,1,0,0,0,143,160,1,0,0,0,144,146,10,9,0,0,145,147,5,11,0,0,146,
        145,1,0,0,0,146,147,1,0,0,0,147,151,1,0,0,0,148,152,3,12,6,0,149,
        152,3,8,4,0,150,152,3,4,2,0,151,148,1,0,0,0,151,149,1,0,0,0,151,
        150,1,0,0,0,152,154,1,0,0,0,153,155,5,11,0,0,154,153,1,0,0,0,154,
        155,1,0,0,0,155,159,1,0,0,0,156,157,10,4,0,0,157,159,3,18,9,0,158,
        144,1,0,0,0,158,156,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,
        161,1,0,0,0,161,15,1,0,0,0,162,160,1,0,0,0,163,164,5,12,0,0,164,
        169,3,12,6,0,165,166,5,12,0,0,166,169,3,8,4,0,167,169,5,12,0,0,168,
        163,1,0,0,0,168,165,1,0,0,0,168,167,1,0,0,0,169,17,1,0,0,0,170,171,
        6,9,-1,0,171,172,3,12,6,0,172,173,3,18,9,5,173,179,1,0,0,0,174,175,
        3,8,4,0,175,176,3,18,9,4,176,179,1,0,0,0,177,179,5,9,0,0,178,170,
        1,0,0,0,178,174,1,0,0,0,178,177,1,0,0,0,179,186,1,0,0,0,180,181,
        10,3,0,0,181,185,3,8,4,0,182,183,10,2,0,0,183,185,3,12,6,0,184,180,
        1,0,0,0,184,182,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,
        1,0,0,0,187,19,1,0,0,0,188,186,1,0,0,0,30,24,33,38,41,46,54,58,60,
        68,76,81,85,90,96,98,106,110,114,121,123,142,146,151,154,158,160,
        168,178,184,186
    ]

class RUSynthParser ( Parser ):

    grammarFileName = "RUSynth.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'\\u0438_CONJ'", "'\\u043D\\u0435\\u0442_PRED'", 
                     "'\\u043D\\u0435_PRCL'" ]

    symbolicNames = [ "<INVALID>", "WS", "AND_CONJ", "NEG_V", "NEG_N", "NOUN", 
                      "CONJ", "VERB", "PRED", "INF", "ADJ", "ADV", "GRND", 
                      "PREP", "UNK" ]

    RULE_sentence = 0
    RULE_clause = 1
    RULE_dep_clause = 2
    RULE_sub_conj = 3
    RULE_prep_phrase = 4
    RULE_adj_phrase = 5
    RULE_noun_phrase = 6
    RULE_verb_phrase = 7
    RULE_grnd_phrase = 8
    RULE_inf_phrase = 9

    ruleNames =  [ "sentence", "clause", "dep_clause", "sub_conj", "prep_phrase", 
                   "adj_phrase", "noun_phrase", "verb_phrase", "grnd_phrase", 
                   "inf_phrase" ]

    EOF = Token.EOF
    WS=1
    AND_CONJ=2
    NEG_V=3
    NEG_N=4
    NOUN=5
    CONJ=6
    VERB=7
    PRED=8
    INF=9
    ADJ=10
    ADV=11
    GRND=12
    PREP=13
    UNK=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    stack = [{}]



    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RUSynthParser.ClauseContext)
            else:
                return self.getTypedRuleContext(RUSynthParser.ClauseContext,i)


        def CONJ(self, i:int=None):
            if i is None:
                return self.getTokens(RUSynthParser.CONJ)
            else:
                return self.getToken(RUSynthParser.CONJ, i)

        def getRuleIndex(self):
            return RUSynthParser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)




    def sentence(self):

        localctx = RUSynthParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.clause()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 21
                    self.match(RUSynthParser.CONJ)
                    self.state = 26
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 27
                self.clause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 29
                    self.match(RUSynthParser.CONJ)
                    self.state = 30
                    self.clause()
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 36
                self.clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.clause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verb_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Verb_phraseContext,0)


        def grnd_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Grnd_phraseContext,0)


        def noun_phrase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RUSynthParser.Noun_phraseContext)
            else:
                return self.getTypedRuleContext(RUSynthParser.Noun_phraseContext,i)


        def getRuleIndex(self):
            return RUSynthParser.RULE_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClause" ):
                listener.enterClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClause" ):
                listener.exitClause(self)




    def clause(self):

        localctx = RUSynthParser.ClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_clause)
        self._la = 0 # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 40
                    self.grnd_phrase()


                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 43
                        self.noun_phrase(0) 
                    self.state = 48
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 49
                self.verb_phrase(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.verb_phrase(0)
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 51
                        self.noun_phrase(0) 
                    self.state = 56
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                self.state = 58
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 57
                    self.grnd_phrase()


                pass


            self._ctx.stop = self._input.LT(-1)
            check_clause(self.stack)
            self.stack.append({})
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dep_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sub_conj(self):
            return self.getTypedRuleContext(RUSynthParser.Sub_conjContext,0)


        def clause(self):
            return self.getTypedRuleContext(RUSynthParser.ClauseContext,0)


        def verb_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Verb_phraseContext,0)


        def getRuleIndex(self):
            return RUSynthParser.RULE_dep_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDep_clause" ):
                listener.enterDep_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDep_clause" ):
                listener.exitDep_clause(self)




    def dep_clause(self):

        localctx = RUSynthParser.Dep_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dep_clause)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.sub_conj()
                self.state = 63
                self.clause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.sub_conj()
                self.state = 66
                self.verb_phrase(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_conjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONJ(self):
            return self.getToken(RUSynthParser.CONJ, 0)

        def ADJ(self):
            return self.getToken(RUSynthParser.ADJ, 0)

        def getRuleIndex(self):
            return RUSynthParser.RULE_sub_conj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub_conj" ):
                listener.enterSub_conj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub_conj" ):
                listener.exitSub_conj(self)




    def sub_conj(self):

        localctx = RUSynthParser.Sub_conjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sub_conj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not(_la==6 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prep_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREP(self):
            return self.getToken(RUSynthParser.PREP, 0)

        def noun_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Noun_phraseContext,0)


        def ADJ(self):
            return self.getToken(RUSynthParser.ADJ, 0)

        def getRuleIndex(self):
            return RUSynthParser.RULE_prep_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrep_phrase" ):
                listener.enterPrep_phrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrep_phrase" ):
                listener.exitPrep_phrase(self)




    def prep_phrase(self):

        localctx = RUSynthParser.Prep_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_prep_phrase)
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(RUSynthParser.PREP)
                self.state = 73
                self.noun_phrase(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(RUSynthParser.PREP)
                self.state = 75
                self.match(RUSynthParser.ADJ)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Adj_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADV(self):
            return self.getToken(RUSynthParser.ADV, 0)

        def ADJ(self):
            return self.getToken(RUSynthParser.ADJ, 0)

        def NEG_N(self):
            return self.getToken(RUSynthParser.NEG_N, 0)

        def adj_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Adj_phraseContext,0)


        def prep_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Prep_phraseContext,0)


        def dep_clause(self):
            return self.getTypedRuleContext(RUSynthParser.Dep_clauseContext,0)


        def getRuleIndex(self):
            return RUSynthParser.RULE_adj_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdj_phrase" ):
                listener.enterAdj_phrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdj_phrase" ):
                listener.exitAdj_phrase(self)



    def adj_phrase(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RUSynthParser.Adj_phraseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_adj_phrase, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(RUSynthParser.ADV)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 80
                    self.match(RUSynthParser.NEG_N)


                self.state = 83
                self.match(RUSynthParser.ADJ)
                pass

            elif la_ == 2:
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 84
                    self.match(RUSynthParser.NEG_N)


                self.state = 87
                self.match(RUSynthParser.ADV)
                self.state = 88
                self.match(RUSynthParser.ADJ)
                pass

            elif la_ == 3:
                self.state = 89
                self.match(RUSynthParser.ADJ)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 96
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = RUSynthParser.Adj_phraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_adj_phrase)
                        self.state = 92
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 93
                        self.prep_phrase()
                        pass

                    elif la_ == 2:
                        localctx = RUSynthParser.Adj_phraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_adj_phrase)
                        self.state = 94
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 95
                        self.dep_clause()
                        pass

             
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Noun_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NOUN = None # Token

        def adj_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Adj_phraseContext,0)


        def noun_phrase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RUSynthParser.Noun_phraseContext)
            else:
                return self.getTypedRuleContext(RUSynthParser.Noun_phraseContext,i)


        def NOUN(self):
            return self.getToken(RUSynthParser.NOUN, 0)

        def NEG_N(self):
            return self.getToken(RUSynthParser.NEG_N, 0)

        def AND_CONJ(self):
            return self.getToken(RUSynthParser.AND_CONJ, 0)

        def dep_clause(self):
            return self.getTypedRuleContext(RUSynthParser.Dep_clauseContext,0)


        def getRuleIndex(self):
            return RUSynthParser.RULE_noun_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoun_phrase" ):
                listener.enterNoun_phrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoun_phrase" ):
                listener.exitNoun_phrase(self)



    def noun_phrase(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RUSynthParser.Noun_phraseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_noun_phrase, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 102
                self.adj_phrase(0)
                self.state = 103
                self.noun_phrase(5)
                pass

            elif la_ == 2:
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 105
                    self.match(RUSynthParser.NEG_N)


                self.state = 108
                localctx._NOUN = self.match(RUSynthParser.NOUN)
                add_subj(self.stack, *get_tags((None if localctx._NOUN is None else localctx._NOUN.text)))
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 121
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = RUSynthParser.Noun_phraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_noun_phrase)
                        self.state = 112
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 114
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==2:
                            self.state = 113
                            self.match(RUSynthParser.AND_CONJ)


                        self.state = 116
                        self.noun_phrase(4)
                        pass

                    elif la_ == 2:
                        localctx = RUSynthParser.Noun_phraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_noun_phrase)
                        self.state = 117
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 118
                        self.adj_phrase(0)
                        pass

                    elif la_ == 3:
                        localctx = RUSynthParser.Noun_phraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_noun_phrase)
                        self.state = 119
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 120
                        self.dep_clause()
                        pass

             
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Verb_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._VERB = None # Token

        def NEG_N(self):
            return self.getToken(RUSynthParser.NEG_N, 0)

        def verb_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Verb_phraseContext,0)


        def NEG_V(self):
            return self.getToken(RUSynthParser.NEG_V, 0)

        def prep_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Prep_phraseContext,0)


        def inf_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Inf_phraseContext,0)


        def PRED(self):
            return self.getToken(RUSynthParser.PRED, 0)

        def VERB(self):
            return self.getToken(RUSynthParser.VERB, 0)

        def ADV(self, i:int=None):
            if i is None:
                return self.getTokens(RUSynthParser.ADV)
            else:
                return self.getToken(RUSynthParser.ADV, i)

        def noun_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Noun_phraseContext,0)


        def dep_clause(self):
            return self.getTypedRuleContext(RUSynthParser.Dep_clauseContext,0)


        def getRuleIndex(self):
            return RUSynthParser.RULE_verb_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerb_phrase" ):
                listener.enterVerb_phrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerb_phrase" ):
                listener.exitVerb_phrase(self)



    def verb_phrase(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RUSynthParser.Verb_phraseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_verb_phrase, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 127
                self.match(RUSynthParser.NEG_N)
                self.state = 128
                self.verb_phrase(8)
                pass

            elif la_ == 2:
                self.state = 129
                self.match(RUSynthParser.NEG_V)
                pass

            elif la_ == 3:
                self.state = 130
                self.prep_phrase()
                self.state = 131
                self.verb_phrase(6)
                pass

            elif la_ == 4:
                self.state = 133
                self.inf_phrase(0)
                self.state = 134
                self.verb_phrase(5)
                pass

            elif la_ == 5:
                self.state = 136
                self.match(RUSynthParser.PRED)
                self.state = 137
                self.inf_phrase(0)
                pass

            elif la_ == 6:
                self.state = 138
                localctx._VERB = self.match(RUSynthParser.VERB)
                self.state = 139
                self.match(RUSynthParser.ADV)
                pass

            elif la_ == 7:
                self.state = 140
                localctx._VERB = self.match(RUSynthParser.VERB)
                add_verb(self.stack, *get_tags((None if localctx._VERB is None else localctx._VERB.text)))
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 158
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = RUSynthParser.Verb_phraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_verb_phrase)
                        self.state = 144
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 146
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                        if la_ == 1:
                            self.state = 145
                            self.match(RUSynthParser.ADV)


                        self.state = 151
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                        if la_ == 1:
                            self.state = 148
                            self.noun_phrase(0)
                            pass

                        elif la_ == 2:
                            self.state = 149
                            self.prep_phrase()
                            pass

                        elif la_ == 3:
                            self.state = 150
                            self.dep_clause()
                            pass


                        self.state = 154
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                        if la_ == 1:
                            self.state = 153
                            self.match(RUSynthParser.ADV)


                        pass

                    elif la_ == 2:
                        localctx = RUSynthParser.Verb_phraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_verb_phrase)
                        self.state = 156
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 157
                        self.inf_phrase(0)
                        pass

             
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Grnd_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRND(self):
            return self.getToken(RUSynthParser.GRND, 0)

        def noun_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Noun_phraseContext,0)


        def prep_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Prep_phraseContext,0)


        def getRuleIndex(self):
            return RUSynthParser.RULE_grnd_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrnd_phrase" ):
                listener.enterGrnd_phrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrnd_phrase" ):
                listener.exitGrnd_phrase(self)




    def grnd_phrase(self):

        localctx = RUSynthParser.Grnd_phraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_grnd_phrase)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(RUSynthParser.GRND)
                self.state = 164
                self.noun_phrase(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(RUSynthParser.GRND)
                self.state = 166
                self.prep_phrase()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.match(RUSynthParser.GRND)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inf_phraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noun_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Noun_phraseContext,0)


        def inf_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Inf_phraseContext,0)


        def prep_phrase(self):
            return self.getTypedRuleContext(RUSynthParser.Prep_phraseContext,0)


        def INF(self):
            return self.getToken(RUSynthParser.INF, 0)

        def getRuleIndex(self):
            return RUSynthParser.RULE_inf_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInf_phrase" ):
                listener.enterInf_phrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInf_phrase" ):
                listener.exitInf_phrase(self)



    def inf_phrase(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RUSynthParser.Inf_phraseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_inf_phrase, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 10, 11]:
                self.state = 171
                self.noun_phrase(0)
                self.state = 172
                self.inf_phrase(5)
                pass
            elif token in [13]:
                self.state = 174
                self.prep_phrase()
                self.state = 175
                self.inf_phrase(4)
                pass
            elif token in [9]:
                self.state = 177
                self.match(RUSynthParser.INF)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 184
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = RUSynthParser.Inf_phraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_inf_phrase)
                        self.state = 180
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 181
                        self.prep_phrase()
                        pass

                    elif la_ == 2:
                        localctx = RUSynthParser.Inf_phraseContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_inf_phrase)
                        self.state = 182
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 183
                        self.noun_phrase(0)
                        pass

             
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.adj_phrase_sempred
        self._predicates[6] = self.noun_phrase_sempred
        self._predicates[7] = self.verb_phrase_sempred
        self._predicates[9] = self.inf_phrase_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def adj_phrase_sempred(self, localctx:Adj_phraseContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def noun_phrase_sempred(self, localctx:Noun_phraseContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def verb_phrase_sempred(self, localctx:Verb_phraseContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

    def inf_phrase_sempred(self, localctx:Inf_phraseContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




