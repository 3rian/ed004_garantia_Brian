from datetime import date

class Garantia:
    def __init__(self, id, equipamento, data_inicio, data_fim, tipo):
        self.id = id
        self.equipamento = equipamento  # instância da classe Equipamento
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.tipo = tipo

    def esta_valida(self):
        """Verifica se a garantia ainda está dentro do prazo."""
        hoje = date.today()
        return self.data_inicio <= hoje <= self.data_fim

    def dias_restantes(self):
        """Retorna o número de dias restantes da garantia."""
        hoje = date.today()
        if hoje > self.data_fim:
            return 0
        return (self.data_fim - hoje).days

    def __str__(self):
        status = "Válida" if self.esta_valida() else "Expirada"
        return (f"Garantia {self.tipo} do equipamento '{self.equipamento.nome}' "
                f"({status}, até {self.data_fim})")
