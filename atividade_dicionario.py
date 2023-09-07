dados_cliente = {
     "Nome": "Dieimes",
     "Endereço": "Rua ABC, 123",
     "Telefone": "988179995"

}

print (dados_cliente ["LEOMAR"])

dados_cliente["Cidade"]="ivaipora"
print (dados_cliente)

dados_cliente.pop("Telefone")  #para remover um item do dicionário, podemos usar o metado pop()

for indece, valor in dados_cliente.items():
    print=(f"indice:{indice},valor: {valor}")
