import re



testeA = [
     "Como posso atualizar meu cartão de crédito?", "Preciso mudar a forma de pagamento, o que fazer?", "Quero atualizar minhas informações de pagamento", "Método de pagamento desatualizado, como proceder para atualizar?"
]

sair = True

input_text = ""




# $(como)|$(Como) & (atualizar) & (crédito) 
# (forma) (pagamento) *(Preciso)
# (pagamento) (atualizar)
# $(Método) (pagamento) ^(atualizar)
# (mudar) (forma de pagamento) 

def solicite(a):
    intencoes = {

    }
    acoes = {
        'forma de pagamento':"",
        'atualizar pagamento':"",
        'metodo de pagamento':"",
        'mudar forma de pagamento':"",
    }
    input_text = a
    if input_text == "sair":
        return False
    matches = re.findall(r'[+-]?\d+(?:\.\d+)?', input_text)
    print(matches)
    
    return True






while sair:
    sair = solicite(input("Solicite algo ?"))


