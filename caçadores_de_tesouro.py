N = int(input());

coordenadas_anteriores = set();
mesmo_lugar = False;

for i in range(N):
    
    coordenadas = input()

    if coordenadas in coordenadas_anteriores :
        mesmo_lugar = True;

    coordenadas_anteriores.add(coordenadas);

if mesmo_lugar: 
    print(1);
else: 
    print(0);

