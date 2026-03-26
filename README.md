# Comparación de Complejidad: ANTLR vs CYK

Comparación empírica del algoritmo CYK (O(n³)) contra un parser generado con ANTLR4 (O(n)) sobre la misma gramática libre de contexto.

---

## Gramática utilizada

La gramática base es:

```
A → a B C
B → b bas
B → big C boss
C → ε
C → c
```

Adaptada para admitir repeticiones (`S → A | A S`), lo que permite generar entradas de longitud arbitraria para medir el comportamiento en escala.

<img width="128" height="80" alt="Gramática" src="https://github.com/user-attachments/assets/25f0e273-be5a-4e22-85e2-b89f620ee91c" />

---

## Resultados

Ambos parsers coinciden en todas las entradas probadas.

### Gráfica comparativa

![Comparación de rendimiento ANTLR vs CYK](comparacion.png)

La gráfica muestra con claridad la diferencia de complejidad: ANTLR mantiene tiempos de ejecución prácticamente constantes (≈0 s) para cualquier longitud de entrada, mientras que CYK crece de forma cúbica, superando 1.6 s para entradas de ~150 tokens.

### Salida por terminal

```
Ambos parsers coinciden en todas las entradas.
Gráfica guardada en comparacion.png
```

---

## Algoritmo CYK

CYK (Cocke–Younger–Kasami) requiere la gramática en **Forma Normal de Chomsky (FNC)**. La transformación de la gramática original se realiza en cuatro pasos:

### Paso 1 — Eliminar el símbolo de inicio del lado derecho
No hay violaciones; no se realizan cambios.

### Paso 2 — Eliminar producciones nulas, unitarias e inútiles

`C → ε` se elimina y se propagan sus variantes:

```
S → a B C | a B | a B C S | a B S
A → a B C | a B
B → b bas | big C boss | big boss
C → c
```

### Paso 3 — Reemplazar terminales en producciones mixtas

```
A_a  → a
B_b  → b
B_bas → bas
BIG  → big
BOSS → boss
```

### Paso 4 — Reducir producciones con más de dos no terminales

```
S   → A_1 C  |  A_a B  |  A_2 S  |  A_3 S
A_1 → A_a B
A_2 → A_1 C
A_3 → A_a B
A   → A_1 C  |  A_a B
B   → B_b B_bas  |  B_C BOSS  |  BIG BOSS
B_C → BIG C
C   → c
```

---

## Estructura del proyecto

```
/
├── ANTLR/
│   ├── GRAMATICA/
│   │   ├── gramCC.g4          # Gramática ANTLR4
│   │   ├── gramCCLexer.py     # Generado por ANTLR — no editar
│   │   ├── gramCCParser.py    # Generado por ANTLR — no editar
│   │   └── gramCCVisitor.py   # Generado por ANTLR — no editar
│   └── main.py                # Parser ANTLR: función evaluar()
├── cyk.py                     # Implementación del algoritmo CYK
├── comparacion.py             # Script principal de comparación y graficación
├── genEntrada.py              # Generador de archivo de entradas
├── entrada.txt                # Entradas de prueba (generadas)
├── entry.txt                  # Entradas mixtas (válidas e inválidas)
├── comparacion.png            # Gráfica de resultados (generada)
├── requisitos.txt             # Dependencias Python
└── README.md
```

---

## Requisitos previos

### Python 3.8+

```bash
sudo apt install -y python3-full python3-pip python3-venv
```

### Java Runtime (requerido por ANTLR)

```bash
sudo apt install default-jre
java -version
# openjdk version "17.0.x"
```

### ANTLR4 tools

```bash
pip install antlr4-tools
# Si no funciona:
pipx install antlr4-tools
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

---

## Instalación

```bash
# 1. Clonar y entrar al repositorio
git clone <url-del-repo>
cd <carpeta>

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requisitos.txt

# 4. Generar el parser ANTLR (dentro de la carpeta ANTLR/GRAMATICA/)
cd ANTLR/GRAMATICA
antlr4 -Dlanguage=Python3 gramCC.g4
cd ../..
```

---

## Uso

### Generar el archivo de entradas

```bash
python genEntrada.py
```

Esto crea `entrada.txt` con 50 líneas de longitud creciente (3 a 150 tokens), todas válidas según la gramática.

### Ejecutar la comparación

```bash
python comparacion.py entrada.txt
```

Genera la gráfica `comparacion.png` y muestra por consola si ambos parsers coinciden.

### Ejecutar solo CYK

```bash
python cyk.py entrada.txt
```

### Ejecutar solo ANTLR

```bash
python ANTLR/main.py entrada.txt
```

---

## Análisis de complejidad

| Parser | Complejidad | Tiempo (~150 tokens) |
|--------|-------------|----------------------|
| ANTLR  | O(n)        | ≈ 0.01 s             |
| CYK    | O(n³)       | ≈ 1.6 s              |

ANTLR utiliza la estrategia LL(*) con predicción adaptativa, lo que le permite analizar la entrada en tiempo lineal. CYK, al ser un algoritmo de programación dinámica de propósito general para gramáticas en FNC, tiene complejidad cúbica inherente: para una entrada de *n* tokens construye una tabla de n² celdas y cada celda puede requerir hasta *n* comparaciones.
 
