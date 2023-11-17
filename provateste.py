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
        r'/^(Como)/':"como",
        r'/(89890898)/':"mudar",
        r'/(d08980)/':"metodo",

    }
    acoes = {
        'como':"Vá para aba meus cartões e entre em meu cartão de crédito",
        'mudar':"Vá para aba meus pagamentos",
        'metodo de pagamento':"Vá para aba mudar forma de pagamento",
    }
    input_text = a
    if input_text == "sair":
        return False
   # print()

    #if acoes[(intencoes[input_text]).lower()]:
        print(acoes[intencoes[input_text]])
    
    #else:
       # print("Não entendi")

    
    return True






while sair:
    sair = solicite(input("Solicite algo ?"))


