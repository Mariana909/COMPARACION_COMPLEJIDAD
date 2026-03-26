# Generated from gramCC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramCCParser import gramCCParser
else:
    from gramCCParser import gramCCParser

# This class defines a complete generic visitor for a parse tree produced by gramCCParser.

class gramCCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramCCParser#programa.
    def visitPrograma(self, ctx:gramCCParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramCCParser#regla_s.
    def visitRegla_s(self, ctx:gramCCParser.Regla_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramCCParser#regla_a.
    def visitRegla_a(self, ctx:gramCCParser.Regla_aContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramCCParser#regla_b.
    def visitRegla_b(self, ctx:gramCCParser.Regla_bContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramCCParser#regla_c.
    def visitRegla_c(self, ctx:gramCCParser.Regla_cContext):
        return self.visitChildren(ctx)



del gramCCParser