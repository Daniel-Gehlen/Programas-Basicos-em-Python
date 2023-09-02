``` mermaid
graph TD
  subgraph ConexaoBancoDados
    import_sqlite3[Importar sqlite3]
    connect[Conectar ao Banco de Dados]
    create_table[Criar Tabela alunos]
    cursor[Definir Cursor]
  end

  subgraph OperacoesCRUD
    insert_data[Inserir Dados]
    commit[Commit Alterações]
    select_data[Selecionar Dados]
    print_result[Print Dados]
  end

  import_sqlite3 --> connect
  connect --> create_table
  connect --> cursor
  insert_data --> commit
  commit --> select_data
  select_data --> print_result
```