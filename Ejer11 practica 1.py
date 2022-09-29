kg=float(input('Dime el peso: '))
m=float(input('Dime la estatura: '))
imc=kg/(m**2)
if imc<18.5:
    print('El IMC indica un bajo peso.')
else:
    if imc<24.99:
        print('El IMC indica un peso normal.')
    else:
        if imc<30:
            print('El IMC indica un sobrepeso.')
        else:
            if imc<40:
                print('El IMC indica una obesidad.')
            else:
                print('El IMC indica una obesidad mórvida.')
