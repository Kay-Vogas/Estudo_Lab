numeroTeste = 1;

while True:
    ganhador = -1;

    N = int(input());

    if N==0:
        break;

    ingressos = list(map(int,input().split()));
    
    for i,ingresso in enumerate(ingressos,1):
        if ingresso == i:
            ganhador = i;
            break;

    print(f"Teste {numeroTeste}")
    print(ganhador)
    print() 
            
    numeroTeste += 1

