import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from antlr4 import *
from GRAMATICA.gramCCLexer import gramCCLexer
from GRAMATICA.gramCCParser import gramCCParser

def evaluar(expresion):
    input_stream = InputStream(expresion)
    lexer = gramCCLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = gramCCParser(tokens)
    
    lexer.removeErrorListeners()
    parser.removeErrorListeners()

    tree = parser.programa() 
    
    if parser.getNumberOfSyntaxErrors() > 0:
        return False
    else:
        return True

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            entrada = sys.argv[1]
            with open(entrada, 'r') as en:
                datos = en.read().splitlines()
                
                for linea in datos:
                    if linea.strip() == "":
                        continue
                    t_0=time.time()
                    resultado = evaluar(linea)
                    t_1=time.time()
                    estado = "ACEPTADA" if resultado else "RECHAZADA"

                    print(f"{linea} -> {estado} ({t_1 - t_0:.6f} s)")
        else:
            print("No se detectó archivo de entrada")

    except FileNotFoundError:
        print("No se encontró el archivo")