Actividad Análisis Sintáctico

1. Implementar un analizador sintáctico en Python para la gramática de ejemplo de las diapositivas, generando el árbol sintáctico.
   
   <img width="260" height="211" alt="image" src="https://github.com/user-attachments/assets/d5193a3d-4674-45a5-9f7e-978109a23776" />

   

2. Realizar la comparación del algoritmo CYK con complejidad O(n³) y un algoritmo con complejidad lineal de análisis sintáctico.
3. 
   Dentro de los algoritmos de complejidad lineal para el análisis sintáctico se tienen ASD (análisis sintáctico descendente) y ASA (análisis sintáctico ascendente), es decir LL y LR.
   
   Por lo que dentro de la comparación por el lado de complejidad O(n³) se tendrán los algoritmos CYK y Early, mientras que por el lado de complejidad O(n) se realizará la implementación ASD con pila y tabla M, y ASA versión SLR. Las pruebas se realizarán con la misma gramática del primer punto, pero modificada para que no tenga recursividad por izquierda, pues es problemático para utilizar LL.
   
   E → T E'
   E' → opsuma T E' | ε
   T → F T'
   T' → opmul F T' | ε
   F → id
   F → num
   F → pari E pard

   Terminales: opsuma, opmul, pari, pard, id, num
   No terminales: E'', E, E', T, T', F

   SLR
   
   Como primer paso, obtenemos la gramática aumentada.
   E'' → E
   E → T E'
   E' → opsuma T E'
   E' → ε
   T → F T'
   T' → opmul F T'
   T' → ε
   F → id
   F → num
   F → pari E pard

   Ahora necesitamos obtener los conjuntos PRIMERO(X) y SIGUIENTE(A)

   Reglas para calcular PRIMERO

   1. Si X es terminal → PRIMERO(X) = { X }
   2. Si existe X → ε → agregar ε a PRIMERO(X)
   3. Si existe X → Y₁ Y₂ ... Yₖ → agregar PRIMERO(Y₁) sin ε. Si ε ∈ PRIMERO(Y₁), agregar PRIMERO(Y₂) sin ε, y así sucesivamente. Si todos derivan ε, agregar ε.

      PRIMERO(F) = {id, num, pari}
   
      PRIMERO(T') = {opmul, ε}
   
      PRIMERO(T) = {id, num, pari}
   
      PRIMERO(E') = {opsuma, ε}
   
      PRIMERO(E) = {id, num, pari}
   
      PRIMERO(E'') = {id, num, pari}

      Reglas para calcular SIGUIENTE
      
      1. $ ∈ SIGUIENTE(S') donde S' es el símbolo inicial aumentado
      2. Si existe A → α B β → agregar PRIMERO(β) - {ε} a SIGUIENTE(B)
      3. Si existe A → α B o A → α B β con ε ∈ PRIMERO(β) → agregar SIGUIENTE(A) a SIGUIENTE(B)
     
      SIGUIENTE(E'') = {$}

      SIGUIENTE(E) = {$, pard}

      SIGUIENTE(E') = {$, pard}

      SIGUIENTE(T) = {opsuma, $, pard}

      SIGUIENTE(T') = {opsuma, $, pard}

      SIGUIENTE(F) = {opmul, opsuma, $, pard}


      LR(0) y Autómata

      ESTADOS LR(0)

      I0:
        E'' → • E
        E   → • T E'
        T   → • F T'
        F   → • id
        F   → • num
        F   → • pari E pard
      
      I1:
        E'' → E •
      
      I2:
        E  → T • E'
        E' → • opsuma T E'
        E' → •
      
      I3:
        T  → F • T'
        T' → • opmul F T'
        T' → •
      
      I4:
        F → id •
      
      I5:
        F → num •
      
      I6:
        F  → pari • E pard
        E  → • T E'
        T  → • F T'
        F  → • id
        F  → • num
        F  → • pari E pard
      
      I7:
        E → T E' •
      
      I8:
        E' → opsuma • T E'
        T  → • F T'
        F  → • id
        F  → • num
        F  → • pari E pard
      
      I9:
        T → F T' •
      
      I10:
        T' → opmul • F T'
        F  → • id
        F  → • num
        F  → • pari E pard
      
      I11:
        F → pari E • pard
      
      I12:
        F → pari E pard •
      
      TRANSICIONES 
      
      I0  --E-->    I1
      I0  --T-->    I2
      I0  --F-->    I3
      I0  --id-->   I4
      I0  --num-->  I5
      I0  --pari--> I6
      
      I2  --E'-->     I7
      I2  --opsuma--> I8
      
      I3  --T'-->    I9
      I3  --opmul--> I10
      
      I6  --E-->    I11
      I6  --T-->    I2   (reutilizado)
      I6  --F-->    I3   (reutilizado)
      I6  --id-->   I4   (reutilizado)
      I6  --num-->  I5   (reutilizado)
      I6  --pari--> I6   (recursivo)
      
      I8  --T-->    I2   (reutilizado)
      I8  --F-->    I3   (reutilizado)
      I8  --id-->   I4   (reutilizado)
      I8  --num-->  I5   (reutilizado)
      I8  --pari--> I6   (reutilizado)
      
      I10 --F-->    I3   (reutilizado)
      I10 --id-->   I4   (reutilizado)
      I10 --num-->  I5   (reutilizado)
      I10 --pari--> I6   (reutilizado)
      
      I11 --pard--> I12


      Creación de la Tabla
      
      Reglas para llenar la tabla
      ACCION:

      Si A → α • a β está en Iᵢ y IR_A(Iᵢ, a) = Iⱼ → ACCION[i, a] = sj (desplazar)
      Si A → α • está en Iᵢ → para todo a ∈ FOLLOW(A), ACCION[i, a] = rN (reducir por producción N)
      Si E'' → E • está en Iᵢ → ACCION[i, $] = acc (aceptar)
      
      IR_A:
      
      Si IR_A(Iᵢ, A) = Iⱼ donde A es no terminal → IR_A[i, A] = j


     ## Tabla SLR — ACCION / IR_A

| Estado | id | num | pari | pard | opsuma | opmul | $ | E | E' | T | T' | F |
|--------|-----|-----|------|------|--------|-------|---|---|----|---|----|---|
| 0  | s4 | s5 | s6 | —  | —   | —   | —   | 1  | —  | 2 | —  | 3  |
| 1  | —  | —  | —  | —  | —   | —   | acc | —  | —  | — | —  | —  |
| 2  | —  | —  | —  | r3 | s8  | —   | r3  | —  | 7  | — | —  | —  |
| 3  | —  | —  | —  | r6 | r6  | s10 | r6  | —  | —  | — | 9  | —  |
| 4  | —  | —  | —  | r7 | r7  | r7  | r7  | —  | —  | — | —  | —  |
| 5  | —  | —  | —  | r8 | r8  | r8  | r8  | —  | —  | — | —  | —  |
| 6  | s4 | s5 | s6 | —  | —   | —   | —   | 11 | —  | 2 | —  | 3  |
| 7  | —  | —  | —  | r1 | —   | —   | r1  | —  | —  | — | —  | —  |
| 8  | s4 | s5 | s6 | —  | —   | —   | —   | —  | —  | 2 | —  | 3  |
| 9  | —  | —  | —  | r4 | r4  | —   | r4  | —  | —  | — | —  | —  |
| 10 | s4 | s5 | s6 | —  | —   | —   | —   | —  | —  | — | —  | 3  |
| 11 | —  | —  | —  | s12| —   | —   | —   | —  | —  | — | —  | —  |
| 12 | —  | —  | —  | r9 | r9  | r9  | r9  | —  | —  | — | —  | —  |

> **sN** = shift al estado N &nbsp;|&nbsp; **rN** = reducir por producción N &nbsp;|&nbsp; **acc** = aceptar &nbsp;|&nbsp; **—** = error sintáctico  
> Columnas **E, E', T, T', F** corresponden a **IR\_A**. Las demás a **ACCION**.

### Producciones
| N° | Producción |
|----|-----------|
| P1 | E  → T E' |
| P2 | E' → opsuma T E' |
| P3 | E' → ε |
| P4 | T  → F T' |
| P5 | T' → opmul F T' |
| P6 | T' → ε |
| P7 | F  → id |
| P8 | F  → num |
| P9 | F  → pari E pard |



LL

En este caso no se necesita calcular de nuevo PRIMERO y SIGUIENTE, pues estos son los mismo calculados para SLR, lo único a tener en cuenta es que se ignora PRIMERO(E'') y SIGUIENTE(E''), pues E'' solo existe para SLR que necesita de una gramática aumentada.

Reglas para crear la tabla M

1. Para cada producción A → α: agrega A → α en M[A, t] para todo terminal t en PRIMERO(α)
2. Si ε ∈ PRIMERO(α): agrega A → α en M[A, t] para todo t en SIGUIENTE(A)


## Tabla M — LL(1)

| NT \ Terminal | id | num | pari | pard | opsuma | opmul | $ |
|---------------|-----|-----|------|------|--------|-------|---|
| E  | E → T E' | E → T E' | E → T E' | — | — | — | — |
| E' | — | — | — | E' → ε | E' → opsuma T E' | — | E' → ε |
| T  | T → F T' | T → F T' | T → F T' | — | — | — | — |
| T' | — | — | — | T' → ε | T' → ε | T' → opmul F T' | T' → ε |
| F  | F → id | F → num | F → pari E pard | — | — | — | — |

> **—** = error sintáctico
      
 
