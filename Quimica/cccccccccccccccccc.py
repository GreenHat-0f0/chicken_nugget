CInicial = float(input("Digite a concentração inicial: "))
CFinal = float(input("Digite a concentração final desejada: "))
VFinal = float(input("Digite o volume final da solução em mL: "))
VInicial = (CFinal * VFinal)/CInicial 
print("\nVolume da solução inicial necessário =", VInicial, "mL")