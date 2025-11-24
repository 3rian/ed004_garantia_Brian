from database import Database  # importa a classe Database (salva em database.py)
from datetime import date

def main():
    db = Database()

    # Consulta SQL que junta equipamentos com suas garantias
    query = """
        SELECT 
            e.id,
            e.nome,
            e.data_compra,
            e.preco,
            g.id AS garantia_id,
            g.tipo,
            g.data_inicio,
            g.data_fim
        FROM equipamentos e
        LEFT JOIN garantias g ON e.id = g.equipamento_id
        ORDER BY e.id;
    """

    resultados = db.consultar(query)

    print("=== LISTA DE EQUIPAMENTOS E GARANTIAS ===\n")

    if not resultados:
        print("Nenhum registro encontrado.")
    else:
        for linha in resultados:
            (equip_id, nome, data_compra, preco,
             garantia_id, tipo, data_inicio, data_fim) = linha

            print(f"Equipamento #{equip_id}: {nome}")
            print(f"  Data da compra: {data_compra}")
            print(f"  Preço: R$ {preco:.2f}")

            if garantia_id:
                print(f"  Garantia ({tipo}): {data_inicio} até {data_fim}")
            else:
                print("  Nenhuma garantia cadastrada.")

            print("-" * 50)

    db.fechar()  # fecha a conexão com o banco

if __name__ == "__main__":
    main()
