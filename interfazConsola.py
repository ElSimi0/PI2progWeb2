colores = {"rojo": "\033[1;31m",
           "verde": "\033[1;32m",
           "amarillo": "\033[1;33m",
           "morado": "\033[1;35m",
           "blanco": "\033[1;37m",
           "azulClaro": "\033[1;36m",
           "azulOscuro": "\033[0;34m",
           "naranja": "\033[38;5;208m",
           "violeta": "\033[38;5;165m"}

def citas(nombre: str, apellido: str, edad: str, tipoSangre: str,historial: str, examenes: str, examen, clinica: str, fecha, docName, doc4Name) -> str:
    nombre = nombre.replace("-", " ")
    apellido = apellido.replace("-", " ")
    #examen $ == resultado, # == N/A
    #cita = f"\n╔══════════════════════╗\n║PACIENTE:             ║\n║»{nombre:^20} ║\n║»{apellido:^20} ║\n║»{edad:^20} ║\n║»{historial:^20} ║\n║»{fecha:^20} ║\n╚══════════════════════╝"
    if len(nombre) >= 26:
        nombre = nombre[0:25]
    else:
        pass
    if len(apellido) >= 26:
        apellido = apellido[0:25]
    else:
        pass
    historial = str(historial)
    print("\n╔══════════════════════════════════════════════════════╗")
    print("║PACIENTE:                                             ║")
    print(f"║»{nombre:^52} ║")
    print(f"║ {apellido:^52} ║")
    print("║══════════════════════════════════════════════════════║")
    print("║DOCTOR:                                               ║")
    print(f"║»{docName:^52} ║")
    print(f"║ {doc4Name:^52} ║")
    print("║══════════════════════════════════════════════════════║")
    print("║EDAD:                                                 ║")
    print(f"║»{edad:^52} ║")
    print("║HISTORIAL:                                            ║")
    if len(historial) >= 51:
        print(f"║»{historial[0:50]:^52} ║")
        print(f"║ {historial[50:100]:^52} ║")
        if len(historial) >= 101:
            print(f"║ {historial[100:150]:^52} ║")
            if len(historial) >= 151:
                print(f"║ {historial[150:200]:^52} ║")
                if len(historial) >= 201:
                    pass
    elif len(historial) == 0:
        historial = "########"
        print(f"║»{historial:^52} ║")
    else:
        print(f"║»{historial:^52} ║")
    if examenes:
        exam = "Si"
        print(f"║Examenes:{exam:^45}║")
        for exams in str(examen).split(","):
            examenTexto = exams.replace(',', '').replace('{', '').replace('}', '').replace(':', '').replace("'", "").replace(" ", "").replace("-", " ").replace("$", " : ").replace("#", " : N/A")
            print(f"║  *  {examenTexto:<49}║")
    else:
        exam = "No"
        print(f"║»{exam:^52} ║")
    print("║Fecha de Cita:                                        ║")
    print(f"║»{fecha:^52} ║")
    print("╚══════════════════════════════════════════════════════╝")

