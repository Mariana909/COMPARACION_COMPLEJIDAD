Actividad Comparación complejidad


Realizar la comparación del algoritmo CYK con complejidad O(n³) y un algoritmo con complejidad lineal de análisis sintáctico.
 
   La comparación se realizará entre el algoritmo CYK implementado en python y la herramienta antlr con lenguaje objetivo python.
   
   La gramática usada para esta comparación es:

   <img width="128" height="80" alt="image" src="https://github.com/user-attachments/assets/25f0e273-be5a-4e22-85e2-b89f620ee91c" />


   ANTLR


   CYK

   Para realizar este algoritmo se necesita la gramática en forma normal de chomsky.

   Extrayendo de geeksforgeeks:

   Forma normal de Chomsky: 
      Una gramática libre de contexto G está en forma normal de Chomsky (FNC) si cada regla de G tiene la forma:
      
        * A --> BC , [con como máximo dos símbolos no terminales en el lado derecho]
        * A --> a , o [un símbolo terminal en el lado derecho]
        * S --> cadena nula ,             [cadena nula]

   Por lo que es necesario transformar la gramática para que esté en forma normal de Chomsky.

   Pasos para convertir una gramática libre de contexto a forma normal de chomsky

   Gramática Original:

   A → a B C

   B → b bas

   B → big C boss
   
   C → ε

   C → c

   Paso 1: Eliminar el símbolo de inicio del lado derecho.
   Ninguna regla viola este principio, por lo que no se realizan modificaciones en este paso.

   Paso 2: Eliminar producciones nulas, unitarias e inútiles.
   C produce ε, por lo que esta regla se elimina y se modifican las reglas para que contenga o no el simbolo terminal c.

   A → a B C

   A → a B 

   B → b bas

   B → big C boss

   B → big boss

   C → c

   Paso 3: Reemplazar terminales en producciones mixtas

   A → A_a B C        (a → A_1)
   A → A_a B
   A_a  → a
   B → B_b B_bas      (b → B_b, bas → B_bas)
   B_b  → b
   B_bas → bas
   B → BIG C BOSS     (big → BIG, boss → BOSS)
   B → BIG BOSS
   BIG  → big
   BOSS → boss
   C → c
   

   Paso 4: Reduzca las producciones con más de dos no terminales.

   A  → A_1 C         (antes A → A_a B C)
   A_1 → A_a B
   A  → A_a B
   A_a → a
   B  → B_b B_bas
   B_b  → b
   B_bas → bas
   B  → B_C BOSS       (antes B → BIG C BOSS)
   B_C → BIG C
   B  → BIG BOSS
   BIG  → big
   BOSS → boss
   C  → c
   
