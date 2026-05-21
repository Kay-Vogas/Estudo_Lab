
N = int(input())
teste_numero = 1

while N != 0:

    possibilidades_senha = [[], [], [], [], [], []]
    
     
    for i in range(N):
        dados_senha = list(map(str, input().split()))

         
        numeracao_senha = []
        for z in range(10):  
            numeracao_senha.append(int(dados_senha[z]))

     
        letras_senha = []
        for j in range(10, len(dados_senha)):
            letras_senha.append(dados_senha[j])

         
        for k in range(6):   
            letra_digitada = letras_senha[k]
            
             
            if letra_digitada == 'A':
                d1, d2 = numeracao_senha[0], numeracao_senha[1]
            elif letra_digitada == 'B':
                d1, d2 = numeracao_senha[2], numeracao_senha[3]
            elif letra_digitada == 'C':
                d1, d2 = numeracao_senha[4], numeracao_senha[5]
            elif letra_digitada == 'D':
                d1, d2 = numeracao_senha[6], numeracao_senha[7]
            elif letra_digitada == 'E':
                d1, d2 = numeracao_senha[8], numeracao_senha[9]
            
            if i == 0:
                possibilidades_senha[k] = [d1, d2]

            else:
                numeros_em_comum = []
                
                if d1 in possibilidades_senha[k]:
                    numeros_em_comum.append(d1)
                
                if d2 in possibilidades_senha[k]:
                    numeros_em_comum.append(d2)

                possibilidades_senha[k] = numeros_em_comum    

    print(f"Teste {teste_numero}")
    
    for pos in range(6):
        senha_verdadeira = possibilidades_senha[pos][0]
        print(senha_verdadeira, end=" ") 
    
    teste_numero += 1
    N = int(input())  