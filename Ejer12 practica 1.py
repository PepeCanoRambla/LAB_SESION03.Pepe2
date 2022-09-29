h=int(input('Dime cuantas horas estará el coche en el parking: '))
if h<24:
    print('El importe a pagar no se puede calcular')
else:
    if h==24:
        print('El importe a pagar es de 11€')
    else:
        if h>24 and h<=120:
            print('El importe a pagar es de {0}€'.format(11+(h//24)*6))
        else:
            if h>120 and h<=336:
                print('El importe a pagar es de {0}€'.format(11+(h//24)*5.5))
            else:
                if h>337:
                    print('El importe a pagar es de 110€')
                else:
                    if h>=720:
                        print('El importe a pagar no se puede calcular')
                
