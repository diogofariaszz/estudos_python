def bin_to_dec(binary):
    return int(binary, 2)

def dec_to_bin(decimal):
    return bin(decimal)[2:]

def hex_to_dec(hexadecimal):
    return int(hexadecimal, 16)

def dec_to_hex(decimal):
    return hex(decimal)[2:]

def bin_to_hex(binary):
    decimal = bin_to_dec(binary)
    return dec_to_hex(decimal)

def hex_to_bin(hexadecimal):
    decimal = hex_to_dec(hexadecimal)
    return dec_to_bin(decimal)

def main():
    print("Escolha a base numérica do número:")
    print("1. Binário")
    print("2. Decimal")
    print("3. Hexadecimal")
    base_origem = int(input("Digite o número correspondente à base escolhida: "))

    numero_origem = input("Digite o número na base escolhida: ")

    print("Escolha a base numérica para conversão:")
    print("1. Binário")
    print("2. Decimal")
    print("3. Hexadecimal")
    base_destino = int(input("Digite o número correspondente à base escolhida: "))

    if base_origem == 1:  # Binário
        if base_destino == 2:  # Binário para Decimal
            resultado = bin_to_dec(numero_origem)
        elif base_destino == 3:  # Binário para Hexadecimal
            resultado = bin_to_hex(numero_origem)
        else:
            resultado = numero_origem
    elif base_origem == 2:  # Decimal
        if base_destino == 1:  # Decimal para Binário
            resultado = dec_to_bin(int(numero_origem))
        elif base_destino == 3:  # Decimal para Hexadecimal
            resultado = dec_to_hex(int(numero_origem))
        else:
            resultado = numero_origem
    elif base_origem == 3:  # Hexadecimal
        if base_destino == 1:  # Hexadecimal para Binário
            resultado = hex_to_bin(numero_origem)
        elif base_destino == 2:  # Hexadecimal para Decimal
            resultado = hex_to_dec(numero_origem)
        else:
            resultado = numero_origem
    else:
        resultado = "Entrada inválida!"

    print("Resultado da conversão:", resultado)


if __name__ == "__main__":
    main()
