``` mermaid
flowchart TD
  importMath[import math]
  importMathAlias[import math as m]
  importMathFunctions[from math import sqrt, log, cos]
  importSqlite3[import sqlite3]
  criarConexao[conn = sqlite3.connect 'aulaDB.db']
  mostrarConexao[print Conexão com o banco de dados 'aulaDB.db' estabelecida.]

  importMath --> resultadoSqrt
  importMath --> resultadoLog
  importMath --> resultadoCos

  importMathAlias --> resultadoSqrtM
  importMathAlias --> resultadoLogM
  importMathAlias --> resultadoCosM

  importMathFunctions --> resultadoSqrtEspecifico
  importMathFunctions --> resultadoLogEspecifico
  importMathFunctions --> resultadoCosEspecifico

  criarConexao --> mostrarConexao


```