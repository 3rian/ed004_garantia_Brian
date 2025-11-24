-- Criação das tabelas
CREATE TABLE IF NOT EXISTS equipamentos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_compra DATE NOT NULL,
    preco NUMERIC(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS garantias (
    id SERIAL PRIMARY KEY,
    equipamento_id INTEGER REFERENCES equipamentos(id) ON DELETE CASCADE,
    data_inicio DATE NOT NULL,
    duracao_meses INTEGER NOT NULL,
    tipo VARCHAR(50) NOT NULL
);

-- Inserindo alguns exemplos
INSERT INTO equipamentos (nome, data_compra, preco) VALUES
('Notebook Dell', '2023-01-10', 4500.00),
('Impressora HP', '2022-12-05', 800.00);

INSERT INTO garantias (equipamento_id, data_inicio, duracao_meses, tipo) VALUES
(1, '2023-01-10', 24, 'Estendida'),
(2, '2022-12-05', 12, 'Padrão');
