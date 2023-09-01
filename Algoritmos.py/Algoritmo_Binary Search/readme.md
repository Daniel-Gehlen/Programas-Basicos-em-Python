``` mermaid
graph TD
  subgraph Inicializacao
    arr[arr]
    target[target]
    left[left]
    right[right]
    rightLabel[len arr - 1]
  end

  subgraph Loop
    checkLeftRight(left <= right?)
    mid[mid]
    checkMidValueArr[mid igual target?]
    updateLeftRight[Atualiza left ou right]
    compareValuesAarr[mid ? target?]
  end

  subgraph Resultado
    result[Retorna mid]
    notFound[Retorna -1]
  end

  Inicializacao --> arr
  Inicializacao --> target
  Inicializacao --> left
  Inicializacao --> right
  Inicializacao --> rightLabel

  arr --> checkLeftRight
  target --> checkLeftRight
  left --> checkLeftRight
  right --> checkLeftRight

  checkLeftRight -- Sim --> mid
  checkLeftRight -- Nao --> notFound

  mid --> checkMidValue
  checkMidValue -- Sim --> result
  checkMidValue -- Nao --> compareValues

  compareValues -- Maior --> updateLeftRight
  compareValues -- Menor --> checkLeftRight
  compareValues -- Igual --> result

  updateLeftRight --> checkLeftRight

  result --> resultLabel[Retorna mid]

  notFound --> notFoundLabel[Retorna -1]


```