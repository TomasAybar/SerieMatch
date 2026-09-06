def normalizar_json_local(dato_crudo: dict) -> dict:
    return {
        "id": int(dato_crudo.get("id", 0)),
        "titulo": dato_crudo.get("titulo", "Sin título"),
        "generos": dato_crudo.get("generos", []),
        "duracion_min": int(dato_crudo.get("duracion_min", 0)),
        "puntuacion": float(dato_crudo.get("puntuacion", 0.0)),
        "plataforma": dato_crudo.get("plataforma", "Desconocida"),
        "sinopsis": dato_crudo.get("sinopsis", "Sin sinopsis"),
    }
