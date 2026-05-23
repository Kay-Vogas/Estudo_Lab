## Pontos médios de picos
# M = int(input());
## Valores dos picos de M  
# H = list(map(int, input()));

# Nº de Trilhas
N = int(input());

melhor_trilha = 0;
melhor_calculo_energetico = 99999;

for i in range(N):

    input_desejado_m_h = list(map(int, input().split()));
    M = input_desejado_m_h[0]
    H = input_desejado_m_h[1:]

    calculo_energetico_da_trilha_ida = 0;
    calculo_energetico_da_trilha_volta = 0;

    for j in range(M-1):

        if  H[j+1]>H[j]:        
            calculo_energetico_da_trilha_ida += H[j+1]- H[j];

        elif H[j]>H[j+1]:
            calculo_energetico_da_trilha_volta += H[j] - H[j+1];

    calculo_energetico_da_trilha = min(calculo_energetico_da_trilha_ida,calculo_energetico_da_trilha_volta);

    if  melhor_calculo_energetico > calculo_energetico_da_trilha:
        melhor_calculo_energetico = calculo_energetico_da_trilha;
        melhor_trilha = i + 1;

print(melhor_trilha);


# 5
# 4 498 500 498 498
# 10 60 60 70 70 70 70 80 90 90 100
# 5 200 190 180 170 160
# 2 1000 900
# 4 20 20 20 20

# 3
# 5 600 601 600 601 600
# 4 500 499 500 499
# 4 300 300 302 300
