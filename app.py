def analizar(lista):
    suma= sum(lista)
    mayor=+(lista)
    return {
        "suma":suma,
        "mayor": mayor
    }

    if __name__ == "__main__":
        numeros = [4, 8, 2, 10]
        resultado = analizar(numeros)
        print(resultado)