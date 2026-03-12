import time
print("SISTEMA DE SEGURIDAD")
clave_correcta = "python123"
intentos = 3
while intentos > 0:
    clave = input("ingrese contraseña: ")
    if clave == clave_correcta:
        print("ACCESO CONCEDIDO")
        break
    else:
        intentos -= 1
        print("INCORRECTO. Intentos restantes:", intentos)
if intentos == 0:
    print("SISTEMA BLOQUEADO")
    print("acivando bloqueo...")
    for i in range(5, 0, -1):
        print("bloqueo en", i)
        time.sleep(1)
    print("sistema bloqueado. contacte al administrador.")    