#Participantes e Rodadas
P,R = map(int , input().split());

teste_numero = 1

while P != 0 and R != 0:

    #dentro da rodada
    ordem_fila = list(map(int, input().split()));

    for i in range(R):

        dados_da_rodada = list(map(int, input().split()));

        N = dados_da_rodada[0]
        ordem_vivo_morto = dados_da_rodada[1];
        ordem_vivo_morto_participantes = [];
        
        for j in range(2, len(dados_da_rodada)):
            ordem_vivo_morto_participantes.append(dados_da_rodada[j]);

        restantes = [];

        for k in range(N):
            if ordem_vivo_morto_participantes[k] == ordem_vivo_morto:
                restantes.append(ordem_fila[k]);

        ordem_fila = restantes;
    
    print(f"Teste {teste_numero}");
    print(ordem_fila[0]); 
    print();

    teste_numero+=1;

    P,R = map(int , input().split());

