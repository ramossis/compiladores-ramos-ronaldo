def analizar_token_reservadas(cadena):
    cadena = cadena.strip()
    if not cadena:
        return "Cadena vacía"
    
    PALABRAS_RESERVADAS = {
        "tono", 
        "Sonar", 
        "Si_Compas", 
        "Sino", 
        "Pulsacion"
    }
    
    estado = 0
    i = 0
    
    while i < len(cadena):
        c = cadena[i]
        
       
        if estado == 0:
            if c.isalpha() or c == '_':
                estado = 1  
            else:
                return "No válido / Desconocido"
                
       
        elif estado == 1:
            if not (c.isalnum() or c == '_'):
                return "Lexema alfanumérico no válido"
                
        i += 1

   
    if estado == 1:
        if cadena in PALABRAS_RESERVADAS:
            return f"Palabra Reservada Válida: '{cadena}'"
        else:
            return f"Identificador Válido: '{cadena}'"

    return "Cadena no válida"



entradas = ["tono", "Sonar", "Si_Compas", "Sino", "Pulsacion", "variable1", "_contador", "tono123"]

for e in entradas:
    print(f"'{e}' -> {analizar_token_reservadas(e)}")
