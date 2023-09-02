``` mermaid
graph TD;
  start["Início"];
  input["Input: Lista, Valor"];
  initialize["Inicializar índice i = 0"];
  loop["Loop: i < tamanho da lista"];
  check["Verificar se lista[i] == Valor"];
  found["Valor encontrado"];
  notfound["Valor não encontrado"];
  en["Fim"];

  start --> input;
  input --> initialize;
  initialize --> loop;
  loop --> check;
  check --> found;
  check --> loop;
  found --> en;
  loop --> notfound;
  notfound

```