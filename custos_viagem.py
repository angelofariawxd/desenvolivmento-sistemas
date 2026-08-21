class Carro:

    def __init__(self, consumo_km_l, preco_combustivel):
        self.consumo_km_l = consumo_km_l  # ex: 10 km por litro
        self.preco_combustivel = preco_combustivel  # ex: R$ 5.50 por litro

    def calcular_custo_viagem(self, distancia_km):
        litros_necessarios = distancia_km / self.consumo_km_l
        return litros_necessarios * self.preco_combustivel


class Moto:

    def __init__(self, consumo_km_l, preco_combustivel, taxa_pedagio_moto=5.0):
        self.consumo_km_l = consumo_km_l
        self.preco_combustivel = preco_combustivel
        self.taxa_pedagio_moto = taxa_pedagio_moto

    def calcular_custo_viagem(self, distancia_km):
        litros_necessarios = distancia_km / self.consumo_km_l
        custo_combustivel = litros_necessarios * self.preco_combustivel
        return custo_combustivel + self.taxa_pedagio_moto


class Eletrico:

    def __init__(self, consumo_kwh_km, preco_kwh):
        self.consumo_kwh_km = consumo_kwh_km  # ex: 0.18 kWh por km
        self.preco_kwh = preco_kwh  # ex: R$ 0.80 por kWh

    def calcular_custo_viagem(self, distancia_km):
        kwh_necessarios = distancia_km * self.consumo_kwh_km
        return kwh_necessarios * self.preco_kwh


def calcular_custo_total_viagem(veiculos, distancia_km=200):
    custo_total = 0

    for veiculo in veiculos:
        # Polimorfismo: cada objeto calcula seu próprio custo conforme sua regra
        custo_individual = veiculo.calcular_custo_viagem(distancia_km)
        custo_total += custo_individual

    return custo_total


# --- Exemplo de Uso ---
frota = [
    Carro(consumo_km_l=10, preco_combustivel=5.50),  # Custo: R$ 110.00
    Moto(
        consumo_km_l=25, preco_combustivel=5.50, taxa_pedagio_moto=5.0
    ),  # Custo: R$ 49.00
    Eletrico(consumo_kwh_km=0.18, preco_kwh=0.80),  # Custo: R$ 28.80
]

distancia = 200
total = calcular_custo_total_viagem(frota, distancia)

print(f"Custo total da viagem de {distancia} km para a frota: R$ {total:.2f}")
}
