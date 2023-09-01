``` mermaid
graph TD
  start[Início]
  functionDefinition[Definir função imprimir_parametros]
  call1[Chamada 1]
  call2[Chamada 2]
  en[Fim]

  start --> functionDefinition
  functionDefinition --> call1
  call1 --> |Parâmetros| args1{"'São Paulo', 10, 23, 78, 'João'"}
  call1 --> qtde1{qtde_parametros = 5}
  call1 --> loop1[Loop para imprimir parâmetros]
  loop1 --> i1{i = 0}
  loop1 --> valor1{"valor = 'São Paulo'"}
  loop1 --> iincrement1{i = 1}
  loop1 --> valor2{"valor = 10"}
  loop1 --> iincrement2{i = 2}
  loop1 --> valor3{"valor = 23"}
  loop1 --> iincrement3{i = 3}
  loop1 --> valor4{"valor = 78"}
  loop1 --> iincrement4{i = 4}
  loop1 --> valor5{"valor = 'João'"}
  loop1 --> endLoop1{i = 5}

  functionDefinition --> call2
  call2 --> |Parâmetros| args2{"10, 'São Paulo'"}
  call2 --> qtde2{qtde_parametros = 2}
  call2 --> loop2[Loop para imprimir parâmetros]
  loop2 --> i2{i = 0}
  loop2 --> valor6{"valor = 10"}
  loop2 --> iincrement5{i = 1}
  loop2 --> valor7{"valor = 'São Paulo'"}
  loop2 --> endLoop2{i = 2}

  qtde1 --> loop1
  qtde2 --> loop2
  loop1 --> i1
  iincrement1 --> valor1
  loop1 --> iincrement1
  valor1 --> iincrement1
  iincrement1 --> valor2
  loop1 --> iincrement2
  valor2 --> iincrement2
  iincrement2 --> valor3
  loop1 --> iincrement3
  valor3 --> iincrement3
  iincrement3 --> valor4
  loop1 --> iincrement4
  valor4 --> iincrement4
  iincrement4 --> valor5
  loop1 --> iincrement5
  valor5 --> iincrement5
  iincrement5 --> endLoop1

  loop2 --> i2
  iincrement5 --> valor6
  loop2 --> iincrement5
  valor6 --> iincrement5
  iincrement5 --> valor7
  loop2 --> endLoop2
  endLoop1 --> en
  endLoop2 --> en
```