# Generated from gramCC.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,41,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,1,6,4,6,36,8,6,11,6,12,6,37,1,6,1,6,0,0,7,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,1,0,1,3,0,9,10,13,13,32,32,41,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,1,15,1,0,0,0,3,17,1,0,0,0,5,19,1,0,0,0,7,21,1,0,0,0,
        9,25,1,0,0,0,11,29,1,0,0,0,13,35,1,0,0,0,15,16,5,97,0,0,16,2,1,0,
        0,0,17,18,5,98,0,0,18,4,1,0,0,0,19,20,5,99,0,0,20,6,1,0,0,0,21,22,
        5,98,0,0,22,23,5,97,0,0,23,24,5,115,0,0,24,8,1,0,0,0,25,26,5,98,
        0,0,26,27,5,105,0,0,27,28,5,103,0,0,28,10,1,0,0,0,29,30,5,98,0,0,
        30,31,5,111,0,0,31,32,5,115,0,0,32,33,5,115,0,0,33,12,1,0,0,0,34,
        36,7,0,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,
        0,38,39,1,0,0,0,39,40,6,6,0,0,40,14,1,0,0,0,2,0,37,1,6,0,0
    ]

class gramCCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    A = 1
    B = 2
    C = 3
    BAS = 4
    BIG = 5
    BOSS = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'a'", "'b'", "'c'", "'bas'", "'big'", "'boss'" ]

    symbolicNames = [ "<INVALID>",
            "A", "B", "C", "BAS", "BIG", "BOSS", "WS" ]

    ruleNames = [ "A", "B", "C", "BAS", "BIG", "BOSS", "WS" ]

    grammarFileName = "gramCC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


