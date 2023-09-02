``` mermaid
graph TD
  subgraph ConexaoMongoDB
    import_pymongo[Importar pymongo]
    connect[Conectar ao Cluster MongoDB Atlas]
    select_db_collection[Selecionar Banco de Dados e Coleção]
  end

  subgraph OperacoesCRUD
    insert_data[Inserir Documento]
    find_data[Consultar Documentos]
    print_result[Print Resultados]
  end

  import_pymongo --> connect
  connect --> select_db_collection
  select_db_collection --> insert_data
  insert_data --> find_data
  find_data --> print_result
```