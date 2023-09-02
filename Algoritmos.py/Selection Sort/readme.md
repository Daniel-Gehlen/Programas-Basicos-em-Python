``` mermaid
graph TD;
  start["Início"];
  input["Input: Lista de Números"];
  initialize["Inicializar i = 0"];
  outer_loop["Loop Externo: i < tamanho da lista"];
  set_min_i["Definir min_i = i"];
  inner_loop["Loop Interno: j = i + 1 até o final"];
  compare["Comparar arr[j] com arr[min_i]"];
  update_min_i["Atualizar min_i se necessário"];
  swap["Trocar arr[i] com arr[min_i]"];
  increment_i["Incrementar i"];
  en["Fim"];

  start --> input;
  input --> initialize;
  initialize --> outer_loop;
  outer_loop --> set_min_i;
  set_min_i --> inner_loop;
  inner_loop --> compare;
  compare --> update_min_i;
  compare --> inner_loop;
  update_min_i --> inner_loop;
  inner_loop --> inner_loop;
  inner_loop --> swap;
  swap --> increment_i;
  increment_i --> outer_loop;
  outer_loop --> en;
```