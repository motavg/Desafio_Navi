def contar_pares():
    pares = 0
    for number in range(1,5000001):
        if number % 49 == 0 and number % 37 == 0 and number % 2 == 0:
            pares += 1
    return pares

print(f"São {contar_pares()} números pares e múltiplos de 49 e 37")
