def tokenizar_reales(codigo):
    n = len(codigo)
    tokens = []
    estado = 0
    i = 0
    buffer = ""
    
    while i < n:
        c = codigo[i]
        
        # --- ESTADO 0: Inicio ---
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
                i += 1  # Omitir delimitadores
            else:
                i += 1  # Avanzar si encuentra otros caracteres
                
        # --- ESTADO 1: Tras signo (+ o -) ---
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
                
        # --- ESTADO 2: Parte Entera ---
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
                
        # --- ESTADO 3: Punto Decimal ---
        elif estado == 3:
            if c.isdigit():
                buffer += c
                i += 1
                estado = 4
            else:
                return f"ERROR LEXICO en decimal '{buffer}'"
                
        # --- ESTADO 4: Parte Decimal ---
        elif estado == 4:
            if c.isdigit():
                buffer += c
                i += 1
            else:
                tokens.append(('NUMERO_REAL', buffer))
                buffer = ""
                estado = 0

    # Cierre de búfer al final del archivo
    if estado == 2:
        tokens.append(('NUMERO_ENTERO', buffer))
    elif estado == 4:
        tokens.append(('NUMERO_REAL', buffer))
    elif estado in (1, 3):
        return "ERROR LEXICO: Número incompleto al final"

    return tokens


# Prueba con flujo de código
codigo_fuente = "tono resultado = -087.98; Sonar 0.870; +4.6 125"
print(tokenizar_reales(codigo_fuente))
