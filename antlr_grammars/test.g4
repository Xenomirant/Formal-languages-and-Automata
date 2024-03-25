grammar test;

//WS: ('\r' | '\n' | '\t' | ' ')+ -> skip;
WS: [ \t\r\n]+ -> skip;

NOUN : WORD '_NOUN'   //noun
| WORD '_NPRO';       //pronoun

//NEG_V: 'нет_PRED';
//
//NEG_N: 'не_PRCL';

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

fragment WORD : ([а-я] | [А-Я])+;

sentence: NOUN VERB ADV CONJ ADV;