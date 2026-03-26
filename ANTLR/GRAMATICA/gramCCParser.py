# Generated from gramCC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,30,8,3,1,4,3,4,33,8,4,1,4,0,0,5,0,2,4,6,8,0,0,32,0,10,1,0,0,0,
        2,17,1,0,0,0,4,19,1,0,0,0,6,29,1,0,0,0,8,32,1,0,0,0,10,11,3,2,1,
        0,11,12,5,0,0,1,12,1,1,0,0,0,13,18,3,4,2,0,14,15,3,4,2,0,15,16,3,
        2,1,0,16,18,1,0,0,0,17,13,1,0,0,0,17,14,1,0,0,0,18,3,1,0,0,0,19,
        20,5,1,0,0,20,21,3,6,3,0,21,22,3,8,4,0,22,5,1,0,0,0,23,24,5,2,0,
        0,24,30,5,4,0,0,25,26,5,5,0,0,26,27,3,8,4,0,27,28,5,6,0,0,28,30,
        1,0,0,0,29,23,1,0,0,0,29,25,1,0,0,0,30,7,1,0,0,0,31,33,5,3,0,0,32,
        31,1,0,0,0,32,33,1,0,0,0,33,9,1,0,0,0,3,17,29,32
    ]

class gramCCParser ( Parser ):

    grammarFileName = "gramCC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'a'", "'b'", "'c'", "'bas'", "'big'", 
                     "'boss'" ]

    symbolicNames = [ "<INVALID>", "A", "B", "C", "BAS", "BIG", "BOSS", 
                      "WS" ]

    RULE_programa = 0
    RULE_regla_s = 1
    RULE_regla_a = 2
    RULE_regla_b = 3
    RULE_regla_c = 4

    ruleNames =  [ "programa", "regla_s", "regla_a", "regla_b", "regla_c" ]

    EOF = Token.EOF
    A=1
    B=2
    C=3
    BAS=4
    BIG=5
    BOSS=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regla_s(self):
            return self.getTypedRuleContext(gramCCParser.Regla_sContext,0)


        def EOF(self):
            return self.getToken(gramCCParser.EOF, 0)

        def getRuleIndex(self):
            return gramCCParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = gramCCParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.regla_s()
            self.state = 11
            self.match(gramCCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Regla_sContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regla_a(self):
            return self.getTypedRuleContext(gramCCParser.Regla_aContext,0)


        def regla_s(self):
            return self.getTypedRuleContext(gramCCParser.Regla_sContext,0)


        def getRuleIndex(self):
            return gramCCParser.RULE_regla_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegla_s" ):
                return visitor.visitRegla_s(self)
            else:
                return visitor.visitChildren(self)




    def regla_s(self):

        localctx = gramCCParser.Regla_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_regla_s)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.regla_a()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.regla_a()
                self.state = 15
                self.regla_s()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Regla_aContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def A(self):
            return self.getToken(gramCCParser.A, 0)

        def regla_b(self):
            return self.getTypedRuleContext(gramCCParser.Regla_bContext,0)


        def regla_c(self):
            return self.getTypedRuleContext(gramCCParser.Regla_cContext,0)


        def getRuleIndex(self):
            return gramCCParser.RULE_regla_a

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegla_a" ):
                return visitor.visitRegla_a(self)
            else:
                return visitor.visitChildren(self)




    def regla_a(self):

        localctx = gramCCParser.Regla_aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_regla_a)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(gramCCParser.A)
            self.state = 20
            self.regla_b()
            self.state = 21
            self.regla_c()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Regla_bContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def B(self):
            return self.getToken(gramCCParser.B, 0)

        def BAS(self):
            return self.getToken(gramCCParser.BAS, 0)

        def BIG(self):
            return self.getToken(gramCCParser.BIG, 0)

        def regla_c(self):
            return self.getTypedRuleContext(gramCCParser.Regla_cContext,0)


        def BOSS(self):
            return self.getToken(gramCCParser.BOSS, 0)

        def getRuleIndex(self):
            return gramCCParser.RULE_regla_b

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegla_b" ):
                return visitor.visitRegla_b(self)
            else:
                return visitor.visitChildren(self)




    def regla_b(self):

        localctx = gramCCParser.Regla_bContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_regla_b)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(gramCCParser.B)
                self.state = 24
                self.match(gramCCParser.BAS)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(gramCCParser.BIG)
                self.state = 26
                self.regla_c()
                self.state = 27
                self.match(gramCCParser.BOSS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Regla_cContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def C(self):
            return self.getToken(gramCCParser.C, 0)

        def getRuleIndex(self):
            return gramCCParser.RULE_regla_c

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegla_c" ):
                return visitor.visitRegla_c(self)
            else:
                return visitor.visitChildren(self)




    def regla_c(self):

        localctx = gramCCParser.Regla_cContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_regla_c)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 31
                self.match(gramCCParser.C)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





