def tokenizar_reales(codigo):
    n = len(codigo)
    tokens = []
    estado = 0
    i = 0
    buffer = ""
    
    while i < n:
        c = codigo[i]
        
        
        if estado == 0:
            if c in ('+', '-'):
                buffer += c
                i += 1
                estado = 1
            elif c.isdigit():
                buffer += c
                i += 1
                estado = 2
            elif c in (' ', '\n', '\t'):
                i += 1  
            else:
                i += 1  
                
        elif estado == 1:
            if c.isdigit():
                buffer += c
                i += 1
                estado = 2
            elif c == '.':
                buffer += c
                i += 1
                estado = 3
            else:
                return f"ERROR LEXICO cerca de '{buffer}'"
                
       
        elif estado == 2:
            if c.isdigit():
                buffer += c
                i += 1
            elif c == '.':
                buffer += c
                i += 1
                estado = 3
            else:
                tokens.append(('NUMERO_ENTERO', buffer))
                buffer = ""
                estado = 0
                
       
        elif estado == 3:
            if c.isdigit():
                buffer += c
                i += 1
                estado = 4
            else:
                return f"ERROR LEXICO en decimal '{buffer}'"
                
       
        elif estado == 4:
            if c.isdigit():
                buffer += c
                i += 1
            else:
                tokens.append(('NUMERO_REAL', buffer))
                buffer = ""
                estado = 0

   
    if estado == 2:
        tokens.append(('NUMERO_ENTERO', buffer))
    elif estado == 4:
        tokens.append(('NUMERO_REAL', buffer))
    elif estado in (1, 3):
        return "ERROR LEXICO: Número incompleto al final"

    return tokens



codigo_fuente = "tono resultado = -087.98; Sonar 0.870; +4.6 125"
print(tokenizar_reales(codigo_fuente))  
    while i < len(cadena):
        c = cadena[i]
        
        if estado == 0:
            if c in ('+', '-'):
                estado = 1  # Signo opcional
            elif c.isdigit():
                estado = 2  # Inicio de parte entera
            elif c == '.':
                estado = 3  # Inicia directamente con punto deci           else:
                return "No válido (carácter inicial incorrecto)"
                
        elif estado == 1:
            if c.isdigit():
                estado = 2
            elif c == '.':
                estado = 3
            else:
                return "No válido (se esperaba dígito o punto)"
                
        elif estado == 2:
            if c == '.':
                estado = 3  # Transición al punto decimal
            elif not c.isdigit():
                return "Número no válido"
                
        elif estado == 3:
            if not c.isdigit():
                return "Número decimal no válido"
                
        i += 1

    if estado == 2:
        return "Número Entero Válido"
    elif estado == 3:
        return "Número Real Válido"
    
    return "Cadena no válida"

entradas = ["45.67", "-087.98", "0.870", ".587", "+4.6", "125", "45.67.89", "12a.5"]

for e in entradas:
    print(f"'{e}' -> {analizar_numero_real(e)}")
