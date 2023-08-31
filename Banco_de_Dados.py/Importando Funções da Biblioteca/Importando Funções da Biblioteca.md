import math
import math as m
from math import sqrt, log, cos

# Importando funções da biblioteca "math"
resultado_sqrt = math.sqrt(25)
resultado_log = math.log(1024)
resultado_cos = math.cos(45)

# Importando funções da biblioteca "math" com alias "m"
resultado_sqrt_m = m.sqrt(25)
resultado_log_m = m.log(1024)
resultado_cos_m = m.cos(45)

# Importando funções específicas da biblioteca "math"
resultado_sqrt_especifico = sqrt(25)
resultado_log_especifico = log(1024)
resultado_cos_especifico = cos(45)

# Imprimindo os resultados
print("Resultados da biblioteca 'math':")
print("sqrt(25) =", resultado_sqrt)
print("log(1024) =", resultado_log)
print("cos(45) =", resultado_cos)

print("\nResultados da biblioteca 'math' com alias:")
print("sqrt(25) =", resultado_sqrt_m)
print("log(1024) =", resultado_log_m)
print("cos(45) =", resultado_cos_m)

print("\nResultados das funções específicas da biblioteca 'math':")
print("sqrt(25) =", resultado_sqrt_especifico)
print("log(1024) =", resultado_log_especifico)
print("cos(45) =", resultado_cos_especifico)

import sqlite3

conn = sqlite3.connect('aulaDB.db')
print("\nConexão com o banco de dados 'aulaDB.db' estabelecida.")

# Lembre-se de que o banco de dados "aulaDB.db" deve estar presente no diretório de execução
