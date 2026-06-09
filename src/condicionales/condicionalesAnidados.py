edad = 30
estado_civil = 'soltero'

if edad >= 18:
    if estado_civil == 'casado':
        print('Eres un adulto casado.')
    else:
        print('Eres un adulto soltero.')
else:
    print('Eres menor de edad.')

    #Ejemplo de anidados combinando elif y else

    edad = 16
permiso_padres = True

if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
else:
    if edad >= 16:
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.')
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.')
    else:
        print('Eres demasiado joven para conducir.')

#mismo ejemplo de licencia usando and y not

        edad = 16
permiso_padres = True

if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
elif edad >= 16 and permiso_padres:
    print('Puedes obtener la licencia con permiso de tus padres.')
elif edad >= 16 and not permiso_padres:
    print('Necesitas el permiso de tus padres para obtener la licencia.')
else:
    print('Eres demasiado joven para conducir.')

    #condicion evaluado dentro del contexto de otra ejemplo

    usuario = 'admin'
contrasena = '1234'

if usuario == 'admin':
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario no reconocido.')
    