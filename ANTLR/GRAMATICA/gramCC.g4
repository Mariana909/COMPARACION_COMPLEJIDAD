grammar gramCC;

programa: regla_s EOF;

regla_s: regla_a
| regla_a regla_s;

regla_a: A regla_b regla_c;

regla_b: B BAS
| BIG regla_c BOSS;

regla_c  : C?;

A: 'a';
B: 'b';
C: 'c';
BAS: 'bas';
BIG: 'big';
BOSS: 'boss';

WS: [ \t\r\n]+ -> skip;
