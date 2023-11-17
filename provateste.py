testeA = [
     "Como posso atualizar meu cartão de crédito?", "Preciso mudar a forma de pagamento, o que fazer?", "Quero atualizar minhas informações de pagamento", "Método de pagamento desatualizado, como proceder para atualizar?"
]

sair = True

input_text = ""






def solicite(a):
    intencoes = {}
    acoes = {}
    input_text = a
    if input_text == "sair":
        return False
    return True






while sair:
    sair = solicite(input("Solicite algo ?"))


