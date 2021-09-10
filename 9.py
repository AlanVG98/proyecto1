#propinas
print("Cuanto fue el total de su compra?")
bruto = float(input())
propina = round(bruto * 0.18,2)
print("La propina sugerida es de $",propina)
print("El total de su compra es de $",round(bruto+propina,2))