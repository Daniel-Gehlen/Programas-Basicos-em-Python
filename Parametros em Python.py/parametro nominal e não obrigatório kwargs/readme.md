``` mermaid
graph TD
  start[Início]
  functionDefinition[Definir função imprimir_parametros]
  call1[Chamada 1]
  call2[Chamada 2]
  en[Fim]

  start --> functionDefinition
  functionDefinition --> call1
  call1 --> |Parâmetros| kwargs1{"cidade='São Paulo', idade=33, nome='João'"}
  call1 --> type1{"Tipo de objeto recebido = <class 'dict'>"}
  call1 --> qtde1{"Quantidade de parâmetros = 3"}
  call1 --> loop1[Loop para imprimir parâmetros]
  loop1 --> chave1{"chave = 'cidade'"}
  loop1 --> valor1{"valor = 'São Paulo'"}
  loop1 --> chave2{"chave = 'idade'"}
  loop1 --> valor2{"valor = 33"}
  loop1 --> chave3{"chave = 'nome'"}
  loop1 --> valor3{"valor = 'João'"}
  loop1 --> endLoop1{Fim do Loop}

  functionDefinition --> call2
  call2 --> |Parâmetros| kwargs2{"desconto=10, valor=100"}
  call2 --> type2{"Tipo de objeto recebido = <class 'dict'>"}
  call2 --> qtde2{"Quantidade de parâmetros = 2"}
  call2 --> loop2[Loop para imprimir parâmetros]
  loop2 --> chave4{"chave = 'desconto'"}
  loop2 --> valor4{"valor = 10"}
  loop2 --> chave5{"chave = 'valor'"}
  loop2 --> valor5{"valor = 100"}
  loop2 --> endLoop2{Fim do Loop}

  type1 --> qtde1
  type2 --> qtde2
  qtde1 --> loop1
  qtde2 --> loop2
  loop1 --> chave1
  chave1 --> valor1
  loop1 --> chave2
  valor1 --> chave2
  chave2 --> valor2
  loop1 --> chave3
  valor2 --> chave3
  chave3 --> valor3
  loop1 --> endLoop1
  loop2 --> chave4
  chave4 --> valor4
  loop2 --> chave5
  valor4 --> chave5
  chave5 --> valor5
  loop2 --> endLoop2
  endLoop1 --> en
  endLoop2 --> en
```