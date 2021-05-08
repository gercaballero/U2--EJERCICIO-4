from claseFechaHora import FechaHora

def test():
    print('  -----------TEST DE FECHAS-----------')
    print('\n\nFECHA 1: 10/5/20  10HS')
    f1=FechaHora(10,5,2021,10)
    f1.Mostrar()
    print('\n\nFECHA 2: 10/5/20  10HS 20MIN')
    f2=FechaHora(10,5,2021,10,20)
    f2.Mostrar()
    print('\n\nFECHA 3: 10/5/20  10HS 20MIN 10 SEG')
    f3=FechaHora(10,5,2021,10,20,10)
    f3.Mostrar()
    print('\n\nFECHA 4: CON DATOS NO ENTEROS')
    f4=FechaHora('HOLA',5,2021)
    f4.Mostrar()
    print('\n\nFECHA 5: CON DATOS NO ENTEROS')
    f5=FechaHora(10.4,5,9.2,1.1,1.02)
    f5.Mostrar()
    print('------------------------------------------\n')
    

if __name__ == '__main__':
    t=str(input('DESEA PROBAR EL TEST (S/N) : '))
    if t.lower()=='s':
        test() 
    d=int(input("Ingrese Dia: "))
    mes=int(input("Ingrese Mes: "))
    a=int(input("Ingrese Año: "))
    h=int(input("Ingrese Hora: "))
    m=int(input("Ingrese Minutos: "))
    s=int(input("Ingrese Segundos: "))
    r = FechaHora () #  inicilizar día, mes, año con 1/1/2020, y hora, minutos y 
                              #  segundos con 0h, 0m, 0s.
    r1 = FechaHora(d,mes,a); # inicializar con 0h 0m 0s
    r2= FechaHora(d,mes,a,h, m, s)
    r.Mostrar()
    r1.Mostrar()
    r2.Mostrar()
    input()
    r.PonerEnHora(5) # solamente la hora
    r.Mostrar()
    input()
    r2.PonerEnHora(13,30) #hora y minutos
    r2.Mostrar()
    input()
    r.PonerEnHora(14, 30, 25) #hora, minutos y segundos
    r.Mostrar()
    input()
    r.AdelantarHora(3) #sumar 3 horas a la hora actual
    r.Mostrar()
    input()
    r1.AdelantarHora(1,15) #sumar 1 hora y 15 minutos a la hora actual
    r1.Mostrar()
    input()