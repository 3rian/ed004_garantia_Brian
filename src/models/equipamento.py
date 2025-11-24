class Equipamento:
    def __init__(self, id, nome, data_compra, preco):
        self.id = id
        self.nome = nome
        self.data_compra = data_compra
        self.preco = preco
    def __str__(self):
        return f"{self.nome} ({self.data_compra})"