class Loja:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.equipamentos = []  # lista de objetos da classe Equipamento
        self.garantias = []     # lista de objetos da classe Garantia

    def adicionar_equipamento(self, equipamento):
        """Adiciona um equipamento à loja."""
        self.equipamentos.append(equipamento)

    def adicionar_garantia(self, garantia):
        """Adiciona uma garantia à loja."""
        self.garantias.append(garantia)

    def listar_equipamentos(self):
        """Lista todos os equipamentos da loja."""
        return [str(equip) for equip in self.equipamentos]

    def listar_garantias(self):
        """Lista todas as garantias da loja."""
        return [str(g) for g in self.garantias]

    def buscar_equipamento_por_nome(self, nome):
        """Procura equipamentos pelo nome (case-insensitive)."""
        return [e for e in self.equipamentos if nome.lower() in e.nome.lower()]

    def __str__(self):
        return f"Loja: {self.nome} ({self.endereco}) - {len(self.equipamentos)} equipamentos"
