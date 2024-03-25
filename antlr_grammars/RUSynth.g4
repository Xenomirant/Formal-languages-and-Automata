grammar RUSynth;

@header{
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
}

@members{
stack = [{}]
}

//WS: ('\r' | '\n' | '\t' | ' ')+ -> skip;
WS: [ \t\r\n]+ -> channel(HIDDEN);

AND_CONJ: 'и_CONJ';
NEG_V: 'нет_PRED';
NEG_N: 'не_PRCL';

NOUN : WORD '_NOUN'   //noun
| WORD '_NPRO';       //pronoun

CONJ : WORD '_CONJ'; // seems like any conjunctional or wh-phrase

VERB : WORD '_VERB'; //verb in plain form

PRED: WORD '_PRED';

INF: WORD '_INFN'; //infinitive

ADJ : WORD '_ADJF' //adjective
| WORD '_ADJS'
| WORD '_PRTF' //participle
| WORD '_PRTS'
| WORD '_NUMR';

ADV : WORD '_COMP'        //comparative
| WORD '_ADVB';

GRND : WORD '_GRND';

PREP : WORD '_PREP'; // preposition

UNK : WORD '_UNK' //Interjection
| WORD '_INTJ'
| WORD '_PRCL';

fragment WORD : [а-яА-Я]+;


sentence: clause (CONJ)* clause
| (CONJ clause)* clause
| clause;

clause
@after{check_clause(self.stack)
self.stack.append({})}: (grnd_phrase)? (noun_phrase)* verb_phrase
| verb_phrase (noun_phrase)* (grnd_phrase)?;

dep_clause: sub_conj clause
| sub_conj verb_phrase;

sub_conj: CONJ
| ADJ;

prep_phrase: PREP noun_phrase
| PREP ADJ;

adj_phrase: adj_phrase prep_phrase
| adj_phrase dep_clause
| ADV (NEG_N)? ADJ
| (NEG_N)? ADV ADJ
| ADJ;

noun_phrase: adj_phrase noun_phrase
| noun_phrase adj_phrase
| noun_phrase (AND_CONJ)? noun_phrase
| noun_phrase dep_clause
| (NEG_N)? NOUN {add_subj(self.stack, *get_tags($NOUN.text))};

verb_phrase: verb_phrase (ADV)? (noun_phrase | prep_phrase | dep_clause) (ADV)?
| NEG_N verb_phrase
| NEG_V
| prep_phrase verb_phrase
| inf_phrase verb_phrase
| verb_phrase inf_phrase
| PRED inf_phrase
| VERB ADV
| VERB {add_verb(self.stack, *get_tags($VERB.text))};

grnd_phrase: GRND noun_phrase
| GRND prep_phrase
| GRND;

// мне только спросить не разберется
//спрашивать тут уже некого
inf_phrase: noun_phrase inf_phrase
| prep_phrase inf_phrase
| inf_phrase prep_phrase
| inf_phrase noun_phrase
| INF;