def tokenizar_enteros(codigo):
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
            else:
                return f"ERROR LEXICO cerca de '{buffer}'"
                
        # --- ESTADO 2: Parte Entera ---
        elif estado == 2:
            if c.isdigit():
                buffer += c
                i += 1
            else:
                tokens.append(('NUMERO_ENTERO', buffer))
                buffer = ""
                estado = 0
                


    # Cierre de búfer al final del archivo
    if estado == 2:
        tokens.append(('NUMERO_ENTERO', buffer))
    elif estado == 1:
        return "ERROR LEXICO: Signo sin numero al final"

    return tokens


# Prueba con flujo de código
codigo_fuente = "tono base = 125; tono vueltas= -087;"
print(tokenizar_reales(codigo_fuente))
