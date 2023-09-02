``` mermaid
graph TD
  subgraph ConexaoBancoDados
    import_sqlite3[Importar sqlite3]
    connect[Conectar ao Banco de Dados]
    create_table[Criar Tabela fornecedor]
    cursor[Definir Cursor]
  end

  subgraph OperacoesCRUD
    create_data[Operação CREATE]
    read_data[Operação READ]
    update_data[Operação UPDATE]
    delete_data[Operação DELETE]
  end

  subgraph Exemplo
    numbers[Exemplo: 64, 34, 25, 12, 22]
    print_result[Print Resultados]
  end

  import_sqlite3 --> connect
  connect --> create_table
  connect --> cursor
  cursor --> create_data
  create_data --> read_data
  read_data --> print_result
  update_data --> print_result
  delete_data --> print_result
```