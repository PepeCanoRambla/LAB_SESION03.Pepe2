T=float(input('Valor para la temperatura:' ))
V=float(input('Valor para la velocidad del viento:' ))
Ts=13.12+0.6215*T-11.37*(V**0.16)+0.3965*T*(V**0.16)
print('El valor de la temperatura de sensación es igual a {0:.2f} grados.'.format(Ts))
