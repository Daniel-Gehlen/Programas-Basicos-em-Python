import pymongo

# Conectar ao cluster do MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER_URL>/<DB_NAME>?retryWrites=true&w=majority")

# Selecionar um banco de dados e uma coleção
db = client["exemplo_nosql"]
collection = db["registros"]

# Inserir um documento na coleção
novo_registro = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}
registro_inserido = collection.insert_one(novo_registro)
print("Registro inserido:", registro_inserido.inserted_id)

# Consultar e retornar todos os registros na coleção
registros = collection.find()

# Imprimir os registros retornados
for registro in registros:
    print("ID:", registro["_id"])
    print("Nome:", registro["nome"])
    print("Idade:", registro["idade"])
    print("Cidade:", registro["cidade"])
    print("------")

# Fechar a conexão
client.close()


# No entanto, o código não imprimirá os registros na coleção porque requer autenticação e acesso
# aos dados no cluster do MongoDB Atlas. Para realizar consultas e visualizar os dados no MongoDB
# Atlas, você precisa substituir <USERNAME>, <PASSWORD>, <CLUSTER_URL> e <DB_NAME> pelos valores
# corretos da sua conta e configurar as permissões de acesso no MongoDB Atlas.

# Certifique-se de que você tenha criado um banco de dados, uma coleção e inserido dados no 
# MongoDB Atlas antes de tentar recuperar e imprimir esses dados. Caso contrário, não haverá 
# registros para serem retornados e exibidos no terminal.

