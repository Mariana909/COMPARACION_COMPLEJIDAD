with open("entrada.txt", "w") as f:
    base = "a b bas"
    
    for i in range(1, 334):  # 3 * 333 = 999 tokens
        linea = " ".join([base]*i)
        f.write(linea + "\n")