def analizar(lista):
    menor=min(lista)
    promedio = sum(lista/len(lista))
    return{
        "menor": menor,
        "promedio": promedio 
        }

    if __name__ == "__main__":
        numeros = [4, 8, 2, 10]
        resultado = analizar(numeros)
        print(resultado)