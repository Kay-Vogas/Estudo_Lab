
N = int(input());

pilhas = list(map(int,input().split()));
total_pedras = 0;
base_da_escada = 0;

total_pedras = sum(pilhas);

for j in range(N):
    base_da_escada+=j;

base_da_escada = total_pedras - base_da_escada;

if base_da_escada % N == 0:

    pilha_dividendo =  base_da_escada // N ;

    movimentos = 0 ;

    for k in range(N):

        altura_desejada = pilha_dividendo + k;

        if pilhas[k] > altura_desejada:
            movimentos += (pilhas[k] - altura_desejada)
    
    print(movimentos);
else:
    print(-1);

